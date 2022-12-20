from util import read_puzzle_input


class Node:
    def __init__(self, initial_idx, val, next_node=None, prev_node=None):
        self.initial_idx = initial_idx
        self.val = val
        self.next = next_node
        self.prev = prev_node


def _print_list(node, numbers):
    lst = []
    for _ in range(len(numbers)):
        lst.append(str(node.val))
        node = node.next
    print(", ".join(lst))


def grove_coordinates_sum(puzzle_input):
    numbers = [int(num) for num in puzzle_input.strip().split("\n")]

    tail = Node(initial_idx=len(numbers) - 1, val=numbers[-1], next_node=None)
    next_node = tail
    for i in reversed(range(len(numbers) - 1)):
        node = Node(initial_idx=i, val=numbers[i], next_node=next_node)
        next_node.prev = node
        next_node = node
    head = next_node
    head.prev = tail
    tail.next = head

    for initial_idx in range(len(numbers)):
        while node.initial_idx != initial_idx:
            node = node.next

        if node.val > 0:
            swap_1 = node
            for _ in range(node.val % len(numbers)):
                swap_1 = swap_1.next

        elif node.val < 0:
            swap_1 = node.prev
            for _ in range(abs(node.val) % len(numbers)):
                swap_1 = swap_1.prev
        elif node.val == 0:
            continue

        swap_2 = swap_1.next
        swap_2.prev = node
        swap_1.next = node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = swap_1
        node.next = swap_2

    while node.val != 0:
        node = node.next

    coordinates_sum = 0

    for _ in range(3):
        for _ in range(1000):
            node = node.next
        coordinates_sum += node.val

    return coordinates_sum


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {grove_coordinates_sum(puzzle_input)}")
    print(f"Part 2: {grove_coordinates_sum(puzzle_input)}")
