import util

stack = util.Stack()

while True:
    line = input('->')

    line = line.strip()
    if line == "printstack":
        stack.print()
        continue

    if line == "quit" or input == "exit":
        break

    if line.lower() == "exit":
        print("もしかしてexit")
    if line.lower() == "quit":
        print("もしかしてquit")

    if line == "+":
        b, a = stack.pop2()
        c = a + b
        stack.push(c)
        print(c)
    elif line == "-":
        b, a = stack.pop2()
        c = a - b
        stack.push(c)
        print(c)
    elif line == "*":
        b, a = stack.pop2()
        c = a * b
        stack.push(c)
        print(c)
    elif line == "/":
        b, a = stack.pop2()
        c = a / b
        stack.push(c)
        print(c)
    else:
        try:
            v = float(line)
        except SyntaxError:
            print("シンタックスエラー")
            continue
        stack.push(v)
        print(v)