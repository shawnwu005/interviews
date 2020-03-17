class Stack(object):
    def __init__(self):
        self.array = [[], []]

    def l_push(self, data):
        self.array[0].append(data)

    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            self.array[0].pop()

    def r_push(self, data):
        self.array[1].append(data)

    def r_pop(self):
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            self.array[1].pop()

    def show(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            print('Stack a:', self.array[0])
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            print('Stack b:', self.array[1])
