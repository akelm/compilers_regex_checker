from typing import Set, List

from automaton import Automaton
from settings import states, alphabet, State


def check_string(text_: str, states_: List[State], alphabet_: Set[str]):
    if len(text_) == 0:
        return 'N'
    first = text_[0]
    automaton = Automaton(first, states_, alphabet_)
    if all(map(automaton.new_state, text_)):
        return automaton.check_accepting()
    else:
        return 'N'


if __name__ == "__main__":
    print("enter text:", end=" ")
    text = input()
    print("state: ", check_string(text, states, alphabet))
