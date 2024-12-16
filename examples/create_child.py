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

    except wallet.exceptions.ApiException as e:
        pprint(f"API Exception: {e}")
        pprint(f"Status code: {e.status}")
        pprint(f"Reason: {e.reason}")
        pprint(f"Error message: {e.body}")


if __name__ == "__main__":
    child_creation_example()