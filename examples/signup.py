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

    except wallet.exceptions.ApiException as e:
        print(f"Exception when calling auth_api->signup_with_email_and_password: {e}")
        print(f"Error message: {e.body}")

if __name__ == "__main__":
    signup_example()