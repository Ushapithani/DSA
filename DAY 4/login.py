user = "admin"
pass1 = "admin99"
username = input()
password = input()
if username == user and password == pass1:
    print("Login completed ")
elif username == user and password != pass1:
    print("Wrong password!")
elif username != user and password == pass1:
    print("Wrong username!")
else:
    print("Invalid details")