from os import PathLike
from typing import List, Set

def read_puzzle(name: PathLike) -> Set[int]:
  with open(name, r) as fp:
    content = fp.readlines()
    data = set(int(x) for x in content)
  return data

def part1_process(data: Set[int]) -> List[int]:
  conjugate = set(2020-x for x in data)
  remainder = data & conjugate
  result = [(2020-x)* x for x in remainder if 1010 <= x]
  return result
