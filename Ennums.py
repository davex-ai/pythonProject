from enum import Enum


class State(Enum):
    ACTIVE = 0
    INACTIVE = 1

print(State.INACTIVE.value)
print(State['ACTIVE'])
print(list(State))
print(len(State))