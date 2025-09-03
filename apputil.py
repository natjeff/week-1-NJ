#Exercise 1
import string

def palindrome(word: str) -> bool:
    # Remove spaces and punctuation
    cleaned = "".join(ch.lower() for ch in word if ch.isalnum())
    
#   Check palindrome
    return cleaned == cleaned[::-1]


# Test Cases
print(palindrome("racecar"))      # True
print(palindrome("Nurses Run"))   # True
print(palindrome("Hello"))        # False
print(palindrome("Sit on a potato pan, Otis"))  # True


# Exercise 2
def parentheses(sequence):
    count = 0
    for char in sequence:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

# Test Cases
print(parentheses("((blah)()()())"))      # True
print(parentheses("(((())blee))"))        # True
print(parentheses("(()hello((())()))"))   # True
print(parentheses("((((((())"))           # False
print(parentheses("()))"))                # False


# add code below ...
