import sys

def gameScore(hand):
  if hand == ("A", "Y"):
    return 6
  elif hand == ("A", "X"):
    return 3
  elif hand[0] == "A":
    return 0
  elif hand == ("B", "Z"):
    return 6
  elif hand == ("B", "Y"):
    return 3
  elif hand[0] == "B":
    return 0
  elif hand == ("C", "X"):
    return 6
  elif hand == ("C", "Z"):
    return 3
  elif hand[0] == "C":
    return 0
  else:
    return 0

def handScore(hand):
  if hand[1] == "X":
    return 1
  elif hand[1] == "Y":
    return 2
  elif hand[1] == "Z":
    return 3
  else:
    return 0

def pickResponse(hand):
  if hand == ("A", "X"):
    return "Z"
  elif hand == ("A", "Y"):
    return "X"
  elif hand[0] == "A":
    return "Y"
  elif hand == ("B", "X"):
    return "X"
  elif hand == ("B", "Y"):
    return "Y"
  elif hand[0] == "B":
    return "Z"
  elif hand == ("C", "X"):
    return "Y"
  elif hand == ("C", "Y"):
    return "Z"
  elif hand[0] == "C":
    return "X"
  else:
    return None

def part1(lines):
  def processHand(line):
    parts = line.replace(' ', '')
    hand = (parts[0], parts[1])
    return handScore(hand) + gameScore(hand)

  return sum(map(processHand, lines))

def part2(lines):
  def processHand(line):
    parts = line.replace(' ', '')
    l, r = parts[0], parts[1]
    newHand = (l, pickResponse((l, r)))
    return handScore(newHand) + gameScore(newHand)

  return sum(map(processHand, lines))

def solve(filename):
  with open(filename) as f:
    content = f.read()
    lines = content.splitlines()

  print(part1(lines))
  print(part2(lines))

if __name__ == "__main__":
  solve(sys.argv[1])
