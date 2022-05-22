from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7


class StateMachine:
    state = State.A

    def send(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 1],
            State.E: [State.B, 5],
            State.F: [State.G, 6],
            State.G: [State.D, 9],
        })

    def lower(self):
        return self.update({
            State.C: [State.D, 2],
            State.G: [State.B, 7],
        })

    def patch(self):
        return self.update({
            State.D: [State.E, 3],
            State.E: [State.F, 4],
            State.G: [State.G, 8],
        })

    def update(self, transitions):
        try:
            self.state, signal = transitions[self.state]
            return signal
        except KeyError:
            raise KeyError
            
def main():
    obj = StateMachine()
    return obj