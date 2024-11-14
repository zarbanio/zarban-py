'''
Note: This script interacts with real blockchain networks and APIs. Use with
caution and ensure you understand the implications of each transaction.
Security Warning: Never hardcode or commit private keys. Use secure methods
for managing sensitive information in production environments.
'''
import requests
from datetime import datetime
import time
from web3 import Web3
from zarban.service.openapi_client import StableCoinSystemApi, ApiClient, Configuration
from zarban.service.openapi_client.exceptions import ApiException
from zarban.service.openapi_client.models import StablecoinSystemRepayZarTxRequest
import json


def to_native(amount: float):
    return str(int(amount * (10 ** 18)))


def get_vault_tx_steps(
        api: StableCoinSystemApi,
        wallet_address: str,
        vault_id: int, 
        amount: float,
        ):
    if amount:
        native_amount = to_native(amount)
    request = StablecoinSystemRepayZarTxRequest(
        wallet_address,
        vault_id,
        native_amount
        )
    # Get the raw response data
    api_response = api.api_client.call_api(
        '/v2/stablecoinsystem/tx/repayzar', 'POST',
        body=api.api_client.sanitize_for_serialization(request),
        response_type=object
    )
    return api_response[0]["numberOfSteps"], api_response[0]['stepNumber'],  api_response[0]['steps']

def get_address_from_private_key(private_key):
    # Create a Web3 instance
    w3 = Web3()
    
    # Create an account object from the private key
    account = w3.eth.account.from_key(private_key)
    
    # Return the address
    return account.address

def get_logs(tx_hash):
    base_url = "https://testapi.zarban.io"  # Replace with your actual base URL
    endpoint = f"/v2/logs/{tx_hash}"
    
    response = requests.get(base_url + endpoint)
    
    if response.status_code == 200:
        logs = response.json()
        return logs
    else:
        print(f"Error: {response.status_code}")
        print(response.json())
        return None


def save_transaction_details(tx, tx_hash):
    # Create a dictionary with the transaction details
    transaction_data = {
        "timestamp": datetime.now().isoformat(),
        "tx": tx,
        "tx_hash": tx_hash,
    }

    # Read existing data from the file
    try:
        with open("repay_transaction_log.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Append new transaction data
    existing_data.append(transaction_data)

    # Write updated data back to the file
    with open("repay_transaction_log.json", "w") as file:
        json.dump(existing_data, file, indent=2)

    print(f"Transaction details saved to repay_transaction_log.json")

def wait_for_transaction_receipt(w3, tx_hash, max_wait_time=120, check_interval=15):
    """
    Wait for a transaction receipt, checking at regular intervals.
    
    :param w3: Web3 instance
    :param tx_hash: Transaction hash to wait for
    :param max_wait_time: Maximum time to wait in seconds
    :param check_interval: Time between checks in seconds
    :return: Transaction receipt if found, None otherwise
    """
    start_time = time.time()
    while time.time() - start_time < max_wait_time:
        try:
            receipt = w3.eth.get_transaction_receipt(tx_hash)
            if receipt is not None:
                return receipt
        except Exception as e:
            print(f"Error checking transaction receipt: {e}")
        
        print(f"Waiting for transaction {tx_hash} to be mined...")
        time.sleep(check_interval)
    
    print(f"Transaction not mined after {max_wait_time} seconds")
    return None

def beautify_json(json_data):
    # Parse the JSON string if it's not already a Python object
    if isinstance(json_data, str):
        parsed_data = json.loads(json_data)
    else:
        parsed_data = json_data

    # Convert the parsed data back to a string with indentation
    beautified = json.dumps(parsed_data, indent=2, sort_keys=True, ensure_ascii=False)

    return beautified

if __name__ == '__main__':
    # Configuration
    HTTPS_RPC_URL   = "Replace with your Ethereum node URL"
    PRIVATE_KEY     = "Replace with your Private key"
    WALLET_ADDRESS  =  get_address_from_private_key(PRIVATE_KEY)

    # Define vault repayment parameters
    VAULT_ID: int        = "Replace with your vault id"
    AMOUNT: float | int  = "Replace with your actual repayment value"

    # Setup Zarban API client
    configuration           = Configuration(host="https://testapi.zarban.io")
    api_client              = ApiClient(configuration)
    stable_coin_system_api  = StableCoinSystemApi(api_client)
    # Setup Web3 connection
    w3 = Web3(Web3.HTTPProvider(HTTPS_RPC_URL, request_kwargs={'timeout': 30}))
    
    # Verify connection
    if not w3.is_connected():
        print(f"Failed to connect to {HTTPS_RPC_URL}")
        exit(1)

    account  = w3.eth.account.from_key(PRIVATE_KEY)
    chain_id = w3.eth.chain_id

    try:
        num_of_steps, step_number, steps = get_vault_tx_steps(
                stable_coin_system_api,
                WALLET_ADDRESS,
                VAULT_ID,
                AMOUNT
            )

        if steps:
            for s in range((num_of_steps - step_number) + 1):
                numberOf, step_number, steps = get_vault_tx_steps(
                    stable_coin_system_api,
                    WALLET_ADDRESS,
                    VAULT_ID,
                    AMOUNT
                )
                for number, step in enumerate(steps):
                    data  = step["data"]
                    label = data["label"]['en-US']
                    print(f'steps {number + 1}: {label}')
                    if (step_number - 1) == number:
                        print("processing...")
                        method_params   = data["methodParameters"]
                        address_to      = method_params["to"]
                        calldata        = method_params["calldata"]
                        value           = method_params["value"]
                        nonce           = w3.eth.get_transaction_count(account.address)
                        gas             = data["gasUseEstimate"] 
                        # Prepare transaction
                        tx = {
                            'from':         WALLET_ADDRESS,
                            'to':           address_to,
                            'value':        int(value),
                            'gas':          gas,
                            'gasPrice':     w3.eth.gas_price,
                            'nonce':        nonce,
                            'chainId':      chain_id,
                            'data':         calldata
                        }
                        # Sign and send transaction
                        signed_txn = account.sign_transaction(tx)
                        send  = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
                        tx_hash = send.hex()
                        # Save transaction details after each transaction
                        save_transaction_details(tx, tx_hash)  
                        # Wait for the transaction to be mined
                        receipt = wait_for_transaction_receipt(w3, tx_hash)
                        if receipt is None:
                            print(f"Transaction {tx_hash} was not mined within the timeout period.")
                            continue  # Skip to the next step if this transaction wasn't mined

                        print(f"Transaction {tx_hash} was mined in block {receipt['blockNumber']}")
        else:
          print("\nNo steps found in the response.")

    except ApiException as e:
        print(f"Response body: {beautify_json(e.body)}")
    except Exception as e:
        print(f"Unexpected error: {e}")