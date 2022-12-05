import sys

def split(lines):
    first, rest = lines.split('\n\n')

    lastline_len = len(first.splitlines()[-1].rstrip())
    stacks: list[list[str]]
    stacks = [[] for _ in range((lastline_len + 2) // 4)]


    for line in first.splitlines():
        for i, c in enumerate(line[1::4]):
            if not c.isspace():
                stacks[i].append(c)

    for stack in stacks:
        stack.reverse()
    
    return stacks, rest

def part1(lines):
    stacks, rest = split(lines)

    for instr in rest.splitlines():
        _, n_s, _, f_s, _, d_s = instr.split()
        n, f, d = int(n_s), int(f_s), int(d_s)

        for _ in range(n):
            stacks[d - 1].append(stacks[f - 1].pop())

    return ''.join(stack[-1] if stack else '' for stack in stacks)

def part2(lines):
    stacks, rest = split(lines)

    for instr in rest.splitlines():
        _, n_s, _, f_s, _, d_s = instr.split()
        n, f, d = int(n_s), int(f_s), int(d_s)

        victims = stacks[f - 1][-n:]
        del stacks[f - 1][-n:]

        stacks[d - 1].extend(victims)

    return ''.join(stack[-1] if stack else '' for stack in stacks)


def solve(filename):
    with open(filename, "r") as f:
        content = f.read()

    print(part1(content))
    print(part2(content))


if __name__ == "__main__":
  solve(sys.argv[1])

