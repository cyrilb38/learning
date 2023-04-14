#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_value = None

    def Push(self, a):
        if self.max_value is None:
            self.max_value = a
            self.__stack.append(a)
        elif a > self.max_value:
            self.__stack.append(2 * a - self.max_value)
            self.max_value = a
        else:
            self.__stack.append(a)
        # print(self.__stack, self.max_value)

    def Pop(self):
        assert(len(self.__stack))
        val = self.__stack.pop()
        # print(val)
        if val > self.max_value:
            self.max_value = 2 * self.max_value - val

    def Max(self):
        assert(len(self.__stack))
        return self.max_value


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
