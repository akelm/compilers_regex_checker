
from automaton import Automaton


def check_string(text_: str) -> str:
    if len(text_) == 0:
        return 'N'
    first = text_[0]
    automaton = Automaton(first )
    if all(map(automaton.new_state, text_)):
        return automaton.check_accepting()
    else:
        return 'N'


if __name__ == "__main__":
    print("enter text:", end=" ")
    text = input()
    print("state: ", check_string(text))
