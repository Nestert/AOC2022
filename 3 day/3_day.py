from typing import List, Tuple
import sys

def score_an_item(item: str) -> int:
  if item.islower():
    return ord(item) - ord('a') + 1
  else:
    return ord(item) - ord('A') + 27

def part1(lines: List[str]) -> int:
  def process_line(line: str) -> int:
    length = len(line)
    left_part = set(line[:length//2])
    right_part = set(line[length//2:])
    common_part = left_part.intersection(right_part)
    return sum([score_an_item(item) for item in common_part])

  return sum([process_line(line) for line in lines])

def part2(lines: List[str]) -> int:
  def string_to_set(s: str) -> set:
    return set(s)

  def process_chunk(chunk: List[str]) -> int:
    return sum([score_an_item(item) for item in set.intersection(*map(string_to_set, chunk))])

  return sum([process_chunk(lines[i:i+3]) for i in range(0, len(lines), 3)])

def solve(filename: str) -> Tuple[int, int]:
  with open(filename) as f:
    content = f.read()
  lines = content.strip().split('\n')

  print(part1(lines))
  print(part2(lines))

if __name__ == "__main__":
  solve(sys.argv[1])