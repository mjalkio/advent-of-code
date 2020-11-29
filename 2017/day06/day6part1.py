import os.path as op


def get_initial_config():
    with open(op.join(op.dirname(__file__), 'puzzle_input.txt'), 'r') as f:
        puzzle_input = f.read()
    return [int(blocks) for blocks in puzzle_input.split()]


def num_cycles(config):
    config = tuple(config)
    past_configs = set()
    num_cycles = 0
    while config not in past_configs:
        past_configs.add(config)
        num_cycles += 1

        config = list(config)
        max_index, max_blocks = max(enumerate(config),
                                    key=lambda (idx, blocks): blocks)
        config[max_index] = 0
        config = [blocks + max_blocks / len(config) for blocks in config]
        remaining_blocks = max_blocks % len(config)
        idx = max_index + 1
        while remaining_blocks > 0:
            config[idx % len(config)] += 1
            remaining_blocks -= 1
            idx += 1
        config = tuple(config)
    return num_cycles

if __name__ == '__main__':
    initial_config = get_initial_config()
    print(num_cycles(initial_config))
