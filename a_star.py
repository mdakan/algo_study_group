#!/usr/bin/env python3

# A* search in a square grid with randomly generated weights
# each vertex is connected to points up, down, left, and right from it

# ***Grid Loops Around Edges***
# ie, (0,0) is adjacent to (n-1,0) and (0,n-1)

from random import randint
from heapq import *


def a_star(n, start, end):
    def h(point):
        # this is the hypothesis function
        x = min((end[0]-point[0]) % n, (point[0]-end[0]) % n)
        y = min((end[1]-point[1]) % n, (point[1]-end[1]) % n)
        return x + y

    def print_arr():
        # displays the graph

        # possible emoji:
        # ←↑→↓ 👣✅❤️🐾➡️👣👆👇👈👉🌲🌱
        print()

        if end in paths:
            # print("tracing...")
            cur = end
            while cur != start:
                # print(cur)
                nxt = paths[cur]
                paths[cur] = "🐾"
                cur = ((cur[0]-nxt[0]) % n, (cur[1]-nxt[1]) % n)

        for i in range(n):
            paths[start] = "❤️"
            paths[end] = "✅"
            s = [paths[(i, j)] if (i, j) in paths else "🌱" for j in range(n)]
            s = ["👈" if x == (0, 1) else "👉" if x == (0, -1) else x for x in s]
            s = ["👆" if x == (1, 0) else "👇" if x == (-1, 0) else x for x in s]
            print(" ".join(s))

    visited = {}
    # priority queue of points to be evaluated
    fringe = [(h(start), start, None)]
    paths = {}

    while fringe:
        f_val, cur, prev = heappop(fringe)
        # print(cur)
        if cur == end:
            paths[cur] = prev
            # print("Found it!", cur)
            # print("visited:", len(visited))
            # print("leftover heap:", len(fringe))
            print_arr()
            break
        if cur not in visited:
            visited[cur] = f_val
            paths[cur] = prev
            # print_arr()
            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nxt = ((cur[0]+direction[0]) % n, (cur[1]+direction[1]) % n)
                if nxt not in visited:
                    # this random value is the actual weight of the edge
                    new_fval = f_val - h(cur) + h(nxt) + randint(1, 2)
                    heappush(fringe, (new_fval, nxt, direction))


if __name__ == "__main__":
    # n is the size of the graph
    n = randint(5, 30)
    # picking a random starting point and goal for search
    start = (randint(0, n-1), randint(0, n-1))
    end = (randint(0, n-1), randint(0, n-1))
    print("%dx%d grid displaying path from %s to %s (❤️ to ✅ )." %
          (n, n, start, end))
    a_star(n, start, end)
