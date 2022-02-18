def make_division_by(n):
    def divide(x):
        return x / n
    return divide


def run():
    division_3 = make_division_by(3)
    division_5 = make_division_by(5)

    print(division_3(18))
    print(division_5(100))


if __name__ == '__main__':
    run()