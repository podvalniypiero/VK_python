str = input().lower().split(' ')
# print(str)
dict = {}
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
max = max(dict, key=dict.get)
print(max, dict[max])