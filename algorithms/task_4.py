def check_route(N, route):
    x, y = 0, 0
    visited = {(x, y)}

    # Перемещения в соответствии с маршрутом
    moves = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

    for move in route:
        dx, dy = moves[move]
        x += dx
        y += dy

        if (x, y) in visited:
            return "YES"
        else:
            visited.add((x, y))

    return "NO"


# Считываем входные данные
N = int(input())
route = input().strip()

# Проверяем оптимальность маршрута
result = check_route(N, route)

# Выводим результат
print(result)
