# User Signup Example

This example demonstrates how to use the Zarban SDK to implement a user signup process. The example shows how to create a new user account by sending a signup request to the Zarban API.

## Prerequisites

Before running this example, make sure you have:

1. Installed the Zarban SDK:

```bash
pip install zarban
```

2. Access to the Zarban API (test environment)

## Code Example

```python
import zarban.wallet.openapi_client as wallet


def signup_example():
    # Create and configure the Configuration object
    cfg = wallet.Configuration(
        host="https://testwapi.zarban.io"
    )

    # Create an instance of the ApiClient with the configuration
    api_client = wallet.ApiClient(configuration=cfg)

    # Create an instance of the AuthApi using the api_client
    auth_api = wallet.AuthApi(api_client)

    # Prepare the signup request data
    signup_request = wallet.SignUpRequest(
        email="user@example.com",
        password="yourSecuredPassword",
    )

    try:
        # Call the signup API
        api_response = auth_api.signup_with_email_and_password(signup_request)
        print("Confirmation link sent successfully!")
        print(f"Message: {api_response.messages}")

    except wallet.ApiException as e:
        print(f"Exception when calling auth_api->signup_with_email_and_password: {e}")
        print(f"Error message: {e.body}")

if __name__ == "__main__":
    signup_example()
```

## Step-by-Step Explanation

1. **Import Required Modules**

   ```python
   import zarban.wallet.openapi_client as wallet
   ```

   These imports provide the necessary classes and functions to interact with the Zarban API.

2. **Configure the API Client**

   ```python
    cfg = wallet.Configuration(
        host="https://testwapi.zarban.io"
    )
    api_client = wallet.ApiClient(configuration=cfg)
   ```

   Creates a configuration object with the API endpoint and initializes the API client.

3. **Initialize the API Instance**

   ```python
    auth_api = wallet.AuthApi(api_client)
   ```

   Creates an instance of the AuthApi class using the configured client.

4. **Prepare Signup Request**

   ```python
    signup_request = wallet.SignUpRequest(
        email="user@example.com",
        password="yourSecuredPassword",
    )
   ```

   Creates a signup request object with user credentials.

5. **Make the API Call**
   ```python
    api_response = auth_api.signup_with_email_and_password(signup_request)
   ```
   Sends the signup request to the API and handles the response.

## Response Handling

The example includes error handling using try/except blocks:

- On success: Prints a confirmation message and the response messages
- On failure: Catches `ApiException` and prints the error details

## Expected Output

On successful signup:

```
Confirmation link sent successful!
Message: [Confirmation email details...]
```

On error:

```
Exception when calling DefaultApi->auth_signup_post: [Error details]
Error message: [Detailed error message]
```

## Important Notes

1. Replace `"user@example.com"` and `"yourSecuredPassword"` with actual user credentials
2. The example uses the test API endpoint (`testwapi.zarban.io`). For production use, update the host accordingly
3. Ensure proper password security practices when implementing in production
4. The API will send a confirmation email to the provided email address

## Error Handling

Common errors that might occur:

- Invalid email format
- Password doesn't meet security requirements
- Email already registered
- Network connectivity issues
- API server errors

## See Also

- [API Reference Documentation](../src/zarban/wallet/docs/DefaultApi.md)
- [Security Best Practices](security-best-practices.md)
