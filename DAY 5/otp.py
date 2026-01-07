import time

valid_otp = "123456"
otp_time = time.time()   

entered_otp = input("Enter OTP: ")

if entered_otp == valid_otp and (time.time() - otp_time) <= 30:
    print(" OTP is valid")
else:
    print("OTP is invalid or expired")