import sys

input = sys.stdin.readline

memo = {}

def repeat(x, y, z):

    if (x, y, z) in memo:

        return memo[(x, y, z)]

    if x <= 0 or y <= 0 or z <= 0:

        result = 1

    elif x > 20 or y > 20 or z > 20:

        result = repeat(20, 20, 20)

    elif x < y and y < z:

        result = repeat(x, y, z-1) + repeat(x, y-1, z-1) - repeat(x, y-1, z)

    else:

        result = (

            repeat(x-1, y, z)

            + repeat(x-1, y-1, z)

            + repeat(x-1, y, z-1)

            - repeat(x-1, y-1, z-1)

        )

    memo[(x, y, z)] = result

    return result

while True:

    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:

        break

    result = repeat(a, b, c)

    print(f"w({a}, {b}, {c}) = {result}")

