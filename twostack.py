
class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = -1
        self.top2 = self.size

        # Method to push an element x to stack1

    def l_push(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top1 = self.top1 + 1
            self.arr[self.top1] = x

        else:
            print("Stack Overflow ")
            exit(1)

            # Method to push an element x to stack2

    def r_push(self, x):

        # There is at least one empty space for new element
        if self.top1 < self.top2 - 1:
            self.top2 = self.top2 - 1
            self.arr[self.top2] = x

        else:
            print("Stack Overflow ")
            exit(1)

            # Method to pop an element from first stack

    def l_pop(self):
        if self.top1 >= 0:
            x = self.arr[self.top1]
            self.top1 = self.top1 - 1
            return x
        else:
            print("Stack Underflow ")
            exit(1)

            # Method to pop an element from second stack

    def r_pop(self):
        if self.top2 < self.size:
            x = self.arr[self.top2]
            self.top2 = self.top2 + 1
            return x
        else:
            print("Stack Underflow ")
            exit()

        # Driver program to test twoStacks class


ts = twoStacks(5)
ts.l_push(5)
ts.r_push(10)
ts.r_push(15)
ts.l_push(11)
ts.r_push(7)

print("Popped element from stack1 is " + str(ts.l_pop()))
ts.r_push(40)
print("Popped element from stack2 is " + str(ts.r_pop()))