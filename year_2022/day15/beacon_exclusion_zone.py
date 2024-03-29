from util import read_puzzle_input


def manhattan_distance(point_a, point_b):
    return sum(abs(a - b) for a, b in zip(point_a, point_b))


def num_positions_cannot_contain_beacon(puzzle_input, row_num=2_000_000):
    positions_cannot_contain_beacon = set()
    for line in puzzle_input.split("\n"):
        if line == "":
            continue
        sensor, beacon = line.split(": ")
        sensor_x = int(sensor[sensor.find("=") + 1 : sensor.find(",")])
        sensor_y = int(sensor[sensor.rfind("=") + 1 :])
        beacon_x = int(beacon[beacon.find("=") + 1 : beacon.find(",")])
        beacon_y = int(beacon[beacon.rfind("=") + 1 :])

        distance = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))

        if row_num in range(sensor_y - distance, sensor_y + distance + 1):
            for x in range(sensor_x - distance, sensor_x + distance + 1):
                if (x, row_num) != (
                    beacon_x,
                    beacon_y,
                ) and distance >= manhattan_distance(
                    (sensor_x, sensor_y), (x, row_num)
                ):
                    positions_cannot_contain_beacon.add((x, row_num))

    return len(positions_cannot_contain_beacon)


def distress_beacon_tuning_frequency(puzzle_input, max_coord=4_000_000):
    sensors = []
    for line in puzzle_input.split("\n"):
        if line == "":
            continue
        sensor, beacon = line.split(": ")
        sensor_x = int(sensor[sensor.find("=") + 1 : sensor.find(",")])
        sensor_y = int(sensor[sensor.rfind("=") + 1 :])
        beacon_x = int(beacon[beacon.find("=") + 1 : beacon.find(",")])
        beacon_y = int(beacon[beacon.rfind("=") + 1 :])

        distance = manhattan_distance((sensor_x, sensor_y), (beacon_x, beacon_y))

        sensors.append((sensor_x, sensor_y, distance))

    for x in range(max_coord):
        if x % (max_coord / 100) == 0:
            print(f"Search {x / max_coord * 100}% complete...")
        y = 0
        while y <= max_coord:
            found_distress_beacon = True
            for sensor_x, sensor_y, distance in sensors:
                if manhattan_distance((x, y), (sensor_x, sensor_y)) <= distance:
                    found_distress_beacon = False
                    x_dist = abs(x - sensor_x)
                    y_dist = abs(y - sensor_y)
                    y += distance - x_dist - y_dist + 1
                    break
            if found_distress_beacon:
                return x * 4_000_000 + y


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_positions_cannot_contain_beacon(puzzle_input)}")
    print(f"Part 2: {distress_beacon_tuning_frequency(puzzle_input)}")
