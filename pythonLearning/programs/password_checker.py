password = str(input("Enter your Password?... ")).lower()

if len(password) > 10:
    print("Strong")
elif len(password) >= 6:
    print("Medium")
elif len(password) < 6:
    print("Weak")



