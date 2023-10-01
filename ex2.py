n = 2 ** int(input("Введите количество итераций треугольника Серпинского : "))
fS = ["*"]
print(''.join(fS))
for i in range(n - 1):
    f = ["1"]
    if len(fS) >= 2:
        c = 0
        while c + 1 < len(fS):
            f.append(str(int(fS[c]) + int(fS[c + 1])))
            c += 1
    f.append("1")
    fS.clear()
    for p in range(len(f)):
        fS.append(f[p])
    for l in range(len(f)):
        if int(f[l]) % 2 != 0:
            f[l] = "*"
        else:
            f[l] = " "
    print(''.join(f))
