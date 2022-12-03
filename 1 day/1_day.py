from typing import List
import sys

def part1(lines: List[str]) -> int:
  m = 0
  c = 0
  for line in lines:
    line = line.rstrip()
    if line == "":
      m = max(m, c)
      c = 0
    else:
      c += int(line)
  return m

def part2(lines: List[str]) -> int:
  m = []
  c = 0
  for line in lines:
    line = line.rstrip()
    if line == "":
      m.append(c)
      c = 0
    else:
      c += int(line)
  m.sort(reverse=True)
  return sum(m[:3])

def solve(filename: str) -> None:
  with open(filename, "r") as f:
    lines = f.readlines()
    
  print(part1(lines))
  print(part2(lines))


if __name__ == "__main__":
  solve(sys.argv[1])
