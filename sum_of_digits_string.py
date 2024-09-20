def getLucky(s, k):
    aux = ''
    for i in range(0, len(s)):
        aux += str(ord(s[i]) - 96)
    aux = int(aux)
    print(aux)
    s = aux
    for i in range(k):
        aux = s
        s = 0
        while aux:
            s += aux % 10
            aux /= 10
    return s

getLucky("abc",2)