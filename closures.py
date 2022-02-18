def make_repeat_of(n):
    def repeater(string):
        assert type(string) == str, 'Solo puedes ingresar cadenas de texto'
        return string * n
    return repeater

def run():
    repeat = make_repeat_of(6)
    print(repeat('Hola'))
    print(repeat('Jeje'))
    repeat_3 = make_repeat_of(3)
    print(repeat_3('This'))

if __name__ == '__main__':
    run()