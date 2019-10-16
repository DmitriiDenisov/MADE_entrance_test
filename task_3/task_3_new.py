# encrypted = [30, 37, 20, 25, 7, 19, 18, 0, 1, 8]
n = int(input())
encrypted = list(map(int, (input().split(" "))))
integers = list(range(1, len(encrypted) + 1))
decrypted = [-1] * len(encrypted)


def get_distance(i, dict_ans):
    sum = 0
    for key, item in dict_ans.items():
        sum += abs(i - item)
    return sum


idx = encrypted.index(min(encrypted))
decrypted[idx] = integers[-1]
dict_ans = {integers[-1]: idx}

for integer in integers[::-1][1:]:
    for i in range(len(encrypted)):
        pos = encrypted[i]
        if decrypted[i] != -1:
            continue
        if get_distance(i, dict_ans) == pos:
            decrypted[i] = integer
            dict_ans[integer] = i
            break
print(*decrypted, sep=' ')
