# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes
# t!e@s/#t% t%E^S&T!
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
name = input("Enter name:")

for i in punctuation:
    name = name.replace(i, "")
hashtag = name.title()
hashtag = hashtag.replace(" ","")
if len(hashtag) > 140:
    hashtag = hashtag[:139]
print("#" + hashtag)