import re

# Regex patterns
aadhaar_pattern = r'^[0-9]{12}$'
pan_pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
usn_pattern = r'^[0-9][A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{3}$'

# Test values
aadhaar = "458912367890"
pan = "ABCDE1234F"
usn = "1MS22AD001"

# Aadhaar validation
if re.fullmatch(aadhaar_pattern, aadhaar):
    print("Aadhaar Valid")
else:
    print("Aadhaar Invalid")

# PAN validation
if re.fullmatch(pan_pattern, pan):
    print("PAN Valid")
else:
    print("PAN Invalid")

# USN validation
if re.fullmatch(usn_pattern, usn):
    print("USN Valid")
else:
    print("USN Invalid")
