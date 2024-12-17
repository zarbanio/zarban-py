# Loan Repayment Documentation

## Overview

This document describes how to use the Zarban SDK to repay loans. The SDK provides functionality for previewing repayments, executing repayments, and monitoring their status through a simple Python interface.

## Prerequisites

- Python 3.x
- Zarban SDK (`zarban.wallet`)
- Valid API access token
- Child user credentials (if applicable)

## Installation

```bash
pip install zarban
```

## Authentication

The SDK requires two forms of authentication:

1. An API access token
2. A child user header (optional, depending on use case)

```python
cfg = wallet.Configuration(host="https://testwapi.zarban.io")
cfg.access_token = "your_access_token_here"
api_client = wallet.ApiClient(cfg)
api_client.default_headers['X-Child-User'] = "your_child_username"
```

## Core Functions

### Repaying a Loan

#### `repay_loan(loans_api, loan_id, intent="Repay")`

Handles loan repayment operations, including preview and actual repayment.

**Parameters:**

- `loans_api`: wallet.LoansApi instance
- `loan_id`: str - Unique identifier for the loan
- `intent`: str - Either "Preview" or "Repay"

**Returns:**

- API response object containing repayment details if successful
- None if operation fails

**Example:**

```python
# Preview repayment
preview_response = repay_loan(loans_api, "loan123", intent="Preview")

# Execute repayment
repayment_response = repay_loan(loans_api, "loan123", intent="Repay")
```

### Checking Loan Status

#### `get_loan_status(loan_details, loan_id)`

Retrieves and displays detailed information about a loan.

**Parameters:**

- `loan_details`: Loan object containing loan information
- `loan_id`: str - Unique identifier for the loan

**Returns:**
Loan details object containing:

- Loan state
- User ID
- Liquidation price
- Collateral amount
- Collateralization ratio
- Loan to value
- Debt amount
- Loan plan

**Example:**

```python
loan_details = loans_api.get_loan_details(loan_id)
status = get_loan_status(loan_details, loan_id)
```

## API Endpoints

### POST /loans/repay

Previews or executes a loan repayment.

**Request Body:**

```json
{
  "intent": "Preview", // or "Repay"
  "loan_id": "loan123"
}
```

**Response (200 OK):**

```json
{
  "id": "vault123",
  "userId": 12345,
  "liquidationPrice": {
    "USD": "1500.00",
    "ETH": "0.75"
  },
  "collateral": {
    "ETH": "1.0",
    "USD": "2000.00"
  },
  "collateralizationRatio": "1.5",
  "loanToValue": "0.66",
  "debt": {
    "DAI": "1000.00",
    "USD": "1000.00"
  }
  // other fields
}
```

### GET /loans/{id}

Retrieves loan details.

**Path Parameters:**

- `id`: Loan identifier

**Response (200 OK):**
Returns loan details including state, collateral, debt, and other relevant information.

## Error Handling

The SDK uses `ApiException` for error handling. Common errors include:

- 400: Bad Request
- 401: Unauthorized
- 500: Internal Server Error

Example error handling:

```python
try:
    loans_response = loans_api.repay_loan(repay_request)
except wallet.ApiException as e:
    print(f"Exception when calling LoansApi->repay_loan: %s\n" % e)
```

## Complete Usage Example

```python
def main():
    # Setup
    ACCESS_TOKEN = "your_access_token_here"

    # Setup API client
    cfg = wallet.Configuration(host="https://testwapi.zarban.io")
    cfg.access_token = ACCESS_TOKEN
    api_client = wallet.ApiClient(cfg)
    loans_api = wallet.LoansApi(api_client)

    # Set child user header
    api_client.default_headers['X-Child-User'] = "your_child_username"

    # Preview repayment
    preview_response = repay_loan(loans_api, "loan123", intent="Preview")

    if preview_response:
        print("\nRepayment preview details:")
        print(f"Collateral to be returned: {preview_response.collateral}")
        print(f"Debt to be repaid: {preview_response.debt}")

        # Execute repayment if preview successful
        repayment_response = repay_loan(loans_api, "loan123")

        if repayment_response:
            # Monitor repayment status
            while True:
                loan_details = loans_api.get_loan_details("loan123")
                if loan_details.state.LocaleEn == "Loan settled":
                    print("\nLoan repayment successful!")
                    break
                time.sleep(10)

    # Clean up
    api_client.default_headers.pop('X-Child-User', None)
```

## Best Practices

1. Always preview repayment before executing
2. Implement proper error handling for all API calls
3. Monitor repayment status after execution
4. Remove the X-Child-User header after use
5. Store sensitive information (like access tokens) in environment variables
6. Implement proper timeout handling for status monitoring

## Limitations

- Repayment preview is recommended before actual repayment
- Status monitoring may require multiple API calls
- API access tokens should be kept secure and not hardcoded

## Support

For additional support or bug reports, please contact the Zarban support team.

## See Also

- [API Reference Documentation](../wallet)
- [Loan Creation Documentation](./loan-creation-docs.md)
