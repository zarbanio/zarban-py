# zarban.wallet.openapi_client.BalanceApi

All URIs are relative to *https://wapi.zarban.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_by_symbol**](BalanceApi.md#get_balance_by_symbol) | **GET** /balance/{symbol} | Get balance
[**get_wallet_balance**](BalanceApi.md#get_wallet_balance) | **GET** /balance | Get wallet balance


# **get_balance_by_symbol**
> Balance get_balance_by_symbol(symbol)

Get balance

Get the balance by a symbol.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://wapi.zarban.io
# See configuration.py for a list of all supported configuration parameters.
configuration = zarban.wallet.openapi_client.Configuration(
    host = "https://wapi.zarban.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = zarban.wallet.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with zarban.wallet.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarban.wallet.openapi_client.BalanceApi(api_client)
    symbol = zarban.wallet.openapi_client.Symbol() # Symbol | Coin symbol

    try:
        # Get balance
        api_response = api_instance.get_balance_by_symbol(symbol)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BalanceApi->get_balance_by_symbol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **symbol** | [**Symbol**](.md)| Coin symbol | 

### Return type

[**Balance**](Balance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_balance**
> WalletBalance get_wallet_balance()

Get wallet balance

Get the balance of the wallet.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import zarban.wallet.openapi_client
from zarban.wallet.openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://wapi.zarban.io
# See configuration.py for a list of all supported configuration parameters.
configuration = zarban.wallet.openapi_client.Configuration(
    host = "https://wapi.zarban.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = zarban.wallet.openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with zarban.wallet.openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = zarban.wallet.openapi_client.BalanceApi(api_client)
    
    try:
        # Get wallet balance
        api_response = api_instance.get_wallet_balance()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BalanceApi->get_wallet_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WalletBalance**](WalletBalance.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

