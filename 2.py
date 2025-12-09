# a part: 
import re
s="I like apples, bananas and mangoes, grapes too"
parts=re.split(r'([, ]+)',s)
words=parts[0::2]
seps=parts[1::2]
print(words,seps) 

# b part: 
import re
t=open("input.txt").read()
nums=list(map(int,re.findall(r'\d+',t)))
print(sum(nums)) 
