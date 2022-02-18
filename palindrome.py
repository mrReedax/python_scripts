def is_palindrome(string: str) -> bool:
    return string.replace(" ",'').lower() == string.replace(" ",'').lower()[::-1]

def run():
    print(is_palindrome(100))

if __name__ == '__main__':
    run()