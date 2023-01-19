from __future__ import annotations

from abc import ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class AbstractNode(ABC):
    name: str

@dataclass
class Node(AbstractNode):
    left: Optional[AbstractNode]
    right: Optional[AbstractNode]

@dataclass
class Leaf(AbstractNode):
    pass
