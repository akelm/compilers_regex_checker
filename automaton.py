from collections import defaultdict



from settings import alphabet, states, State

class Automaton:
    def __init__(self):
        self._states_list = states
        self._on_input = defaultdict(lambda: State.on_other)
        if len(alphabet) < 2:
            raise "too short alphabet"
        self._on_input[alphabet[0]] = State.on_first
        self._on_input[alphabet[1]] = State.on_opposite
        self._state_number = 0

    def new_state(self, x: str) -> bool:
        current_state: State = self._states_list[self._state_number]
        next_state_num = self._on_input[x](current_state)
        if next_state_num is None:
            return False
        else:
            self._state_number = next_state_num
            return True

    def check_accepting(self) -> str:
        return self._states_list[self._state_number].accepting
