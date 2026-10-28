
# ask the user to enter numbers
numbers = input("Enter numbers(example: 5,6,7,4,3,4): ")

# remove the parentheses
numbers = numbers.replace("(", "")
numbers = numbers.replace(")", "")

# turn the numbers into a list
numbers = numbers.split(",")

# change the numbers into integers
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# save the unsorted numbers
unsorted = numbers.copy()

# start sorting the numbers
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):

        # check if the number is bigger than the next one
        if numbers[j] > numbers[j + 1]:

            # switch the numbers
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

# show the numbers in order
print("Numbers in order:")
print(tuple(numbers))

# compare the unsorted and sorted numbers
print()
print("Comparison:")
print("Unsorted:", tuple(unsorted))
print("Sorted:  ", tuple(numbers))
