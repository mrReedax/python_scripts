def is_prime(number: int) -> bool:
    count: int = 0
    for i in range(1,number + 1):
        if number%i == 0:
            count += 1
    return count == 2

def run():
    print(is_prime(5))

if __name__ == "__main__":
    run()