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

    except wallet.exceptions.ApiException as e:
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