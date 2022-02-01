def palindrome(word):
    if not word:
        print("Can't be a palindrome")
        return
    odd_count = 0
    word_dict = {}
    for char in word:
        if not char.isalpha():
            print("Can't be a palindrome")
            return
        char = char.lower()
        word_dict.setdefault(char, 0)
        word_dict[char] += 1
    for letter in word_dict:
        if word_dict[letter] % 2 != 0:
            odd_count += 1
    if odd_count > 1:
        print("Can't be a palindrome")
        return

    print("Can be a palindrome")
    return

palindrome("code") # -> no
palindrome("aab") # -> yes
palindrome("235j32 ") # -> no
palindrome("RacECar") # -> yes

