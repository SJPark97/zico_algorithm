S = input()
alph = [-1] * 26

for alphbet in range(len(S)):
    if alph[ord(S[alphbet]) - 97] != -1:
        continue
    else:
        alph[ord(S[alphbet]) - 97] = alphbet

print(*alph)
