// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

import "./Split.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract HackSplit {
    Split public splitContract;

    constructor(Split _splitContract) {
        splitContract = _splitContract;
    }

    function interactWithDistribute(
        uint256 splitId,
        address[] memory accounts,
        uint32[] memory percents,
        uint32 relayerFee,
        IERC20 token
    ) public {
        // Call distribute function
        splitContract.distribute(splitId, accounts, percents, relayerFee, token);
    }
    
    function interactWithWithdraw(
        IERC20[] memory tokens,
        uint256[] memory amounts
    ) public {
        // Call withdraw function
        splitContract.withdraw(tokens, amounts);
    }

    receive() external payable {}

    fallback() external payable {}
}