var_boolean = False
string = str(input())
for i in string:
        if i=="a" or i=="o":
            var_boolean = True
        elif i=="i" or i=="e":
            var_boolean = False
            break
print(var_boolean)
