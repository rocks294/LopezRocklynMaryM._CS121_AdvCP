n = int(input("Enter a number: "))

orig = n
reversed = 0


while n > 0:
    digit = n % 10
    reversed = reversed * 10 + digit
    n //= 10
if orig == reversed:
    print ("Palindrome.")
else:
    print("Not a palindrome.")    

