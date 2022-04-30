from collections import defaultdict
from typing import Set

from state import State


class Automaton:
    def __init__(self, first: str, states_list, alphabet: Set[str]):
        self.states_list = states_list
        self.on_input = defaultdict(lambda: State.on_other)
        if len(alphabet) < 2:
            raise "too short alphabet"
        if first in alphabet:
            opposite = alphabet.difference({first}).pop()
            self.on_input[first] = State.on_first
            self.on_input[opposite] = State.on_opposite
        self.state_number = 0

    def new_state(self, x: str) -> bool:
        current_state: State = self.states_list[self.state_number]
        next_state_num = self.on_input[x](current_state)
        if next_state_num is None:
            return False
        else:
            self.state_number = next_state_num
            return True

    def check_accepting(self):
        return self.states_list[self.state_number].accepting
