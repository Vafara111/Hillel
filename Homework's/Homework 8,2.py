def is_palindrome(text: str) -> bool:
    punctuation = r""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    for i in punctuation:
        text = text.replace(i, "")
    text = text.lower()
    straight = list(text)
    reverse = list(text)
    reverse.reverse()
    if straight == reverse:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")