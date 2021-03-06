import bisect
horigin,worigin,m = map(int,input().split())
dich = {}
dicw = {}
 
havew = {}
for _ in range(m):
    h,w = map(int,input().split())
    if h in dich:
        dich[h] += 1
        havew[h].append(w)
    else:
        dich[h] = 1
        havew[h] = [w]
    if w in dicw:
        dicw[w] += 1
    else:
        dicw[w] = 1
 
dichi = list(dich.items())
dichi.sort(reverse=True, key=lambda x:x[1])
dicwi = list(dicw.items())
dicwi.sort(reverse=True, key=lambda x:x[1])
 
# print(havew)
#
# print(dichi)
# print(dicwi)
 
hmax = dichi[0][1]
wmax = dicwi[0][1]
 
for hs in dichi:
    if hs[1] != hmax:
        break
    wlis = sorted(havew[hs[0]])
    for ws in dicwi:
        if ws[1] != wmax:
            break
        idx = bisect.bisect_left(wlis, ws[0])
        if idx >= len(wlis):
            print(hmax+wmax)
            exit()
        if ws[0] != wlis[idx]:
            print(hmax+wmax)
            exit()
print(hmax+wmax-1)
 
