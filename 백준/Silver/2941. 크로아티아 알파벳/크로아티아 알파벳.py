word = input()
croatian_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = len(word)
for check in croatian_alph:
    count -= word.count(check)

print(count)