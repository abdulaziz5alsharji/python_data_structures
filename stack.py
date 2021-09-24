class Stack:
    def __init__(self) -> None:
        self.__stack = []
        self.__top = -1

    def isEmpty(self) -> bool:
        return self.__top == -1

    def push(self, value) -> None:
        self.__top += 1
        self.__stack.append(value)

    def pop(self) -> None:
        if self.isEmpty():
            raise Exception("Tne Stack Is Empty")
        self.__stack.pop(self.__top)
        self.__top -= 1

    @property
    def getTop(self):
        if self.isEmpty():
            raise Exception("Tne Stack Is Empty")
        return self.__stack[self.__top]

    def display(self) -> None:
        if self.isEmpty():
            raise Exception("Tne Stack Is Empty")
        print(self.__stack)

    def clearStack(self) -> None:
        self.__stack.clear()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.display()
    print(stack.isEmpty())
