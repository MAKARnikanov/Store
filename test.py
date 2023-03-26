import pytest
from utils import Item

def returned(self):
    desc = str(self.name) + " " + self.price + self.count
    return desc.title()
