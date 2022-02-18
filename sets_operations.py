def run():
    set_1 = {1,2,3,4,'a','b'}
    set_2 = {'a', 'e', 'i', 1, 3, 5}

    print(f'Union: {set_1 | set_2}')
    print(f'Interseccion: {set_1 & set_2}')
    print(f'Diferencia: set_1 - set_2 = {set_1 - set_2}')
    print(f'Diferencia: set_2 - set_1 = {set_2 - set_1}')
    print(f'Diferencia simetrica: {set_1 ^ set_2}')

    #Methods
    #set1.union(set2)
    #set1.symmetric_difference(set2)
    #set1.difference(set2)
    #set1.intersection(set2)
if __name__ == '__main__':
    run()