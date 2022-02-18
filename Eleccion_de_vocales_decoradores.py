VOWELS = {
    'a': False,
    'e': False,
    'i': False,
    'o': False,
    'u': False,
}

def take_vowel(func):
    def wrapper(*args, **kwargs):
        vowel = (func(*args, **kwargs)).lower()
        if not VOWELS[vowel]:
            VOWELS[vowel] = True
        else:
            print(f"The vowel {vowel} isn't available")
        available_vowels = [key for key, value in VOWELS.items() if not value]
        print(f'Available: {available_vowels}')
        return bool(available_vowels)
    return wrapper

@take_vowel
def choose_vowel():
    return input('Choose a vowel: ')

if __name__ == '__main__':
    end_loop = True
    while end_loop:
        end_loop = choose_vowel()