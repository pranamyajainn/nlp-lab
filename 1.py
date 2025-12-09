# part a 
import re
t=open("input.txt").read()
print("Emails:",re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[AZa-z]{2,}',t))
print("Phones:",re.findall(r'\b\d{10}\b',t))
print("IPs:",re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b',t))
print("Dates:",re.findall(r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b',t))
print("URLs:",re.findall(r'https?://\S+',t))

# part b 
n=int(input())
l=[int(input()) for _ in range(n)]
print(l.count(19)==2 and l.count(5)>=3) 
