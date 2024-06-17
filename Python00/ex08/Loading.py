from typing import Generator
from time import sleep, time_ns
from tqdm import tqdm
import os


def ft_tqdm(lst: range) -> Generator[int, None, None]:
    """Adds a progress bar output while iterating on a range

    Args:
        lst (range): range to iter on

    Yields:
        Generator[int, None, None]: every values of the given range
    """

    ONE_SEC_NS = 10**9
    ONE_MIN_NS = 60 * ONE_SEC_NS
    cols = os.get_terminal_size().columns
    n = len(lst)
    start = time_ns()

    for i, elem in enumerate(lst):
        now = time_ns()

        count = f"{i + 1}/{n}"

        elapsed_ns = now - start
        mins, secs = divmod(elapsed_ns, ONE_MIN_NS)
        secs //= ONE_SEC_NS
        elapsed = f"{mins:02}:{secs:02}"

        remaining_ns = elapsed_ns * (n - i - 1) // (i + 1)
        mins, secs = divmod(remaining_ns, ONE_MIN_NS)
        secs //= ONE_SEC_NS
        remaining = f"{mins:02}:{secs:02}" if i else "?"

        secs = elapsed_ns / ONE_SEC_NS
        its = f"{i / secs:5.2f}" if i else "?"
        perfs = f"[{elapsed}<{remaining}, {its}it/s]"

        percentage = round((i + 1) * 100 / n)
        width = cols - 8 - len(count) - len(perfs)
        done = (i + 1) * width // n
        bar = '█' * done + ' ' * (width - done)

        print(f"\r{percentage:3}%|{bar}| {count} {perfs}", end='')
        yield elem


def main():
    """Compares the ft_tqdm"""

    n = 333
    mul = 1
    for elem in ft_tqdm(range(n)):
        sleep(0.005 * mul)
    print()
    for elem in tqdm(range(n)):
        sleep(0.005 * mul)
    print()


if __name__ == "__main__":
    main()
