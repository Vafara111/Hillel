def first_word(text: str) -> str:
    """ Пошук першого слова """
    symbols = r"""!"#$%&()*+,-./:;<=>?@[\]^_{|}~"""
    for i in symbols:
        text = text.replace(i, " ")
    text = text.strip()
    text = text.split(" ")
    return text[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
