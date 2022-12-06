import sys
from typing import List



def getPosition(line, nbConsecutiveDiffChar):
        groups = map(set, [line[i-nbConsecutiveDiffChar:i]
                           for i in range(nbConsecutiveDiffChar, len(line))])
                           
        for i, group in enumerate(groups):
            if len(group) == nbConsecutiveDiffChar:
                return i + nbConsecutiveDiffChar

        return -1


def part1(line: List[str]) -> None:
    return getPosition(line, 4)


def part2(line: List[str]) -> None:
    return getPosition(line, 14)


def solve(filename):
    with open(filename, "r") as f:
        content = f.read()

    print(part1(content))
    print(part2(content))


if __name__ == "__main__":
  solve(sys.argv[1])

