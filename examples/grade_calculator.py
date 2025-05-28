students = ["Alice,90,80,70", "Bob,85,95,100"]
for s in students:
    d = s.split(",")
    t = int(d[1]) + int(d[2]) + int(d[3])
    a = t / 3
    print(d[0], "has avg", a)
