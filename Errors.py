a=input("type a number")
b=input("type a number")

a=int(a)
b=int(b)

try:
    print(a/b)



except ZeroDivisionError:
    print("Sorry")
except ArithmeticError:
    print("To je divne")
finally:
    print("Hotovo")

