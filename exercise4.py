word  = input('Plese enter a word ')

def num_letters(word):
    if len(word) <  8:
        return False
    if len(word) >=  8:
        return True

print(num_letters(word))