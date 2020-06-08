def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome.
    
    word str
    """
    if len(word) == 0 or len(word) == 1:
        return True
    
    if first(word) == last(word):
        return is_palindrome(middle(word))

    return False


word = 'noon'

print(is_palindrome(word))
print(is_palindrome('bob'))
print(is_palindrome('Sarah'))