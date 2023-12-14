str = input().lower()

# SET() хранит только уникальные значения
set = list(set(str))
values = [ x for x in set if x != " "]
s_values = sorted(values)
print(' '.join(s_values))


