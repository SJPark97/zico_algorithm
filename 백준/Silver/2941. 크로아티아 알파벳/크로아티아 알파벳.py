checking_alph = input()
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = len(checking_alph)
for alph_check in alph:
    count -= checking_alph.count(alph_check)

print(count)