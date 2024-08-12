# Lottery SALF Alvise Salary: Polygon Lottery Project with Python and Smart Contracts

TLDR: This project uses a Smart Contract deployed on the Polygon network to conduct a lottery in a transparent and decentralized manner. The Smart Contract uses Chainlink VRF to generate a verifiable random number.

This is a unofficial MPV as example of demostration as open source of build in public a kind of application for donate the salary of 10.000€ of euro deputy, following the small spec/requirements disclosed by Alvise Perez (SALF) (aka SALFLottery) in his [website](https://www.alvisecumpliendo.com/como-funciona).

The Alvise Contract Address: [0x6469eadA60A24Ac6e871F314916c11da960010eA](https://polygonscan.com/address/0x6469eadA60A24Ac6e871F314916c11da960010ea) which was created 2024-08-02 21:47:44

The transfer loads from owner [0x04EcC5ba3258840725FD808BE0fAE3430B8346F2](https://polygonscan.com/address/0x04ecc5ba3258840725fd808be0fae3430b8346f2):

- [Loaded with 33 MATIC @ ($13.41)](https://polygonscan.com/tx/0xb51cb81ee3c85ad3fe0687958c1cd78ea036c1b4206287d85e2f56cdb65334e4)
- [Loaded with 129.26953363 MATIC @ ($52.67)](https://polygonscan.com/tx/0xd91dad2b0b02e01b60546accfae84423743e43b9e716625d2b363b40e714e4d0)

## Requirements of problem to solve

The Smart Contract is used to generate a random number that will be selected, ensuring fairness and transparency in the process.

The Smart Contract will be deployed on the public Polygon network and a unique contract address will be obtained from the blockchain network. To review the source code of the Smart Contract and the associated transactions, it can be accessed on the Polygon blockchain using a block explorer such as PolygonScan.

To ensure fairness and randomness in the generation of the number, the Smart Contract uses Chainlink v2.5, a decentralized oracle technology. Chainlink provides a Verifiable Random Function (VRF) that guarantees the fairness of the choice by being unpredictable and publicly verifiable. This means that:

No one can predict the number before its generation.
After its generation, anyone can verify that the number is truly random and has not been manipulated.

## Principles of the process

- Decentralization: Decentralization ensures that no centralized entity has control over the generation of the random number, thus eliminating the possibility of manipulation.

- Automation: The Smart Contract automatically executes the generation of the random number through an action verb linked to the Chainlink VRF service. This ensures that the process is executed impartially and without human intervention.

- Transparency: All Smart Contract activity, including the request and generation of the random number, is publicly recorded on the Polygon blockchain. This allows anyone to verify the process and ensure that there has been no manipulation.

- Immutability: Once deployed on the blockchain, the Smart Contract source code cannot be altered. This guarantees that the random number generation process is always carried out under the same conditions initially established, providing trust to the participants.

## Requirements

- Python 3.8+
- Virtualenv
- Access to the Polygon network
- Private key for a Polygon account
- LINK tokens to pay for the Chainlink VRF service
  
### 1. Clone the Repository

```bash
git clone https://github.com/shakaran/lottery-salf-alvise-salary.git
cd lottery-salf-alvise-salary
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv;source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Configure Environment Variables

Modify the .env file in the root of the project for your variables:

```
WEB3_PROVIDER_URL=https://polygon-rpc.com
CONTRACT_ADDRESS=0xYourContractAddressHere
PRIVATE_KEY=your-private-key-here
CHAIN_ID=137  # Polygon's Chain ID
GAS_LIMIT=300000
```

### 5. Run the Script

Ensure the virtual environment is activated and run the following command to select a winner:

```bash
python select_winner.py
```

Notes

- Make sure you have enough MATIC tokens in your account to cover gas fees.
- Please note that the Chainlink VRF service requires LINK tokens.
