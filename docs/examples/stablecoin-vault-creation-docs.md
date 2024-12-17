# Stablecoin System Vault Creation Documentation

## Overview

This documentation covers the implementation of vault creation in the Zarban Stablecoin System. The SDK provides functionality for creating vaults, handling transactions, and managing collateral using Web3 and the Zarban API.

## Prerequisites

- Python 3.x
- Web3.py
- Zarban SDK
- Ethereum node access (RPC URL)
- Private key with sufficient funds
- Required Python packages:
  ```bash
  pip install zarban
  ```

## Core Components

### 1. Collateral Type Management

#### `get_ilks_symbol(api)`

Retrieves available collateral types from the system.

**Parameters:**

- `api (service.StableCoinSystemApi)`: The API client instance

**Returns:**

- `list`: Unique collateral type symbols

**Example:**

```python
symbols = get_ilks_symbol(stable_coin_system_api)
```

### 2. Amount Conversion

#### `to_native(api, symbol, amount)`

Converts human-readable amounts to blockchain native format.

**Parameters:**

- `api (service.StableCoinSystemApi)`: The API client instance
- `symbol (str)`: Asset symbol (e.g., "ETH", "ZAR")
- `amount (float)`: Human-readable amount

**Returns:**

- `str`: Amount in native blockchain format (wei)

**Example:**

```python
native_amount = to_native(api, "ETH", 0.01)
```

### 3. Vault Transaction Processing

#### `get_vault_tx_steps(api, ilk_name, symbol, wallet_address, collateral_amount, loan_amount)`

Retrieves transaction steps for vault creation.

**Parameters:**

- `api (service.StableCoinSystemApi)`: The API client instance
- `ilk_name (str)`: Collateral type name
- `symbol (str)`: Asset symbol
- `wallet_address (str)`: User's wallet address
- `collateral_amount (float)`: Collateral amount
- `loan_amount (float)`: Loan amount in stablecoin

**Returns:**

- `dict`: (number_of_steps, step_number, steps)

### 4. Transaction Management

#### `wait_for_transaction_receipt(w3, tx_hash, max_wait_time=120, check_interval=15)`

Waits for transaction confirmation.

**Parameters:**

- `w3`: Web3 instance
- `tx_hash`: Transaction hash
- `max_wait_time`: Maximum wait time in seconds
- `check_interval`: Check interval in seconds

**Returns:**

- Transaction receipt or None

### 5. Transaction Logging

#### `save_transaction_details(tx, tx_hash, vault_id)`

Saves transaction details to a JSON file.

**Parameters:**

- `tx`: Transaction object
- `tx_hash`: Transaction hash
- `vault_id`: Vault identifier (can be None)

## Complete Implementation Example

```python
# Configuration
HTTPS_RPC_URL = "your_ethereum_node_url"
PRIVATE_KEY = "your_private_key"
WALLET_ADDRESS = get_address_from_private_key(PRIVATE_KEY)

# Setup API client
cfg = service.Configuration(host="https://testapi.zarban.io")
api_client = service.ApiClient(cfg)
stable_coin_system_api = service.StableCoinSystemApi(api_client)

# Setup Web3
w3 = Web3(Web3.HTTPProvider(HTTPS_RPC_URL))

# Vault parameters
ILK_NAME = "ETHA"
SYMBOL = "ETH"
COLLATERAL_AMOUNT = 0.01
LOAN_AMOUNT = 1000

# Create vault
api_response = get_vault_tx_steps(
    stable_coin_system_api,
    ILK_NAME,
    SYMBOL,
    WALLET_ADDRESS,
    COLLATERAL_AMOUNT,
    LOAN_AMOUNT
)
```

## Transaction Flow

1. **Initialization**

   - Set up API client and Web3 connection
   - Configure vault parameters

2. **Transaction Steps**

   - Retrieve vault creation steps
   - Process each step sequentially
   - Handle transaction signing and submission

3. **Transaction Monitoring**

   - Wait for transaction confirmation
   - Log transaction details
   - Verify vault creation

4. **Result Verification**
   - Get transaction logs
   - Extract vault ID
   - Update transaction records

## Error Handling

```python
try:
    # Vault creation code
except service.ApiException as e:
    print(f"Response body: {beautify_json(e.body)}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Best Practices

1. **Security**

   - Never hardcode private keys
   - Use environment variables for sensitive data
   - Verify all transaction parameters before signing

2. **Transaction Management**

   - Always wait for transaction confirmations
   - Implement proper error handling
   - Log all transactions for audit purposes

3. **Gas Management**
   - Use appropriate gas limits
   - Monitor gas prices
   - Implement retry mechanisms for failed transactions

## Logging and Monitoring

The system maintains a transaction log file (`transaction_log.json`) with the following information:

- Timestamp
- Transaction details
- Transaction hash
- Vault ID (when available)

Example log entry:

```json
{
  "timestamp": "2024-03-13T10:00:00",
  "tx": {
    "from": "0x...",
    "to": "0x...",
    "value": "1000000000000000",
    "gas": 200000
  },
  "tx_hash": "0x...",
  "vault_id": "123"
}
```

## Limitations and Considerations

1. **Network Dependencies**

   - Requires stable network connection
   - Dependent on Ethereum network status
   - May be affected by network congestion

2. **Resource Requirements**

   - Sufficient ETH for gas fees
   - Adequate collateral for vault creation
   - Valid API access

3. **Transaction Timing**
   - Transaction confirmation times vary
   - Maximum wait time configurable
   - May require multiple steps

## Troubleshooting

1. **Connection Issues**

   ```python
   if not w3.is_connected():
       print(f"Failed to connect to {HTTPS_RPC_URL}")
       exit(1)
   ```

2. **Transaction Failures**

   - Check gas prices and limits
   - Verify account balance
   - Confirm network status

3. **API Errors**
   - Validate API credentials
   - Check request parameters
   - Review error responses

## Support

For additional support or bug reports, please contact the Zarban support team or refer to the API documentation.

## See Also

- [API Reference Documentation](../service/StableCoinSystemApi.md)
