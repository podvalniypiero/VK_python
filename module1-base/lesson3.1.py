var1 = int(input())
if var1 >= 0:
    print(f"{var1:+010}")
else:
    print(f"{var1:-010}")

#  b = 3.1415926535
var2 = float(input())
if var2 >= 0:
    print(f"{var2:#>10.2f}")
else:
    print(f"{var2:#>-10.2f}")

# c = 1127
# 0000_0100_0110_0111
var3 = (f"{int(input()) :b}")
# print(var3)
var16 = (f"{var3:0>16}")
# print(var16)

list =[]
i=0
while (i<len(var16)):
    list.append(var16[i:i+4])
    i+=4
print("_".join(list))



