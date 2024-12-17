# Child User Creation and Management

This example demonstrates how to create and manage child users using the Zarban SDK. It includes the process of authenticating as a superuser, creating a child user, and accessing the child user's profile.

## Prerequisites

Before running this example, ensure you have:

1. Installed the Zarban SDK:

```bash
pip install zarban
```

2. Superuser credentials with appropriate permissions
3. Access to the Zarban API (test environment)

## API Specification

### Endpoint: `/users/children`

- **Method**: POST
- **Description**: Create a child user
- **Authentication**: Required (Bearer Token)

### Request Format

```json
{
  "username": "john"
}
```

#### Required Fields

| Field    | Type   | Description         | Example |
| -------- | ------ | ------------------- | ------- |
| username | string | Child user username | "john"  |

### Response Format

#### Success Response (200 OK)

```json
{
  "username": "john"
  // Additional user properties
}
```

#### Error Responses

- **400 Bad Request**

```json
{
  "msg": "Bad request",
  "reasons": ["Invalid username format"]
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

from pprint import pprint


def child_creation_example():
    # Initialize API client
    cfg = wallet.Configuration(host="https://testwapi.zarban.io")
    api_client = wallet.ApiClient(cfg)
    auth_api = wallet.AuthApi(api_client)
    user_api = wallet.UserApi(api_client)

    # Constant superuser email and password
    SUPERUSER_EMAIL = "user@example.com"
    SUPERUSER_PASSWORD = "yourSecuredPassword"

    try:
        # Superuser login
        login_request = wallet.LoginRequest(
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD
        )
        login_response = auth_api.login_with_email_and_password(login_request)
        pprint(f"Superuser login successful")

        # Set the access token for subsequent requests
        cfg.access_token = login_response.token

        # Create a child user
        child_username = f"child_user_test"
        child_request = wallet.CreateChildUserRequest(
            username=child_username
        )

        child_response =user_api.create_child_user(child_request)
        pprint(f"Child user created. Username: {child_response.username}")

        # Get child user's profile
        # Set the X-Child-User header in the api_client's default headers
        api_client.default_headers['X-Child-User'] = child_response.username

        # Make the profile request
        profile_response = user_api.get_user_profile()

        pprint("Child user profile:")
        pprint(profile_response)

        # Remove the X-Child-User header after use
        api_client.default_headers.pop('X-Child-User', None)

    except wallet.ApiException as e:
        pprint(f"API Exception: {e}")
        pprint(f"Status code: {e.status}")
        pprint(f"Reason: {e.reason}")
        pprint(f"Error message: {e.body}")


if __name__ == "__main__":
    child_creation_example()
```

## Step-by-Step Explanation

1. **Initialize API Client**

   ```python
    cfg = wallet.Configuration(host="https://testwapi.zarban.io")
    api_client = wallet.ApiClient(cfg)
    auth_api = wallet.AuthApi(api_client)
    user_api = wallet.UserApi(api_client)
   ```

   Sets up the API client with the test environment endpoint.

2. **Superuser Authentication**

   ```python
    login_request = wallet.LoginRequest(
        email=SUPERUSER_EMAIL,
        password=SUPERUSER_PASSWORD
    )

    login_response = auth_api.login_with_email_and_password(login_request)
    cfg.access_token = login_response.token
   ```

   Authenticates the superuser and stores the access token.

3. **Create Child User**

   ```python
    child_request = wallet.CreateChildUserRequest(
        username=child_username
    )

    child_response =user_api.create_child_user(child_request)
   ```

   Creates a new child user account.

4. **Access Child User Profile**

   ```python
    api_client.default_headers['X-Child-User'] = child_response.username
    profile_response = user_api.get_user_profile()
   ```

   Sets the required header and retrieves the child user's profile.

## Important Headers

| Header Name   | Description                     | Example Value    |
| ------------- | ------------------------------- | ---------------- |
| Authorization | Bearer token for authentication | Bearer eyJhbG... |
| X-Child-User  | Username of the child user      | child_user_test  |

## Error Handling

### Common Error Scenarios

1. **400 Bad Request**

   - Invalid username format
   - Username already exists
   - Missing required fields

2. **500 Internal Server Error**
   - Database connection issues
   - Internal service failures

### Error Handling Example

```python
try:
    child_response =user_api.create_child_user(child_request)
except wallet.ApiException as e:
    if e.status == 400:
        print("Invalid request: Check username format")
    elif e.status == 500:
        print("Server error: Please try again later")
```

## Best Practices

1. **Header Management**

   ```python
   # DO clean up headers after use
   api_client.default_headers.pop('X-Child-User', None)

   # DON'T leave sensitive headers in place
   # Incorrect: Not removing headers after use
   ```

2. **Username Generation**

   ```python
   # DO use safe username generation
   import uuid
   safe_username = f"child_{uuid.uuid4().hex[:8]}"

   # DON'T use predictable usernames
   # Incorrect: sequential usernames
   username = f"child_{sequential_number}"
   ```

3. **Security Considerations**
   - Implement proper authentication checks
   - Use secure random username generation
   - Clean up sensitive headers after use
   - Implement proper error handling
   - Monitor child user creation activities
   - Implement rate limiting for creation requests

## See Also

- [API Reference Documentation](../wallet)
- [Security Best Practices](security-best-practices.md)
