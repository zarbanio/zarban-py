from zarban.wallet.openapi_client.configuration import Configuration
from zarban.wallet.openapi_client.api_client import ApiClient
from zarban.wallet.openapi_client.api import DefaultApi
from zarban.wallet.openapi_client.models import SignUpRequest
from zarban.wallet.openapi_client.exceptions import ApiException

def signup_example():
    # Create and configure the Configuration object
    configuration = Configuration(
        host="https://testwapi.zarban.io"
    )

    # Create an instance of the ApiClient with the configuration
    api_client = ApiClient(configuration)

    # Create an instance of the DefaultApi using the ApiClient
    api_instance = DefaultApi(api_client)

    # Prepare the signup request data
    signup_request = SignUpRequest(
        email="user@example.com",
        password="yourSecuredPassword",
    )

    try:
        # Call the signup API
        api_response = api_instance.auth_signup_post(signup_request)
        print("Confirmation link sent successful!")
        print(f"Message: {api_response.messages}")

    except ApiException as e:
        print(f"Exception when calling DefaultApi->auth_signup_post: {e}")
        print(f"Error message: {e.body}")

if __name__ == "__main__":
    signup_example()