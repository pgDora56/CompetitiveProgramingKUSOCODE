n = int(input())
for i in range(1, n + 1):
    out = ""
    if i % 2 == 0:
        out += "a"
    if i % 3 == 0:
        out += "b"
    if i % 4 == 0:
        out += "c"
    if i % 5 == 0:
        out += "d"
    if i % 6 == 0:
        out += "e"
    if out == "":
        out = str(i)
    print(out)

