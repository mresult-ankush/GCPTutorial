emp = open("employees.txt").read().split("\n")
for i in emp:
    if i != "":
        d = i.split(",")
        print("Name: " + d[0])
        print("Salary: " + d[1])
        print("Bonus: " + str(float(d[1]) * 0.1))
