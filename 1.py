begin = 200
end = 320
l = []
for i in range(begin, end+1):
    if i % 7 == 0:
        if i % 5 == 0:
            continue
        l.append(str(i))
print("/----/".join(l))