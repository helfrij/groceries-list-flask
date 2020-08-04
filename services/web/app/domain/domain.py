from typing import List
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class GroceryItem:
    id: int
    name: str
    quantity: int


@dataclass_json
@dataclass
class GroceryList:
    id: int
    name: str
    items: List[GroceryItem] = field(default_factory=list)
