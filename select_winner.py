from web3 import Web3
from web3.middleware import geth_poa_middleware
import os
from dotenv import load_dotenv

load_dotenv()

web3_provider_url = os.getenv('WEB3_PROVIDER_URL')
contract_address = os.getenv('CONTRACT_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')
chain_id = int(os.getenv('CHAIN_ID'))
gas_limit = int(os.getenv('GAS_LIMIT'))

# Connect to Polygon network
web3 = Web3(Web3.HTTPProvider(web3_provider_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Load ABI (Application Binary Interface) from a JSON file 
with open('abi.json', 'r') as abi_file:
    contract_abi = abi_file.read()

# Initialize the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Function to select a winner
def transfer_and_call(to_address, value, data):
    account = web3.eth.account.privateKeyToAccount(private_key)
    tx = contract.functions.transferAndCall(to_address, value, data).buildTransaction({
        'chainId': chain_id,
        'gas': gas_limit,
        'nonce': web3.eth.getTransactionCount(account.address),
    })
    signed_tx = web3.eth.account.signTransaction(tx, private_key=private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    print(f"Transaction sent with hash: {web3.toHex(tx_hash)}")


transfer_and_call()