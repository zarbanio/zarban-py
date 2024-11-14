from zarban.wallet.openapi_client.configuration import Configuration
from zarban.wallet.openapi_client.api_client import ApiClient
from zarban.wallet.openapi_client.api.default_api import DefaultApi
from zarban.wallet.openapi_client.models import LoginRequest
from zarban.wallet.openapi_client.exceptions import ApiException

import logging

def login_example():
    # Set up logging
    logger = logging.getLogger(__name__)

    # Create and configure the Configuration object
    configuration = Configuration(
        host="https://testwapi.zarban.io" # Use the working API URL
    )

    # Create an instance of the ApiClient with the configuration
    api_client = ApiClient(configuration)
    
    # Create an instance of the DefaultApi using the ApiClient
    api_instance = DefaultApi(api_client)

    # Prepare the login request data
    login_request = LoginRequest(
        email="user@example.com",
        password="your_secure_password"
    )

    try:
        # Call the login API
        api_response = api_instance.auth_login_post(login_request)
        logger.info("Login successful!")
        logger.info(f"Token: {api_response.token}")
        
        # After successful login, you can set the access token for future authenticated requests
        configuration.access_token = api_response.token
        
        # If the response includes user information, log it
        if hasattr(api_response, 'user'):
            logger.info(f"User ID: {api_response.user.id}")
            logger.info(f"User Email: {api_response.user.email}")
        
        return api_response.token
        
    except ApiException as e:
        logger.error(f"Exception when calling DefaultApi->auth_login_post: {e}")
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