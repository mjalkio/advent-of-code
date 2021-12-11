from day6part1 import get_initial_config

# Warning: massive code duplication from day6part1 #lazy


def redistribute(config):
    config = list(config)
    max_index, max_blocks = max(
        enumerate(config),
        # Was originally lambda (idx, blocks): blocks
        key=lambda config: config[1],
    )
    config[max_index] = 0
    config = [blocks + int(max_blocks / len(config)) for blocks in config]
    remaining_blocks = max_blocks % len(config)
    idx = max_index + 1
    while remaining_blocks > 0:
        config[idx % len(config)] += 1
        remaining_blocks -= 1
        idx += 1
    return tuple(config)


def loop_size(config):
    config = tuple(config)
    past_configs = set()
    while config not in past_configs:
        past_configs.add(config)
        config = redistribute(config)

    # We found the loop! Now let's measure its length
    loop_size = 0
    past_configs = set()
    while config not in past_configs:
        loop_size += 1
        past_configs.add(config)
        config = redistribute(config)
    return loop_size


if __name__ == "__main__":
    initial_config = get_initial_config()
    print(loop_size(initial_config))
