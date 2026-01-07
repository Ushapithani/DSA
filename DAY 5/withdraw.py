balance = 8000
amount = 5000

if amount <= 0:
    print("Invalid amount.")
elif amount > balance:
    print("Insufficient balance.")

else:
    balance -= amount
    print("collect your cash:", amount)
    print("Remaining balance:", balance)