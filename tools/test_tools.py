# from tools.banking_tools import get_transaction


# result = get_transaction.invoke(
#     {
#         "transaction_id": "TX1001"
#     }
# )

# print("Result:")
# print(result)

# from tools.banking_tools import get_customer


# result = get_customer.invoke(
#     {
#         "customer_id": "C1001"
#     }
# )

# print("Customer Result:")
# print(result)   


# from tools.banking_tools import get_account


# result = get_account.invoke(
#     {
#         "account_id": "A1001"
#     }
# )

# print("Account Result:")
# print(result)

# from tools.banking_tools import get_fraud_alert


# result = get_fraud_alert.invoke(
#     {
#         "transaction_id": "TX1001"
#     }
# )

# print("Fraud Alert Result:")
# print(result)

from tools.banking_tools import get_investigation


result = get_investigation.invoke(
    {
        "transaction_id": "TX1001"
    }
)

print("Investigation Result:")
print(result)