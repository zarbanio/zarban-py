# Stablecoin System Vault Repayment Documentation

## Overview

This documentation covers the implementation of vault repayment in the Zarban Stablecoin System. The SDK provides functionality for repaying existing vaults, handling transactions, and logging repayment details using Web3 and the Zarban API.

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

### 1. Amount Conversion

#### `to_native(amount)`

Converts a human-readable amount to its native blockchain format (wei).

**Parameters:**

- `amount (float)`: The amount to be converted

**Returns:**

- `str`: The amount in native blockchain format

**Example:**

```python
native_amount = to_native(1.5)
```

### 2. Vault Repayment Transaction Processing

#### `get_vault_tx_steps(api, wallet_address, vault_id, amount)`

Retrieves transaction steps for vault repayment.

**Parameters:**

- `api (service.StableCoinSystemApi)`: The API client instance
- `wallet_address (str)`: User's wallet address
- `vault_id (int)`: The ID of the vault to be repaid
- `amount (float)`: The repayment amount

**Returns:**

- `dict`: (number_of_steps, step_number, steps)

### 3. Transaction Management

#### `wait_for_transaction_receipt(w3, tx_hash, max_wait_time=120, check_interval=15)`

Waits for transaction confirmation.

**Parameters:**

- `w3`: Web3 instance
- `tx_hash`: Transaction hash
- `max_wait_time`: Maximum wait time in seconds
- `check_interval`: Check interval in seconds

**Returns:**

- Transaction receipt or None

### 4. Transaction Logging

#### `save_transaction_details(tx, tx_hash)`

Saves transaction details to a JSON file.

**Parameters:**

- `tx`: Transaction object
- `tx_hash`: Transaction hash

## Complete Implementation Example

```python
# Configuration
HTTPS_RPC_URL = "your_ethereum_node_url"
PRIVATE_KEY = "your_private_key"
WALLET_ADDRESS = get_address_from_private_key(PRIVATE_KEY)

# Setup API client
cfg = service.Configuration(host="https://testapi.zarban.io")
api_client = ApiClient(cfg)
stable_coin_system_api = service.StableCoinSystemApi(api_client)

# Setup Web3
w3 = Web3(Web3.HTTPProvider(HTTPS_RPC_URL))

# Vault repayment parameters
VAULT_ID = 123  # Replace with your actual vault ID
REPAYMENT_AMOUNT = 500  # Replace with your actual repayment amount

# Repay vault
num_of_steps, step_number, steps = get_vault_tx_steps(
    stable_coin_system_api,
    WALLET_ADDRESS,
    VAULT_ID,
    REPAYMENT_AMOUNT
)
```

## Transaction Flow

1. **Initialization**

   - Set up API client and Web3 connection
   - Configure vault repayment parameters

2. **Transaction Steps**

   - Retrieve vault repayment steps
   - Process each step sequentially
   - Handle transaction signing and submission

3. **Transaction Monitoring**

   - Wait for transaction confirmation
   - Log transaction details

4. **Result Verification**
   - Review transaction logs for successful repayment

## Error Handling

```python
try:
    # Vault repayment code
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

The system maintains a transaction log file (`repay_transaction_log.json`) with the following information:

- Timestamp
- Transaction details
- Transaction hash

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
  "tx_hash": "0x..."
}
```

## Limitations and Considerations

1. **Network Dependencies**

   - Requires stable network connection
   - Dependent on Ethereum network status
   - May be affected by network congestion

2. **Resource Requirements**

   - Sufficient ETH for gas fees
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
