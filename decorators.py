from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'{time_elapsed.total_seconds()} seconds')
    return wrapper


@execution_time
def random_func():
    for _ in range (1, 100000000):
        pass

@execution_time
def sum(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre='Empty'):
    print(f'Hola {nombre}')

def run():
    sum(1,2)
    random_func()
    saludo('Andres')

if __name__ == "__main__":
    run()