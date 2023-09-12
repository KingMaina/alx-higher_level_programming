def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result 

# Ask for input
# Loop for each number
# print fib result and increment

numFibValues = int(input("Enter number of fibonacci values to find: "))

i = 0
while i < numFibValues:
    fibValue = fib(i)
    print(fibValue)
    i += 1
print("***All done***")