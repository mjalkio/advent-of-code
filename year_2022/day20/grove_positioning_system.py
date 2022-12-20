from util import read_puzzle_input


class Node:
    def __init__(self, val, next_node=None, prev_node=None):
        self.val = val
        self.next = next_node
        self.prev = prev_node


def _print_list(node, numbers):
    lst = []
    for _ in range(len(numbers)):
        lst.append(str(node.val))
        node = node.next
    print(", ".join(lst))


def grove_coordinates_sum(puzzle_input, compute_correctly=False):
    numbers = [int(num) for num in puzzle_input.strip().split("\n")]
    node_map = {}

    tail = Node(val=numbers[-1], next_node=None)
    node_map[len(numbers) - 1] = tail
    next_node = tail
    for i in reversed(range(len(numbers) - 1)):
        node = Node(val=numbers[i], next_node=next_node)
        node_map[i] = node
        next_node.prev = node
        next_node = node
    head = next_node
    head.prev = tail
    tail.next = head

    for initial_idx in range(len(numbers)):
        node = node_map[initial_idx]

        if node.val == 0:
            continue

        # Remove the node from wherever it was in the loop
        node.prev.next = node.next
        node.next.prev = node.prev

        if node.val > 0:
            swap_1 = node
            for _ in range(node.val % (len(numbers) - 1)):
                swap_1 = swap_1.next

        elif node.val < 0:
            swap_1 = node.prev
            for _ in range(abs(node.val) % (len(numbers) - 1)):
                swap_1 = swap_1.prev

        swap_2 = swap_1.next
        swap_2.prev = node
        swap_1.next = node
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
    print(f"Part 2: {grove_coordinates_sum(puzzle_input, compute_correctly=True)}")
