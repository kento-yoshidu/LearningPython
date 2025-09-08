import sys

args = sys.argv
for s in args[1:]:
    if s == '-V' or s == 'version':
        print("example1")
        sys.exit()

while True:
    line = input('->')

    line = line.strip()
    if line == "quit" or line == "exit":
        break

    print(line)
