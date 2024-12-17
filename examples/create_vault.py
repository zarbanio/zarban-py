"""
Vault Creation Script using Web3 and Zarban API

This script demonstrates the process of creating a vault in a stablecoin system
using the Web3 library for Ethereum interactions and the Zarban API for
stablecoin-specific operations.

Key components and functionality:

1. Imports and Setup:
   - Web3 for Ethereum blockchain interactions
   - Zarban API client for stablecoin system operations
   - Custom functions for data conversion and API interactions

2. Helper Functions:
   - get_ilks_symbol: Retrieves available collateral types (ilks) from the API
   - to_native: Converts human-readable amounts to blockchain-native amounts
   - get_vault_tx_steps: Obtains transaction steps for vault creation

3. Main Execution:
   - Sets up Web3 connection and Zarban API client
   - Defines vault creation parameters (collateral type, amounts)
   - Retrieves vault creation transaction steps
   - Iterates through steps, creating and sending Ethereum transactions

Usage:
1. Replace placeholder values (RPC URL, private key, wallet address)
2. Set desired ILK_NAME, COLLATERAL_AMOUNT, and LOAN_AMOUNT
3. Run the script to create a vault with specified parameters

Note: This script interacts with real blockchain networks and APIs. Use with
caution and ensure you understand the implications of each transaction.

Security Warning: Never hardcode or commit private keys. Use secure methods
for managing sensitive information in production environments.
"""

import requests
from datetime import datetime
import time
from web3 import Web3
import json

import zarban.service.openapi_client as service


def get_ilks_symbol(api: service.StableCoinSystemApi):
    """
    Retrieve and return a list of unique collateral type symbols.

    Args:
        api (StableCoinSystemApi): The API client instance.

    Returns:
        list: A list of unique collateral type symbols.
    """
    ilks = api.get_all_ilks()
    symbols = []
    for ilk in ilks.data:
        symbols.append(ilk.symbol)
    return list(set(symbols))


def to_native(
        api: service.StableCoinSystemApi,
        symbol: str,
        amount: float
):
    """
    Convert a human-readable amount to its native blockchain representation.

    Args:
        api (StableCoinSystemApi): The API client instance.
        symbol (str): The symbol of the asset (e.g., "ETH", "ZAR").
        amount (float): The human-readable amount to convert.

    Returns:
        int: The amount in its native blockchain representation.
    """
    # 1) get symbols
    symbols = get_ilks_symbol(api)
    # 2) create ratio dict
    ratio = {
        "ZAR": 18,
    }
    for s in symbols:
        ratio[s] = 18

    return str(int(amount * (10 ** ratio[symbol])))


def get_vault_tx_steps(
        api: service.StableCoinSystemApi,
        ilk_name: str,
        symbol: str,
        wallet_address: str,
        collateral_amount: float,
        loan_amount: float
):
    """
    Retrieve the transaction steps required to create a vault.

    Args:
        api (StableCoinSystemApi): The API client instance.
        ilk_name (str): The name of the collateral type.
        wallet_address (str): The user's wallet address.
        collateral_amount (float): The amount of collateral to deposit.
        loan_amount (float): The amount of stablecoin to generate.

    Returns:
        list: A list of transaction steps to create the vault.
    """
    native_collateral_amount = to_native(api, symbol, collateral_amount)
    native_loan_amount = to_native(api, "ZAR", loan_amount)

    request = service.StablecoinSystemCreateVaultTxRequest(
        ilk_name,
        wallet_address,
        native_collateral_amount,
        native_loan_amount
    )
    # Get the raw response data
    api_response = api.create_stable_coin_vault(request)

    return api_response


def get_address_from_private_key(private_key):
    # Create a Web3 instance
    w3 = Web3()

    # Create an account object from the private key
    account = w3.eth.account.from_key(private_key)

    # Return the address
    return account.address


def get_logs(logs_api: service.LogsApi, tx_hash: str):
    response = logs_api.get_logs_by_transaction_hash(tx_hash)
    return  response.data


def get_vault_id(logs):
    vaultId = None
    if logs:
        for log in logs:
            if log.name == "NewCdp":
                vaultId = log.decoded['Cdp']
    return vaultId


