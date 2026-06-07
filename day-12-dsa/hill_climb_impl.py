def hill_climb():
    x = 1

    while True:
        current = -(x - 5) ** 2 + 25

        left = -((x - 1) - 5) ** 2 + 25
        right = -((x + 1) - 5) ** 2 + 25

        if left > current:
            x = x - 1
        elif right > current:
            x = x + 1
        else:
            break

    return x


print(hill_climb())