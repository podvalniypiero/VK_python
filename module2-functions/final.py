# нужны доработки, RE

def cache_deco(func):
    cache = {} # словарь
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper

def solution(func_map, func_filter, data):
    filtered = filter(func_filter, data)
    mapped = map(func_map, filtered)

    # for data in range(0, len(data), 2):
    #     yield data

    for data in mapped:

            next(mapped) # пропуск первого элемента
            yield data


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)