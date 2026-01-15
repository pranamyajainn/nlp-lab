# Step 1: Take number of elements
n = int(input("Enter number of elements: "))

# Step 2: Create list
lst = []
for i in range(n):
    num = int(input())
    lst.append(num)

# Step 3: Count occurrences
count_19 = lst.count(19)
count_5 = lst.count(5)

# Step 4: Check condition
if count_19 == 2 and count_5 >= 3:
    print(True)
else:
    print(False)
