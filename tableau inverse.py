T = []
N = int(input("entrer la demention du tableau\n"))
for i in range(0,N) :
        elt = int(input("entrer un element du tableau\n"))
        T.append(elt)
print("le tableau sait est")
print(T)
i = 0
while i < N :
    X = T[i]
    T[i] = T[N-1]
    T[N-1] = X
    i = i + 1
    N = N - 1
print(T)
