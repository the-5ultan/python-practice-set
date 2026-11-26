def evenOrOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("Welcome to the Even or Odd Checker!")
while True:
    num = int(input("Enter a number (or 0 to quit): "))
    if num == 0:
        break
    print(f"The number {num} is {evenOrOdd(num)}.")