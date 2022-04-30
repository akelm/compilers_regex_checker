from typing import Optional


class State:
    def __init__(self, on_a: Optional[int], on_b: Optional[int], on_c: Optional[int], accepting: str):
        self._on_a = on_a
        self._on_b = on_b
        self._on_c = on_c
        self.accepting = accepting

    def on_first(self):
        return self._on_a

    def on_opposite(self):
        return self._on_b

    def on_other(self):
        return self._on_c
