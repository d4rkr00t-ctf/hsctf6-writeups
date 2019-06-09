res = []
for i in range(1, 13):
    with open("input/%d.txt" % i, "rb") as f: data = f.read()
    data = data.split("\n")[1:]
    dx, dy = 0, 0
    for d in data:
        if "east" in d: dx += 1
        if "west" in d: dx -= 1
        if "north" in d: dy += 1
        if "south" in d: dy -= 1
    res.append(chr(int(round(2 * (dx ** 2 + dy ** 2) ** 0.5) % 26) + 97))
print("".join(res))
