
def Fmax(c, l):
    max = 0
    for i in range(l):
        if c[i] >= max:
            max = i

    temp = c[max]
    c[max] = c[l - 1]
    c[l - 1] = temp
    return max


r = []
v = [12, 20, 15, 10, 4, 5]
w = [2, 1, 4, 6, 4, 1]
c = 15
v_w = []

l = len(w)

for i in range(l):
    v_w.append(v[i] / w[i])

k = l
for i in range(l):

    max = Fmax(v_w, k)
    print(v_w)
    print(max)
    k = k-1

    if w[max] <= c:
        r.append(v[max])
        #print(w[max])
        c = c - w[max]

    elif c > 0:
        r.append(c * v_w[max])
        print(w[max])

print(r)
