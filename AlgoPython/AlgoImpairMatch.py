"""
nbPremiers357(n) :
Idée :
    - Les nb premiers sont impairs sauf 2
    - Un nombre impair est soit divisible par au moins 1 entier impair soit est premier
    - Si un nombre impair > 7 n'est pas divisible par 3, 5 ou 7, il est premier
@return Liste tous les entiers premiers <= n
Définit 3 variables (mul3, mul5, mul7)
mul3 pour les multiples de 3, mul5 ...
incrementMul fonction anonyme pour incrémenter une variable multiple3/5/7
boucle for pour tous les entiers impairs jusqu'à n
    pour chaque multiples (3,5,7) incrémente de la valeur du multiple si mul < i
    si aucun des multiples = i alors i est premier
    
>>> nbPremiers357(21) :
premiers                i       mul3    mul5    mul7    premier ? (O/N)
[2,3,5,7,11]            _       12      15      14      _
[2,3,5,7,11,13]         13      15      15      14      O
[2,3,5,7,11,13]         15      15      15      21      N
[2,3,5,7,11,13,17]      17      18      20      21      O
[2,3,5,7,11,13,17,19]   19      21      20      21      O
[2,3,5,7,11,13,17,19]   21      21      25      21      N
FIN

"""
def nbPremiers357(n) :
    premiers = []
    if n > 1 :
        premiers.append(2)
    if n > 2 :
        premiers.append(3)
    if n > 4 :
        premiers.append(5)
    if n > 6 :
        premiers.append(7)
    if n > 10 :
        premiers.append(11)
        mul3 = 12
        mul5 = 15
        mul7 = 14
        incrementMul = lambda mul, currentNb, val : mul+val if mul<currentNb else mul
        for i in range(13,n+1,2) :
            mul3 = incrementMul(mul3,i,3)
            mul5 = incrementMul(mul5,i,5)
            mul7 = incrementMul(mul7,i,7)
            if not (mul3==i or mul5==i or mul7==i) :
                premiers.append(i)
    return premiers