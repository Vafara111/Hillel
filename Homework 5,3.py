# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

punctuation = r""" !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
name = 'i like python community!'
hashtag = name.title()
for i in punctuation:
    hashtag = hashtag.replace(i, "")
if len(hashtag) > 140:
    hashtag = hashtag[:139]
print("#" + hashtag)