from typing import Iterable
from time import sleep
from tqdm import tqdm

# TODO Finir
def ft_tqdm(lst: range) -> Iterable:
    for i, elem in enumerate(lst):
        yield elem


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
