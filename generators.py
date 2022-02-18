import time

def fibo_gen(maximum: int = 0):
    n2      = 1
    n1      = 0
    counter = 0
    while True:
        aux = n1 + n2
        if aux <= maximum or maximum == 0:
            if counter == 0:
                aux = n1
            elif counter == 1:
                aux = n2
            else:
                n1, n2 = n2, aux
                aux = n2
            counter += 1
            yield aux
        else:
            break

if __name__ == '__main__':
    fibonacci = fibo_gen()
    for element in fibonacci:
        print(element)
        time.sleep(1)
