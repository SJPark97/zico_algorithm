S = input()
alph = [-1] * 26

for number in range(len(S)):
    if alph[ord(S[number]) - 97] != -1:
        continue
    else:
        alph[ord(S[number]) - 97] = number

print(*alph)

# str_inp = input()
# for i in range(26):
#     print(str_inp.find(chr(i + 97)), end=' ')
