from util import *
from math import floor, ceil


def main(data):
    times, distances = data.splitlines()
    times = times.split()[1:]
    distances = distances.split()[1:]

    def winning_ways(t, d):
        high_root = (t + isqrt(t ** 2 - 4 * d)) / 2
        low_root = (t - isqrt(t ** 2 - 4 * d)) / 2
        return floor(high_root) - ceil(low_root) + 1

    yield prod(
        winning_ways(int(t), int(d)) for t, d in zip(times, distances)
    )

    time = int("".join(times))
    distance = int("".join(distances))
    yield winning_ways(time, distance)