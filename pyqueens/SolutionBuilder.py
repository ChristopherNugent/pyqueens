class SolutionBuilder:
    def __init__(self, n, w):
        self.n = n
        self.w = w
        self.state = [None for _ in range(n)]
        self.queens_count = 0
        self.solution_count = 0
        self.solutions = list()

    def get_safe_pos_list(self):
        n, w = self.n, self.w
        safe_pos_list = [True for i in range(n)]
        k = self.queens_count
        for i in range(k):
            if k - i >= n - w:
                continue
            j = self.state[i]
            safe_pos_list[j] = False
            h = k - i + j
            if h >= 0 and h < n:
                safe_pos_list[h] = False
            h = i - k + j
            if h >= 0 and h < n:
                safe_pos_list[h] = False
        return [i for i in range(n) if safe_pos_list[i]]

    def count_solutions(self):
        self.solution_count = 0
        self.state = [None for _ in range(self.n)]
        self.queens_count = 0
        self.__count_solutions()
        return self.solution_count

    def __count_solutions(self):
        if self.queens_count == self.n:
            self.solution_count += 1
        else:
            for pos in self.get_safe_pos_list():
                self.state[self.queens_count] = pos
                self.queens_count += 1
                self.__count_solutions()
                self.queens_count -= 1
