def login(username, password):
    if username == "admin" and password == "99":
        return "Login successful"
    else:
        return "Invalid credentials"