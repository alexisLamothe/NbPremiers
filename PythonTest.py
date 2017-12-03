import time
from AlgoImpairMatch import nbPremiers357

def getTimeExecution(f,n) :
    t_before = time.time()
    f(n)
    print(time.time()-t_before)

print('n = 5 : '+str(nbPremiers357(5)))
print('n = 23 : '+str(nbPremiers357(23)))
print('n = 100 : '+str(nbPremiers357(100)))
getTimeExecution(nbPremiers357,50)
getTimeExecution(nbPremiers357,500)
getTimeExecution(nbPremiers357,5000)
getTimeExecution(nbPremiers357,50000)
getTimeExecution(nbPremiers357,500000)
getTimeExecution(nbPremiers357,5000000)
