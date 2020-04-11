s='jayprakash mahto'
cnt={}
for c in s:
    cnt[c]=cnt.get(c,0)+1
    
print(cnt)

# import pandas as pd

import matplotlib.pyplot as plt
x,y=zip(*cnt.items())
plt.bar(x,y)
plt.show()