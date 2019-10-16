n = int(input())
companies = list(map(int, (input().split(" "))))


list_mikes = [1]
curr_mike = 1
for i in range(1, len(companies)):
    if companies[i] == companies[i - 1]:
        list_mikes.append(curr_mike)
    elif companies[i] != companies[i - 1] and curr_mike == 1:
        list_mikes.append(2)
        curr_mike = 2
    elif companies[i] != companies[i - 1] and curr_mike == 2:
        list_mikes.append(1)
        curr_mike = 1

try_list = list_mikes[:]

if list_mikes[-1] == list_mikes[0] and companies[-1] != companies[0]:
    if list_mikes[0] == 1:
        temp = 2
    else:
        temp = 1
    try_list[-1] = temp
    if companies[-1] == companies[-2]:
        pass
    else:
        if try_list[-1] == 1:
            temp = 2
        else:
            temp = 1
        i = -2
        while abs(i) <= len(list_mikes):
            try_list[i] = temp
            if temp == 2:
                temp = 1
            else:
                temp = 2
            if abs(i) < len(list_mikes) and companies[i] == companies[i - 1]:
                break
            i -= 1

        if abs(i) >= len(list_mikes): #!!!
            try_list[0] = 3



print(len(set(try_list)))
print(*try_list, sep=' ')