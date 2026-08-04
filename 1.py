begin = 2000
end = 3200
l = []
for i in range(begin, end+1):
    if i % 7 == 0:
        if i % 5 == 0:
            continue
        l.append(str(i))
print(",".join(l))