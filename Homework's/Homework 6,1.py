letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
pair = input("Enter letters: ")
start_index = letters.find(pair[0])
end_index = letters.find(pair[2])
if start_index > end_index:
    result = letters[start_index : end_index : -1]
    result += pair[2]
else:
    result = letters[start_index : end_index + 1]

print(result)