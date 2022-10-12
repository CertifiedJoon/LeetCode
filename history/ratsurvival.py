import math

class hole:
   def __init__(self, filled=False, number):
       self.id = number
       self.filled = filled
class rat:
    def __init__(self, number,reachableHoles = [],xr ,yr):
        self.id = number
        self.reachableHoles = reachableHoles
        self.xr = xr
        self.yr = yr

n,m,s,v = input().split()
rats = []
holes = []
for i in range(n):
    xr, yr = float(input().split())
    rats.append(rat(i,,xr,yr))
    
for i in range(m):
    holes.append(hole(,i))
    xh, yh = float(input().split())
    for j in range(n):
        if (math.sqrt(abs(rats[j].xr - xh)**2 + abs(rats[j].xr - xh)**2) < s*v):
            rats[j].reachableHoles.append(i)


for i in [_ for len(rats[_].reachableHoles) == 1]:
    holes[rats[i].reachableHoles[0]].filled = True
    for j in range(n):
        if rats[i].reachableHoles[0] in rats[j].reachableHoles:
            (rats[j].reachableHoles).remove(rats[i].reachableHoles[0])
        
    
