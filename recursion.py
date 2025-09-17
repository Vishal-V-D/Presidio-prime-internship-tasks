#Recursion

def  rev(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + rev(s[:-1])
print(rev("hello"))

def isPowerOfFour(n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 4 != 0:
            return False
        return isPowerOfFour(n//4)

#HashMap
from typing import List
from collections import defaultdict
def totalFruit(self, fruits: List[int]) -> int:
        l=0
        m=0
        d=defaultdict(int)
        for r in range(len(fruits)):
            d[fruits[r]]+=1
            while len(d)>2:
                d[fruits[l]]-=1
                
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1
            m=max(m,r-l+1)
        return m