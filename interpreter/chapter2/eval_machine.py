import sys

while True:
    line = input('->')

    line = line.strip()

    if line == "quit" or line == "exit":
        break

    try:
        result = eval(line)
        if result != None:
            print(result)
    except Exception:
        print ('シンタックスエラー')
