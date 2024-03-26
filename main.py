

def find_minimum_count_of_moves(point: list[int]) -> int:
    moves_count: int = 1

    if sum(point) == 0:
        return 0

    while True:
        point = list(map(abs, point))
        max_point, min_point = max(point), min(point)

        if max_point * max_point + min_point * min_point <= 5:
            break

        if max_point - min_point < 3:
            point = [max_point - 1, min_point - 2]
        else:
            point = [max_point - 2, min_point - 1]

        moves_count += 1

    if max_point * max_point + min_point * min_point < 5:
        if max_point - min_point > 0:
            moves_count += 1
        else:
            return 2

    return moves_count


def main() -> None:
    for y in range(8):
        for x in range(8):
            distance = find_minimum_count_of_moves([x, y])
            print(distance)


if __name__ == '__main__':
    main()
