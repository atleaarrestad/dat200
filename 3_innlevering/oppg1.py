
# maks iterasjon er len(word)//2 som blir O(n)
def is_palindrom_iterative(word):
    for i in range(0, len(word)//2):
        if word[i] != word[len(word) -1 -i]:
            return False
    return True

# maks iterasjon er len(word)//2 som blir O(n)
def is_palindrome_recursive(word):
    if len(word) < 2:
        return True
    if word[0] == word[-1]:
        return is_palindrome_recursive(word[1:-1])
    return False


print(is_palindrom_iterative("oppo"))

