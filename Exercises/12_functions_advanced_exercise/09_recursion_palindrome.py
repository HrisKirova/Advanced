def palindrome(word, index=0):
    # Base case: if the index reaches or surpasses the midpoint, the word is a palindrome
    if index >= len(word) // 2:
        return f"{word} is a palindrome"
    # Check if characters at the current index and its mirror position are the same
    if word[index] != word[-(index + 1)]:
        return f"{word} is not a palindrome"
    # Recursive call with the next index
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))