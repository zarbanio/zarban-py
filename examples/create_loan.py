from zarban.wallet.openapi_client import DefaultApi, ApiClient, Configuration
from zarban.wallet.openapi_client.models import LoanCreateRequest
from zarban.wallet.openapi_client.exceptions import ApiException

def create_loan(
    api_instance, 
    plan_name, 
    collateral, 
    debt, 
    symbol, 
    loan_to_value_option):
    loan_request = LoanCreateRequest(
        intent="Create",
        plan_name=plan_name,
        collateral=collateral,
        debt=debt,
        symbol=symbol,
        loan_to_value_option=loan_to_value_option
    )

    try:
        api_response = api_instance.loans_create_post(loan_request)
        print("Loan created successfully. Loan ID:", api_response.id)
        return api_response.id
    except ApiException as e:
        print("Exception when calling DefaultApi->loans_create_post: %s\n" % e)
        return None


def loan_Status(api_instance, loan_id):
    try:
        loan_details = api_instance.loans_id_get(loan_id)
        print(f"Loan Details for ID {loan_id}:")
        print(f"Status: {loan_details.status}")
        print(f"Collateral: {loan_details.collateral}")
        print(f"Debt: {loan_details.debt}")
        print(f"Interest Rate: {loan_details.interest_rate}")
        print(f"Creation Date: {loan_details.created_at}")
        return loan_details
    except ApiException as e:
        print(f"Exception when calling DefaultApi->loans_id_get: %s\n" % e)
        return None

def main():
    # Replace with your actual access token
    ACCESS_TOKEN = "your_access_token_here"

    # Setup API client
    configuration = Configuration(host="https://testwapi.zarban.io")
    configuration.access_token = ACCESS_TOKEN
    api_client = ApiClient(configuration)
    api_instance = DefaultApi(api_client)

    # Set the X-Child-User header in the api_client's default headers
    api_client.default_headers['X-Child-User'] = "your_child_username"

    # Loan creation parameters, Replace them with yout actual data
    # *** either collateral or debt must be empty ***
    PLAN_NAME             = "DAIA"   # Only DAIA and DAIB supported
    COLLATERAL            = "1000"   # Amount of collateral
    DEBT                  = ""       # Amount of debt
    SYMBOL                = "USDT"   # Coin symbol
    LOAN_TO_VALUE_OPTIONS = "Safe"   # Risky - Normal - Safe

    
    # Create loan
    loan_id = create_loan(api_instance, PLAN_NAME, COLLATERAL, DEBT, SYMBOL, LOAN_TO_VALUE_OPTIONS)
    
    # Remove the X-Child-User header after use
    api_client.default_headers.pop('X-Child-User', None)


    if loan_id:
        print(f"Loan created with ID: {loan_id}")
        
        # Track loan status
        print("\nTracking loan status...")
        loan_details = loan_Status(api_instance, loan_id)
        
        if loan_details:
            # You can add more specific actions based on the loan status
            if loan_details.status == "active":
                print("Loan is active.")
            elif loan_details.status == "closed":
                print("Loan has been closed.")
            else:
                print(f"Loan status: {loan_details.status}")
    else:
        print("Failed to create loan")

if __name__ == "__main__":
    main()