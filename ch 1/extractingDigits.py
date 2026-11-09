num = int(input("Enter a three-digit number : "))
if(num >= 100 and num <= 999):
    digit1 = num // 100
    digit2 = (num // 10) % 10
    digit3 = num % 10
    print(f"The digits are: {digit1}, {digit2}, {digit3}")
else:
    print("Please enter a valid three-digit number.")