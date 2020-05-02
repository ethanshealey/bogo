import random 
import time

# Function to check if list is in order
def inOrder(numbers):
    # For each number ->
    for i in range(len(numbers)-1):
        # If next value is larger than the current ->
        if numbers[i] > numbers[i+1]:
            return False
    # If you made it here, list is in order
    return True

# Function to do the dirty work
def bogo(numbers):
    # Set the count to 0
    count = 0
    # While the list is not in order ->
    while not inOrder(numbers):
        # Increment count
        count += 1
        # Call random's shuffle function to shuffle the deck
        random.shuffle(numbers)
    # Once you escape the while loop, return the
    # count and the sorted list
    return count, numbers

# Driver
if __name__ == "__main__":
    # Create an empty array
    numbers = []
    # Populate array with 10 random numbers between 0 and 100 ->
    for i in range(10):
        numbers.append(randint(0, 100))

    # Start the timer
    start = time.time()
    # Call bogo and wait
    count, numbers = bogo(numbers)
    # Print the sorted list and the count
    print(numbers, count)
    # Print the time it took
    print('Time:', time.time()-start)
