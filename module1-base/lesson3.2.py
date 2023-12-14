string = str(input().lower())
count = 0
for symbol in string:
    # print(symbol)
    if symbol == "#" or symbol == "@" or symbol == "!" or symbol == "%":
        count+=1
        string.replace(symbol, " ")
print(count)
print(string.replace("#", " ").replace("@", " ").replace("!", " ").replace("%", " "))
# import re
# print(re.sub(r"[#@!%.]", " ", string)) # with the help of reg exp