from typing import Iterable
from time import sleep, time_ns
from tqdm import tqdm
import os

# TODO Finir
def ft_tqdm(lst: range) -> Iterable:
    cols = os.get_terminal_size().columns
    start = time_ns()
    n = len(lst)
    for i, elem in enumerate(lst):
        count = f"{i + 1}/{n}"
        now = time_ns()
        elapsed_ns = now - start
        mins = elapsed_ns // 60_000_000_000
        secs = (elapsed_ns % 60_000_000_000) // 1_000_000_000
        elapsed = f"{mins:02}:{secs:02}"
        remaining_ns = elapsed_ns * (n - i - 1) // (i + 1)
        mins = remaining_ns // 60_000_000_000
        secs = (remaining_ns % 60_000_000_000) // 1_000_000_000
        remaining = f"{mins:02d}:{secs:02d}" if i else "?"
        it = f"{i / (elapsed_ns // 60_000_000_000):.2f}" if i else "?"
        perfs = f"[{elapsed}<{remaining}, {it}it/s]"
        percentage = (i + 1) * 100 // n
        width = cols - 8 - len(count) - len(perfs)
        done = percentage * width // 100
        bar = f"|{'█' * done}{' ' * (width - done)}|"
        print(f"\r{percentage:3}%{bar} {count} {perfs}", end='')
        yield elem


def main():
    mul = 1
    for elem in ft_tqdm(range(333)):
        sleep(0.005 * mul)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005 * mul)
    print()


if __name__ == "__main__":
    main()
