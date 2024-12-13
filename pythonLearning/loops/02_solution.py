# sum of even numbers
n = 20
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even = sum_even + i

print("Sum of even no: ", sum_even)