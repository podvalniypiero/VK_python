# start,end,step= input().split()
# print(start, end, step)
start, end, step = map(int, input().split())
for i in map(lambda x: x**2 if x%2 !=0 else -x, range(start, end, step)):
    print(i)
# result = list(map(lambda x: x**2 if x%2 !=0 else -x, range( start, end,step)))
# for i in result:
#      print(i)

