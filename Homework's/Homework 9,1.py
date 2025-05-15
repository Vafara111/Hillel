def popular_words (text: str, words: list) -> dict:
    symbols = r"""!"#$%&()*+,-./:;<=>?@[\]^_{|}~"""
    text = text.lower()
    for i in symbols:
        text = text.replace(i, " ")
    text = text.split(" ")
    result = {}
    for word in words:
        result[word] = 0
        for i in text:
            if i == word:
                result[i] += 1
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print("Ok")