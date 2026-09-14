from enum import Enum, auto
from copy import deepcopy
import math


class Effect(Enum):
    HEAL = auto()
    STAMINA = auto()


BASE_EFFECT = {Effect.HEAL: 5, Effect.STAMINA: 2}

effect = [[Effect.HEAL, Effect.STAMINA], [Effect.HEAL]]
data = {}
for r in effect:
    for e in r:
        data[e] = 0
for k, v in data.items():
    v = BASE_EFFECT[k] * 10
    print(v)
print(data)
effect = deepcopy(data)
print(effect)
