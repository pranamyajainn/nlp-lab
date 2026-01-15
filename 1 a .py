import re

# Step 1: Read text from file
with open("data.txt", "r") as file:
    text = file.read()

# Step 2: Extract using regex
emails = re.findall(r'\S+@\S+', text)
urls = re.findall(r'https?://\S+', text)
dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
names = re.findall(r'My name is ([A-Za-z ]+)', text)

# Step 3: Print results
print("Emails:", emails)
print("URLs:", urls)
print("Dates:", dates)
print("Names:", names)
