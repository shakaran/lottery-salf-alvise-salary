// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract Lottery is VRFConsumerBase {
    address[] public donors;
    address public recentWinner;
    uint256 public randomness;
    uint256 public fee;
    bytes32 public keyHash;
    address public owner;

    event WinnerSelected(address winner);

    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyHash,
        uint256 _fee
    ) VRFConsumerBase(_vrfCoordinator, _linkToken) 
    {
        keyHash = _keyHash;
        fee = _fee;
        owner = msg.sender;
    }

    function enterLottery(address donor) public 
    {
        require(msg.sender == owner, "Only the owner can enter donors.");
        donors.push(donor);
    }

    function pickWinner() public returns (bytes32 requestId) 
    {
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK to pay fee");
        require(donors.length > 0, "No donors entered in the lottery");
        return requestRandomness(keyHash, fee);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomness) internal override 
    {
        uint256 indexOfWinner = randomness % donors.length;
        recentWinner = donors[indexOfWinner];
        emit WinnerSelected(recentWinner);
    }

    function getWinner() public view returns (address) 
    {
        return recentWinner;
    }
}