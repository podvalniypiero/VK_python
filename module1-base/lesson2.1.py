# while data := input():
#     print("Entered:", data)

# data = input()
# while data:
#     print("Entered:", data)
#     data = input()

var_left = input()
var_right = input()
var_boolean = True
data = input()
while data:
        if int(var_left) <= int(data) <= int(var_right):
            var_boolean = True
            data = input()
        else:
            var_boolean = False
            break
            # data = input()
print(var_boolean)
