# n = 5
# t = [4, 12, -5, 8, 14]
# t = [-20, -14, -8, -2]
n = int(input())
t = list(map(int, (input().split(" "))))
# print(t)

def func_task_1(t):
    for window in range(1, len(t)):
        for i in range(len(t) - window):
            if abs(t[i + window] - t[i]) <= 5:
                return window-1
    return -1


ans = func_task_1(t)
print(ans)
