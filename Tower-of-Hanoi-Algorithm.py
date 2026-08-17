
def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def solve(n, source, auxiliary, target):
        if n == 1:
            rods[target].append(rods[source].pop())
            moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
            return

        solve(n - 1, source, target, auxiliary)

        rods[target].append(rods[source].pop())
        moves.append(f"{rods[0]} {rods[1]} {rods[2]}")

        solve(n - 1, auxiliary, source, target)

    moves.append(f"{rods[0]} {rods[1]} {rods[2]}")
    solve(n, 0, 1, 2)

    return "\n".join(moves)

