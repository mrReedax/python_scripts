def matusculas(func):
    def wrapper(text):
        return func(text.upper())
    return wrapper

@matusculas
def message(text):
    return f'{text} is my name'


def run():
    print(message('Andres'))

if __name__ == '__main__':
    run()
