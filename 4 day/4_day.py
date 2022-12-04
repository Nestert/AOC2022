import sys

def parse_segment(segment):
    a, b = segment.split("-")
    return (int(a), int(b))

def parse_line(line):
    a, b = line.split(",")
    return (parse_segment(a), parse_segment(b))

def part1(lines):
    def process_segments(l):
        a, b = l
        al, ar = a
        bl, br = b

        if (al >= bl and ar <= br) or (bl >= al and br <= ar):
            return 1
        else:
            return 0

    return sum(
        map(
            process_segments,
            map(parse_line, lines)
        )
    )

def part2(lines):
    def process_segments(l):
        a, b = l
        al, ar = a
        bl, br = b

        if al < bl:
            return min(max(ar - bl + 1, 0), 1)
        else:
            return min(max(br - al + 1, 0), 1)

    return sum(
        map(
            process_segments,
            map(parse_line, lines)
        )
    )

def solve(filename):
    with open(filename, "r") as f:
        content = f.read()
    lines = content.split("\n")

    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
  solve(sys.argv[1])

