from __future__ import annotations
from typing import Any, Generic, TypeVar

VT = TypeVar("VT")

__all__ =  (
    "UStack",
)

class UStack(Generic[VT]):
    def __init__(self, __list: list[VT] = list()) -> UStack:
        """
        UStack's methods:
            append(*items) - to add item to begin.
            empty() - true if stack is empty.
            pop() - delete the last element in stack.
        """
        self.__list = __list
        
    def pop(self) -> VT:
        """Return and remove top element."""
        return self.__list.pop()

    @property
    def top(self) -> VT:
        """Top element of stack."""
        return self.top()
    
    def top(self) -> VT:
        """Gets top element of stack."""
        if self:
            return self.__list[-1]
        else:
            return False
        
    def append(self, *items) -> UStack:
        """Append items to stack"""
        self.__list.extend(items)
        return UStack(self.__list)
    
    def is_empty(self) -> bool:
        return len(self) == 0

    def __add__(self, stack: UStack) -> UStack:
        return UStack(self.__list + stack.__list)

    def __radd__(self, stack: UStack) -> UStack:
        return UStack(stack.__list + self.__list)
    
    def __len__(self) -> int:
        return len(self.__list)
    
    def __nonzero__(self) -> bool:
        return not self.is_empty()