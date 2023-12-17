import abc


class Traversal(abc.ABC):
    def __init__(self):
        pass

    def step(self):
        pass

    def init_value(self):
        pass

    def should_continue(self, current_val):
        pass


class Ascending(Traversal):

    def __init__(self, first, last):
        super().__init__()
        self.first = first
        self.last = last

    def step(self):
        return 2

    def init_value(self):
        return self.first if self.first % 2 == 0 else self.first + 1

    def should_continue(self, current_val):
        return current_val < self.last


class Descending(Traversal):

    def __init__(self, first, last):
        super().__init__()
        self.first = first
        self.last = last

    def step(self):
        return -2

    def init_value(self):
        return self.first if self.first % 2 == 0 else self.first - 1

    def should_continue(self, current_val):
        return current_val > self.last


class EvenGenerator:

    def __init__(self, first, last, step=2):
        if first > last:
            self.traversal = Descending(first, last)
        else:
            self.traversal = Ascending(first, last)

        self.current = self.traversal.init_value()

    def __iter__(self):
        return self

    def __next__(self):
        if self.traversal.should_continue(self.current):
            num = self.current
            self.current = self.current + self.traversal.step()
            return num
        raise StopIteration
