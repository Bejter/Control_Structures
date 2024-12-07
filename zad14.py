# Bank account balance
account_balance = 500

# List of purchase amounts
purchases = [140, 499, 500, 501, 720]

# Process each purchase
for total_amount in purchases:
    print(f"Total amount of purchase: {total_amount} PLN")
    if total_amount <= account_balance:
        print("Payment approved.")
        account_balance -= total_amount  # Deduct the purchase amount from account
    else:
        print("Insufficient funds. Payment cannot be made.")
    print(f"Remaining balance: {account_balance} PLN\n")
