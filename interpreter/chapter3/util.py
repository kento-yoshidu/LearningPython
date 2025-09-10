class Stack:
    def __init__(self):
        self.stack = []

    def push(self, v):
        self.stack.append(v)

    def pop(self):
        try:
            result = self.stack.pop()
        except IndexError:
            print("スタックにデータがありません。")
            return
        return result

    def pop2(self):
        try:
            result1 = self.stack.pop()
        except IndexError:
            print("スタックにデータがありません。")
            return
        try:
            result2 = self.stack.pop()
        except IndexError:
            print("スタックにデータがありません。")
            self.stack.append(result1)
            return
        return [result1, result2]

    def print(self):
        for v in self.stack:
            print(v)
