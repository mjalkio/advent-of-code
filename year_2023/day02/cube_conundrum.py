from util import read_puzzle_input


def _is_possible(subset, bag):
    cube_counts = subset.split(", ")
    for count in cube_counts:
        num_cubes, cube_color = count.split(" ")
        num_cubes = int(num_cubes)
        if bag[cube_color] < num_cubes:
            return False

    return True


def sum_possible_games(puzzle_input, bag={"red": 12, "green": 13, "blue": 14}):
    answer = 0
    games = puzzle_input.split("\n")
    for game in games:
        game_part, subset_part = game.split(": ")
        game_id = int(game_part[5:])
        subsets = subset_part.split("; ")
        if all(_is_possible(subset, bag) for subset in subsets):
            answer += game_id

    return answer


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_possible_games(puzzle_input)}")
    print(f"Part 2: {sum_possible_games(puzzle_input)}")
