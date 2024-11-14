from zarban.wallet.openapi_client.configuration import Configuration
from zarban.wallet.openapi_client.api_client import ApiClient
from zarban.wallet.openapi_client.api.default_api import DefaultApi
from zarban.wallet.openapi_client.models.login_request import LoginRequest
from zarban.wallet.openapi_client.models.create_child_user_request import CreateChildUserRequest 
from zarban.wallet.openapi_client.exceptions import ApiException
from pprint import pprint

def child_creation_example():
    # Initialize API client
    configuration = Configuration(host="https://testwapi.zarban.io")
    api_client = ApiClient(configuration)
    api = DefaultApi(api_client)

    # Constant superuser email and password
    SUPERUSER_EMAIL = "user@example.com"
    SUPERUSER_PASSWORD = "yoursecurepassword"

    try:
        # Superuser login
        login_request = LoginRequest(
            email=SUPERUSER_EMAIL,
            password=SUPERUSER_PASSWORD
        )
        login_response = api.auth_login_post(login_request)
        pprint(f"Superuser login successful")

        # Set the access token for subsequent requests
        configuration.access_token = login_response.token

        # Create a child user
        child_username = f"child_user_test"
        child_request = CreateChildUserRequest(
            username=child_username
        )
        
        child_response = api.users_children_post(child_request)
        pprint(f"Child user created. Username: {child_response.username}")

        # Get child user's profile
        # Set the X-Child-User header in the api_client's default headers
        api_client.default_headers['X-Child-User'] = child_response.username

        # Make the profile request
        profile_response = api.profile_get(_request_timeout=30)
        
        pprint("Child user profile:")
        pprint(profile_response)

        # Remove the X-Child-User header after use
        api_client.default_headers.pop('X-Child-User', None)

    except ApiException as e:
        pprint(f"API Exception: {e}")
        pprint(f"Status code: {e.status}")
        pprint(f"Reason: {e.reason}")
        pprint(f"Error message: {e.body}")

if __name__ == "__main__":
    child_creation_example()