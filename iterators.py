import time

class Fiboiter():
    def __init__(self, max: int = 0):
        self.max        = max
        self.n1         = 0
        self.n2         = 1
        self.counter    = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == 0:
            aux = self.n1
        elif self.counter == 1:
            aux = self.n2
        else:
            aux = self.n1 + self.n2
            if aux < self.max or self.max == 0:
                self.n1, self.n2 = self.n2, aux
                aux = self.n2
            else:
                raise StopIteration
        self.counter += 1
        return aux

if __name__ == '__main__':
    fibonacci = Fiboiter(60)
    for element in fibonacci:
        print(element)
        time.sleep(0.05)