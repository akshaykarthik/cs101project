class Location:
    def __init__(self, position, voice):
        self.position = position
        self.voice = voice


class Map:
    def __init__(self):
        ### Normally this would be loaded in but this is just a testing map.
        self.map = ((0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
                    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0)
        )
        self.locations = []
        self.position = (0, 0)
        self.file = ""

    def load_map(self, file):
        self.file = file

    def set_position(self, position):
        self.position = position

    def get_key_locations(self):
        return self.locations

    def astar(self, m, startp, endp):
        w, h = 12, 12
        sx, sy = startp
        ex, ey = endp
        #[parent node, x, y,g,f]
        node = [None, sx, sy, 0, abs(ex - sx) + abs(ey - sy)]
        closeList = [node]
        createdList = {}
        createdList[sy * w + sx] = node
        k = 0
        while (closeList):
            node = closeList.pop(0)
            x = node[1]
            y = node[2]
            l = node[3] + 1
            k += 1
            #find neighbours
            #make the path not too strange
            if k & 1:
                neighbours = ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y))
            else:
                neighbours = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
            for nx, ny in neighbours:
                if nx == ex and ny == ey:
                    path = [(ex, ey)]
                    while node:
                        path.append((node[1], node[2]))
                        node = node[0]
                    return list(reversed(path))
                if 0 <= nx < w and 0 <= ny < h and m[ny][nx] == 0:
                    if ny * w + nx not in createdList:
                        nn = (node, nx, ny, l, l + abs(nx - ex) + abs(ny - ey))
                        createdList[ny * w + nx] = nn
                        #adding to closelist ,using binary heap
                        nni = len(closeList)
                        closeList.append(nn)
                        while nni:
                            i = (nni - 1) >> 1
                            if closeList[i][4] > nn[4]:
                                closeList[i], closeList[nni] = nn, closeList[i]
                                nni = i
                            else:
                                break
        return 'not found'

    def path_to(self, nloc):
        return self.astar(self.map, self.position, nloc)