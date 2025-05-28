f = open("orders.csv").read().split("\n")
for line in f:
    if line != "":
        parts = line.split(",")
        print("Order ID:", parts[0])
        print("Item:", parts[1])
        print("Qty:", parts[2])
        print("Total:", float(parts[2]) * float(parts[3]))
