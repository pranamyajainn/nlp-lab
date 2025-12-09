import matplotlib.pyplot as p
from collections import Counter
t="apple banana apple mango banana apple"
c=Counter(t.split())
w,f=zip(*c.most_common())
p.bar(w,f); p.show() 
