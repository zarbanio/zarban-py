from zarban.wallet.openapi_client import DefaultApi, ApiClient, Configuration
from zarban.wallet.openapi_client.models import RepayLoanRequest
from zarban.wallet.openapi_client.exceptions import ApiException
import time

def repay_loan(api_instance, loan_id, intent="Repay"):
    repay_request = RepayLoanRequest(
        intent=intent,
        loan_id=loan_id
    )

    try:
        api_response = api_instance.loans_repay_post(repay_request)
        print(f"Loan repayment {intent.lower()} successful. Loan ID:", api_response.id)
        return api_response
    except ApiException as e:
        print(f"Exception when calling DefaultApi->loans_repay_post: %s\n" % e)
        return None

def get_loan_status(loan_details, loan_id):
    try:
        print(f"Loan Details for ID {loan_id}:")
        print(f"Loan State for ID {loan_details.state}:")
        print(f"User ID: {loan_details.user_id}")
        print(f"Liquidation Price: {loan_details.liquidation_price}")
        print(f"Collateral: {loan_details.collateral}")
        print(f"Collateralization Ratio: {loan_details.collateralization_ratio}")
        print(f"Loan to Value: {loan_details.loan_to_value}")
        print(f"Debt: {loan_details.debt}")
        print(f"Loan Plan: {loan_details.plan}")
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

    # Loan ID to repay, replace with actual loan ID
    LOAN_ID = "loan123"

    # Preview repayment
    print("Previewing loan repayment...")
    preview_response = repay_loan(api_instance, LOAN_ID, intent="Preview")

    if preview_response:
        print("\nRepayment preview details:")
        print(f"Collateral to be returned: {preview_response.collateral}")
        print(f"Debt to be repaid: {preview_response.debt}")

        # Ask for user confirmation
        confirm = input("\nDo you want to proceed with the repayment? (y/n): ")
        
        if confirm.lower() == 'y':
            # Proceed with actual repayment
            repayment_response = repay_loan(api_instance, LOAN_ID)
            
            if repayment_response:
                print("repayment in progress...")
                while True:
                    loan_details = api_instance.loans_id_get(LOAN_ID)
                    if loan_details.state.LocaleEn == "Loan settled":
                        print("\nLoan repayment successful!")
                        get_loan_status(loan_details, LOAN_ID)
                        break
                    elif loan_details.state.LocaleEn == "Loan settlement failed":
                        print(loan_details.state.LocaleEn)
                        break
                    time.sleep(10)
                # Get updated loan status
                print("\nUpdated loan status:")
                get_loan_status(api_instance, LOAN_ID)
        else:
            print("Repayment cancelled.")
    else:
        print("Failed to preview loan repayment")

    # Remove the X-Child-User header after use
    api_client.default_headers.pop('X-Child-User', None)

if __name__ == "__main__":
    main()