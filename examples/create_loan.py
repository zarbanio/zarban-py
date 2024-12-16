import zarban.wallet.openapi_client as wallet


def create_loan(
        loans_api: wallet.LoansApi,
        plan_name,
        collateral,
        debt,
        symbol,
        loan_to_value_option):
    loan_request = wallet.LoanCreateRequest(
        intent="Create",
        plan_name=plan_name,
        collateral=collateral,
        debt=debt,
        symbol=symbol,
        loan_to_value_option=loan_to_value_option
    )

    try:
        api_response = loans_api.create_loan_vault(loan_request)
        print("Loan created successfully. Loan ID:", api_response.id)
        return api_response.id
    except wallet.exceptions.ApiException as e:
        print("Exception when calling loans_api->create_loan_vault: %s\n" % e)
        return None


def loan_status(loans_api: wallet.LoansApi, loan_id):
    try:
        loan_details = loans_api.get_loan_details(loan_id)
        print(f"Loan Details for ID {loan_id}:")
        print(f"User ID: ${loan_details.user_id}")
        print(f"State: {loan_details.state}")
        print(f"Collateral: {loan_details.collateral}")
        print(f"Debt: {loan_details.debt}")
        print(f"Liquidation Price: {loan_details.liquidation_price}")
        print(f"Loan To Value: {loan_details.loan_to_value}")
        return loan_details
    except wallet.exceptions.ApiException as e:
        print(f"Exception when calling loans_api->get_loan_details: %s\n" % e)
        return None


def main():
    # Replace with your actual access token
    ACCESS_TOKEN = "your_child_username"

    # Setup API client
    cfg = wallet.Configuration(host="https://testwapi.zarban.io")
    cfg.access_token = ACCESS_TOKEN
    api_client = wallet.ApiClient(cfg)
    loans_api = wallet.LoansApi(api_client)

    # Set the X-Child-User header in the api_client's default headers
    api_client.default_headers['X-Child-User'] = "your_child_username"

    # Loan creation parameters, Replace them with yout actual data
    # *** either collateral or debt must be empty ***
    PLAN_NAME = "DAIA"  # Only DAIA and DAIB supported
    COLLATERAL = "1000"  # Amount of collateral
    DEBT = ""  # Amount of debt
    SYMBOL = "DAI"  # Coin symbol
    LOAN_TO_VALUE_OPTIONS = "Safe"  # Risky - Normal - Safe

    # Create loan
    loan_id = create_loan(loans_api, PLAN_NAME, COLLATERAL, DEBT, SYMBOL, LOAN_TO_VALUE_OPTIONS)

    # Remove the X-Child-User header after use
    api_client.default_headers.pop('X-Child-User', None)

    if loan_id:
        print(f"Loan created with ID: {loan_id}")

        # Track loan status
        print("\nTracking loan status...")
        loan_details = loan_status(loans_api, loan_id)

        if loan_details:
            # You can add more specific actions based on the loan status
            print(f"Loan state: {loan_details.state}")
    else:
        print("Failed to create loan")


if __name__ == "__main__":
    main()