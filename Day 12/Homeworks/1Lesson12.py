correct_password = "luka"

while True:
    password = input("Enter the password: ")

    if password == correct_password:
        print("acceess granted")
        break
    else:
        print("access denied. Try again.")