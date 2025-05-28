tasks = []

while True:
    cmd = input("Enter cmd:")
    if cmd == "add":
        t = input("Task:")
        tasks.append(t)
    elif cmd == "list":
        for i in range(len(tasks)):
            print(str(i+1) + ": " + tasks[i])
    elif cmd == "quit":
        break
