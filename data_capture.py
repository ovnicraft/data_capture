class DataStats:
    def __init__(self, items: list) -> None:
        self.items = items

    def less(self, high: int) -> int:
        return len([low for low in self.items if low < high])

    def between(self, low: int, high: int) -> int:
        return len([item for item in self.items if low <= item <= high])

    def greater(self, low: int) -> int:
        return len([high for high in self.items if high > low])


class DataCapture:
    def __init__(self) -> None:
        self.items = []

    def add(self, item: int) -> None:
        if not isinstance(item, int) or item < 0:
            raise ValueError("Only accept positive integers")
        self.items.append(item)

    def build_stats(self):
        return DataStats(self.items)
