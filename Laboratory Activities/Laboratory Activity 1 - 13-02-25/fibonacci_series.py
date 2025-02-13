n = int(input("Enter the number of terms: "))

first = 0
second = 1


if n <= 0:
    print("Please enter a positive integer: ")
elif n == 1:
    print("Fibonacci Series:", end =" ")
else:
    for _ in range (n):
        print (first, end =" ")
        next = first + second
        first = second
        second = next
    print()