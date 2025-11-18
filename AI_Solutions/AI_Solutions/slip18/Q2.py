import heapq

room_area = 100  # 10x10 room

rect_area = 2    # each rectangle is 2x1
square_area = 1  # each square is 1x1

total_rect = 5
total_square = 4

class State:
    def __init__(self, placed_rect, placed_square, used_area):
        self.placed_rect = placed_rect
        self.placed_square = placed_square
        self.used_area = used_area

    def is_goal(self):
        return self.placed_rect == total_rect and self.placed_square == total_square

    def heuristic(self):
        remaining = (total_rect - self.placed_rect) * rect_area + \
                    (total_square - self.placed_square) * square_area
        return remaining

    def get_children(self):
        states = []
        if self.placed_rect < total_rect:
            states.append(State(self.placed_rect+1, self.placed_square, self.used_area+rect_area))

        if self.placed_square < total_square:
            states.append(State(self.placed_rect, self.placed_square+1, self.used_area+square_area))

        return states


def a_star():
    start = State(0, 0, 0)
    pq = []
    heapq.heappush(pq, (start.used_area + start.heuristic(), start))

    while pq:
        f, state = heapq.heappop(pq)

        if state.is_goal():
            return state.used_area

        for child in state.get_children():
            if child.used_area <= room_area:
                heapq.heappush(pq, (child.used_area + child.heuristic(), child))

    return None


used_area = a_star()
print("Minimum area utilized to place all objects:", used_area)
