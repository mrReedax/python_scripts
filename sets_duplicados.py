def remove_duplicates(my_list):
    without_duplicates = list(set(my_list))
    return without_duplicates

def run():
    my_list = 'HOOOOjhgyigiuuoLA'
    print(my_list)
    print(remove_duplicates(my_list))

if __name__ == '__main__':
    run()