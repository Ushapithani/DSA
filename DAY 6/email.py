email = input("Enter your email: ")

while "@" not in email or "." not in email:
    print("Invalid email. Try again.")

print("Email verified:", email)