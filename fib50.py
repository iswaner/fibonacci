#Shows the first 50 numbers in the fibonacci sequence.

print("Fibonacci's sequence to the 50th value.")
fib1 = 0
fib2 = 1
print(f"1. {fib2}")

for i in range(1,50):

    next = fib1 + fib2
    fib1 = fib2
    fib2 = next
    print(f"{i+1}. {next}")