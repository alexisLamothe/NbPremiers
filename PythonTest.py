import time
import sys
sys.path.insert(0,"AlgoPython")
from AlgoListBool import nbPremiers

def getTimeExecution(f,n) :
    t_before = time.time()
    f(n)
    print(time.time()-t_before)

print('n = 5 : '+str(nbPremiers(5)))
print('n = 23 : '+str(nbPremiers(23)))
print('n = 100 : '+str(nbPremiers(100)))
getTimeExecution(nbPremiers,50)
getTimeExecution(nbPremiers,500)
getTimeExecution(nbPremiers,5000)
getTimeExecution(nbPremiers,50000)
#getTimeExecution(nbPremiers,500000) # Too long execution [...]


sys.path.remove("AlgoPython")
