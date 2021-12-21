from collections import defaultdict

from util import read_puzzle_input


PIXEL_MAP = {
    ".": "0",
    "#": "1",
}
NUM_INPUT_PIXELS = 9


def _get_binary_lookup(x, y, image):
    binary_lookup = ""
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            binary_lookup += PIXEL_MAP[image[(x + dx, y + dy)]]
    return int(binary_lookup, 2)


def _print_image(image):
    min_x = min(x for (x, _) in image.keys())
    max_x = max(x for (x, _) in image.keys())
    min_y = min(y for (_, y) in image.keys())
    max_y = max(y for (_, y) in image.keys())
    for y in range(min_y, max_y + 1):
        line = []
        for x in range(min_x, max_x + 1):
            line.append(image[(x, y)])
        print("".join(line))



def get_num_lit_pixels(puzzle_input, num_enhancements=2):
    lines = puzzle_input.split("\n")
    algorithm = lines[0]
    image_lines = lines[2:]

    infinite_pixel = "."

    image = defaultdict(lambda: infinite_pixel)
    for y in range(len(image_lines)):
        for x in range(len(image_lines[y])):
            image[(x, y)] = image_lines[y][x]

    min_x = 0
    max_x = x
    min_y = 0
    max_y = y

    for _ in range(num_enhancements):
        binary_lookup = "".join(
            [PIXEL_MAP[infinite_pixel] for _ in range(NUM_INPUT_PIXELS)]
        )
        infinite_pixel = algorithm[int(binary_lookup, 2)]
        enhanced_image = defaultdict(lambda: infinite_pixel)
        min_x -= 2
        max_x += 2
        min_y -= 2
        max_y += 2
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                enhanced_image[(x, y)] = algorithm[_get_binary_lookup(x, y, image)]
        image = enhanced_image

    return len([pixel for pixel in image.values() if pixel == "#"])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_lit_pixels(puzzle_input)}")
    print(f"Part 2: {get_num_lit_pixels(puzzle_input)}")
