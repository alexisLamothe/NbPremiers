"""
nbPremiers(n)
@return Liste tous les entiers premiers <= n
Boucle pour "i" tous les nombres de 2 à n
Si parmis les nombres premiers trouvés il n'existe pas de multiple possible avec "i",
"i" est premier et on l'ajoute à la liste "premiers"

>>> nbPremiers357(12) :
premiers                i       ListBool                            premier (O/N)
[]                      2       []                                  O
[2]                     3       [False]                             O
[2, 3]                  4       [True, False]                       N
[2, 3]                  5       [False, False]                      O
[2, 3, 5]               6       [True, True, False]                 N
[2, 3, 5]               7       [False, False, False]               O  
[2, 3, 5, 7]            8       [True, False, False, False]         N
[2, 3, 5, 7]            9       [False, True, False, False]         N
[2, 3, 5, 7]            10      [True, False, True, False]          N
[2, 3, 5, 7]            11      [False, False, False, False]        O
[2, 3, 5, 7, 11]        12      [True, True, False, False, False]   N

>
[2, 3, 5, 7, 11]
FIN

"""
def nbPremiers(n) :
    premiers = []
    if n > 1 :
        for i in range (2,n+1) :
            if True not in [i%p==0 for p in premiers] :
                premiers.append(i)
    return premiers
