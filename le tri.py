T = [4,2,3,9,0,1]

permut = False
while permut==False :
    permut = True
    for i in range(0,(len(T)-1)) :
        if T[i] > T[i+1] :
            x = T[i]
            T[i] = T[i+1]
            T[i+1] = x
            permut = True

print(T)