def save_transaction_details(tx, tx_hash, vault_id):
    # Create a dictionary with the transaction details
    transaction_data = {
        "timestamp": datetime.now().isoformat(),
        "tx": tx,
        "tx_hash": tx_hash,
        "vault_id": vault_id
    }

    # Read existing data from the file
    try:
        with open("transaction_log.json", "r") as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Append new transaction data
    existing_data.append(transaction_data)

    # Write updated data back to the file
    with open("transaction_log.json", "w") as file:
        json.dump(existing_data, file, indent=2)

    print(f"Transaction details saved to transaction_log.json")


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

        print(f"Waiting for transaction {tx_hash.hex()} to be mined...")
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
    HTTPS_RPC_URL = "Replace with your Ethereum node URL"
    PRIVATE_KEY = "Replace with your Private key"
    WALLET_ADDRESS = get_address_from_private_key(PRIVATE_KEY)
    # Setup Zarban API client
    cfg = service.Configuration(host="https://testapi.zarban.io")
    api_client = service.ApiClient(cfg)
    stable_coin_system_api = service.StableCoinSystemApi(api_client)
    logs_api = service.LogsApi(api_client)
    # Setup Web3 connection
    w3 = Web3(Web3.HTTPProvider(HTTPS_RPC_URL, request_kwargs={'timeout': 30}))

    # Verify connection
    if not w3.is_connected():
        print(f"Failed to connect to {HTTPS_RPC_URL}")
        exit(1)

    account = w3.eth.account.from_key(PRIVATE_KEY)
    chain_id = w3.eth.chain_id

    # Define vault creation parameters
    ILK_NAME = "ETHA"  # Replace with your desired ilk
    SYMBOL = "ETH"  # Replace with the symbol associated with your ilk
    COLLATERAL_AMOUNT = .01  # Replace with your desired amount
    LOAN_AMOUNT = 1000  # Replace with your desired amount

    try:
        vault_steps = get_vault_tx_steps(
            stable_coin_system_api,
            ILK_NAME,
            SYMBOL,
            WALLET_ADDRESS,
            COLLATERAL_AMOUNT,
            LOAN_AMOUNT)
        num_of_steps = vault_steps.number_of_steps
        step_number = vault_steps.step_number
        steps =  vault_steps.steps

        if steps:
            for s in range((num_of_steps - step_number) + 1):
                vault_steps = get_vault_tx_steps(
                    stable_coin_system_api,
                    ILK_NAME,
                    SYMBOL,
                    WALLET_ADDRESS,
                    COLLATERAL_AMOUNT,
                    LOAN_AMOUNT)
                numberOf = vault_steps.number_of_steps
                step_number = vault_steps.step_number
                steps = vault_steps.steps
                for number, step in enumerate(steps):
                    data = step.data
                    label = data.label['en-US']
                    print(f'steps {number + 1}: {label}')
                    if (step_number - 1) == number:
                        print("processing...")
                        method_params = data.method_parameters
                        address_to = method_params.to
                        calldata = method_params.calldata
                        value = method_params.value
                        nonce = w3.eth.get_transaction_count(account.address)
                        gas = data.gas_use_estimate
                        # Prepare transaction
                        tx = {
                            'from': WALLET_ADDRESS,
                            'to': address_to,
                            'value': int(value),
                            'gas': gas,
                            'gasPrice': w3.eth.gas_price,
                            'nonce': nonce,
                            'chainId': chain_id,
                            'data': calldata
                        }
                        # Sign and send transaction
                        signed_txn = account.sign_transaction(tx)
                        send = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
                        tx_hash = send.hex()
                        # Save transaction details after each transaction
                        save_transaction_details(tx, tx_hash, None)  # vault_id is None at this point
                        # Wait for the transaction to be mined
                        receipt = wait_for_transaction_receipt(w3, "0x"+ tx_hash)
                        if receipt is None:
                            print(f"Transaction {tx_hash} was not mined within the timeout period.")
                            continue  # Skip to the next step if this transaction wasn't mined

                        print(f"Transaction {tx_hash} was mined in block {receipt['blockNumber']}")

                if numberOf == step_number:
                    logs = get_logs(logs_api, "0x"+ tx_hash)
                    vault_id = get_vault_id(logs)
                    if vault_id:
                        print("vault was created successfully.")
                        print(f'TX HASH: 0x{tx_hash}\nVAULT ID: {vault_id}')

                        # Update the last transaction with the vault_id
                        with open("transaction_log.json", "r") as file:
                            data = json.load(file)
                        data[-1]["vault_id"] = vault_id
                        with open("transaction_log.json", "w") as file:
                            json.dump(data, file, indent=2)

        else:
            print("\nNo steps found in the response.")

    except service.ApiException as e:
        print(f"Response body: {beautify_json(e.body)}")
    except Exception as e:
        print(f"Unexpected error: {e}")