// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.9;

contract Dappazon {
    address public owner;

    struct Item {
        uint256 id;
        string name;
        string category;
        string image;
        uint256 cost;
        uint256 rating;
        uint256 stock; 
    }

    struct Order {
        uint256 time;
        Item item;
    }

    struct Ledger{
        uint256 time;
        uint256 amount;
        bool isComplete;
        bool isDelivered;
        bool isReceived;
    }
}