def permute(trail, available, permutations):
    for x in available:
        permute(trail + [x],
                [y for y in available if y != x],
                permutations)
    if len(trail) > 0:
        permutations.append(trail)

def main():
    objects = [1, 2, 3]
    permutations = []
    permute([], objects, permutations)
    print(sorted(permutations))

main()
