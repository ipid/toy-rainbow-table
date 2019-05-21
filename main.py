from rainbow_backend import crack_md5_brute_force, gen_rainbow_table, rainbow_iter, rainbow_r, fmt_int_8
from typing import Set, List, Tuple
import itertools


def whats_in_rainbow(rainbow: List[Tuple]):
    in_rainbow: Set[int] = set()

    for begin, end in rainbow:
        in_rainbow.add(end)

    return in_rainbow


def main():
    print("Generating rainbow...")
    rainbow, vis = gen_rainbow_table()
    print(rainbow, '\n')
    in_rainbow = whats_in_rainbow(rainbow)

    raw_hash = input("Hash: ")
    hsh = bytes.fromhex(raw_hash)
    orig = rainbow_r(hsh)
    assert len(hsh) == 16

    for i in range(10):
        print(f'Iter {i}: hash; r(hash) == {fmt_int_8(orig)}, ', end='')

        if orig in in_rainbow:
            print("found in rainbow.")
            break
        else:
            print("not found. Continue...")
            orig = rainbow_iter(orig)


if __name__ == '__main__':
    main()

# Number for demo: 89135873
# Demo hash: 0a2763aa38b102187a43ef4d4989fd5c
