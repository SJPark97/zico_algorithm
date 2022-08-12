word = input()
result = word
for test in word:
    if test in 'CAMBRIDGE':
        result = result.replace(test, '')

print(result)