import re

# Step 1: Create file and write data
with open("numbers.txt", "w") as file:
    file.write("10 20 30 40 50")

# Step 2: Read file
with open("numbers.txt", "r") as file:
    text = file.read()

# Step 3: Extract numbers using regex
numbers = re.findall(r'\d+', text)

# Step 4: Convert to integers
numbers = [int(num) for num in numbers]

# Step 5: Compute sum
total = sum(numbers)

print("Numbers:", numbers)
print("Sum:", total)
