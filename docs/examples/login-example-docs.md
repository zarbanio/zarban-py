# User Login Example

This example demonstrates how to implement user authentication using the Zarban SDK. It shows how to log in a user, handle the authentication token, and set up proper logging for the authentication process.

## Prerequisites

Before running this example, ensure you have:

1. Installed the Zarban SDK:

```bash
pip install zarban
```

2. Set up Python logging (optional but recommended):

```bash
pip install logging
```

3. Access to the Zarban API (test environment)

## API Specification

### Endpoint: `/auth/login`

- **Method**: POST
- **Description**: Login with email and password and get a JWT token.

### Request Format

```json
{
  "email": "example@domain.com",
  "password": "password"
}
```

#### Required Fields

| Field    | Type   | Description     | Example            |
| -------- | ------ | --------------- | ------------------ |
| email    | string | User's email    | example@domain.com |
| password | string | User's password | password           |

### Response Format

#### Success Response (200 OK)

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR..."
}
```

#### Error Responses

- **400 Bad Request**

```json
{
  "msg": "Bad request",
  "reasons": ["Invalid address"]
}
```

- **401 Unauthorized**

```json
{
  "msg": "Unauthorized",
  "reasons": ["Invalid credentials"]
}
```

- **404 Not Found**

```json
{
  "msg": "Not Found",
  "reasons": ["User not found"]
}
```

- **500 Internal Server Error**

```json
{
  "msg": "Internal Server Error",
  "reasons": ["Server error occurred"]
}
```

## Code Example

```python
import zarban.wallet.openapi_client as wallet

import logging

def login_example():
    # Set up logging
    logger = logging.getLogger(__name__)

    # Create and configure the Configuration object
    cfg = wallet.Configuration(
        host="https://testwapi.zarban.io"  # Use the working API URL
    )

    # Create an instance of the ApiClient with the configuration
    api_client = wallet.ApiClient(cfg)

    # Create an instance of the DefaultApi using the ApiClient
    auth_api = wallet.AuthApi(api_client)

    # Prepare the login request data
    login_request = wallet.LoginRequest(
        email="user@example.com",
        password="your_secured_password"
    )

    try:
        # Call the login API
        api_response = auth_api.login_with_email_and_password(login_request)
        logger.info("Login successful!")
        logger.info(f"Token: {api_response.token}")

        # After successful login, you can set the access token for future authenticated requests
        cfg.access_token = api_response.token

        return api_response.token

    except wallet.ApiException as e:
        logger.error(f"Exception when calling auth_api->login_with_email_and_password: {e}")
        logger.error(f"Status code: {e.status}")
        logger.error(f"Reason: {e.reason}")
        logger.error(f"Error message: {e.body}")
        return None

if __name__ == "__main__":
    token = login_example()
    if token:
        print(f"Login successful. Token: {token}")
    else:
        print("Login failed. Please check the logs for more information.")
```

## Step-by-Step Explanation

1. **Set Up Logging**

   ```python
   logger = logging.getLogger(__name__)
   ```

   Initializes a logger instance for tracking authentication events and errors.

2. **Configure API Client**

   ```python
    cfg = wallet.Configuration(
        host="https://testwapi.zarban.io"
    )

    # Create an instance of the ApiClient with the configuration
    api_client = wallet.ApiClient(cfg)
   ```

   Creates and configures the API client with the test environment endpoint.

3. **Initialize API Instance**

   ```python
    auth_api = wallet.AuthApi(api_client)
   ```

   Creates an instance of the AuthApi for making API calls.

4. **Prepare Login Request**

   ```python
    login_request = wallet.LoginRequest(
        email="user@example.com",
        password="your_secured_password"
    )
   ```

   Creates a login request object with user credentials.

5. **Handle Authentication**
   ```python
    api_response = auth_api.login_with_email_and_password(login_request)
    cfg.access_token = api_response.token
   ```
   Sends login request and stores the authentication token for future requests.

## Error Handling

The example includes comprehensive error handling based on the API specification:

### Error Status Codes

1. **400 Bad Request**

   - Invalid email format
   - Missing required fields
   - Password format validation failure

2. **401 Unauthorized**

   - Invalid credentials
   - Account locked
   - Too many failed attempts

3. **404 Not Found**

   - User account doesn't exist
   - Account deleted or deactivated

4. **500 Internal Server Error**
   - Database connection issues
   - Server configuration problems
   - Internal service failures

### Error Handling Example

```python
try:
    api_response = api_instance.auth_login_post(login_request)
except wallet.ApiException as e:
    if e.status == 400:
        logger.error("Bad Request: Check input parameters")
    elif e.status == 401:
        logger.error("Unauthorized: Invalid credentials")
    elif e.status == 404:
        logger.error("Not Found: User account not found")
    elif e.status == 500:
        logger.error("Server Error: Please try again later")
```

## Logging Configuration

To set up proper logging, add this configuration before running the example:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('auth.log'),
        logging.StreamHandler()
    ]
)
```

## Best Practices

1. **Credential Management**

   ```python
   # DON'T store credentials in code
   email = "user@example.com"  # Incorrect

   # DO use environment variables
   import os
   email = os.environ.get('ZARBAN_USER_EMAIL')
   ```

2. **Token Storage**

   ```python
   # DO store token securely
   def save_token(token):
       # Use your secure storage method
       pass

   # DO clear token on logout
   def logout():
       configuration.access_token = None
       # Clear stored token
   ```

3. **Security Considerations**
   - Always use HTTPS for API calls
   - Implement rate limiting
   - Monitor for suspicious login attempts
   - Store tokens securely
   - Implement token refresh mechanisms
   - Clear tokens on logout
   - Handle token expiration

## See Also

- [API Reference Documentation](../wallet)
- [Security Best Practices](security-best-practices.md)
