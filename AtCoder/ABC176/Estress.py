import bisect, random

for i in range(1000):
    # horigin,worigin,m = map(int,input().split())
    
    dich = {}
    dicw = {}
     
    havew = {}
    for _ in range(random.randint(1,3*(10**5))):
        # h,w = map(int,input().split())
        h,w = random.randint(1,3*(10**5)),random.randint(1,3*(10**5))
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
            if ws[0] != wlis[idx]:
                print(hmax+wmax)
    print(hmax+wmax-1)
     
