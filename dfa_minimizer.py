def minimize_dfa(n, alphabet, finals, delta):
    # Step 1: initialize table of pairs
    marked = [[False] * n for _ in range(n)]

    # Step 2: mark pairs (p,q) if one is final and the other is not
    for p in range(n):
        for q in range(p + 1, n):
            if (p in finals) != (q in finals):
                marked[p][q] = True

    # Step 3: repeat until no more changes
    changed = True
    while changed:
        changed = False
        for p in range(n):
            for q in range(p + 1, n):
                if not marked[p][q]:
                    for sym in range(len(alphabet)):
                        p_next = delta[p][sym]
                        q_next = delta[q][sym]
                        x, y = sorted((p_next, q_next))
                        if marked[x][y]:
                            marked[p][q] = True
                            changed = True
                            break

    # Step 4: collect equivalent pairs
    result = []
    for p in range(n):
        for q in range(p + 1, n):
            if not marked[p][q]:
                result.append(f"({p},{q})")
    return result


def main():
    # 👇 Aquí leemos directamente el archivo input.txt
    with open("input.txt", "r") as f:
        input_data = f.read().strip().splitlines()

    idx = 0
    cases = int(input_data[idx]); idx += 1

    for _ in range(cases):
        n = int(input_data[idx]); idx += 1
        alphabet = input_data[idx].split(); idx += 1
        finals = set(map(int, input_data[idx].split())) if input_data[idx].strip() else set()
        idx += 1

        delta = []
        for _ in range(n):
            row = list(map(int, input_data[idx].split()))
            delta.append(row)
            idx += 1

        pairs = minimize_dfa(n, alphabet, finals, delta)
        print(" ".join(pairs))


if __name__ == "__main__":
    main()
