n=int(input("Enter n number:"))
try:
    f=10/n
except ZeroDivisionError:
    print("Zero")
except ValueError:
    print("Zero")
else:
    print("NO Zero error")
finally:
    print("Code success")
print(10)
print(10)
print("Hello")