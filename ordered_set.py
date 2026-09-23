#----------------------------------------------------------
# Lab #2: Ordered Set Class
# Implementation of a generic ordered set class and its
# corresponding operations.
#
# Date: 24-Sep-2025
# Authors:
#           A01802689 Pablo Alejandro Ortiz Montes
#           A0 Alexander Mejia Tovar
#----------------------------------------------------------
from __future__ import annotations
from typing import cast
from collections.abc import Iterator, Iterable

class OrderedSet[T]:
    class Node[N]:

        info: N
        prev: OrderedSet.Node[N]
        next: OrderedSet.Node[N]

        # Complexity: O(1)
        def __init__(self, value: N) -> None:
            self.info = value
            self.prev = self
            self.next = self

    __sentinel: OrderedSet.Node[T]
    __count: int

    # Complexity: O(N) where N = len(values)
    def __init__(self, values: Iterable[T] = ()) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0
        for elem in values:
            self.add(elem)

    # Complexity: O(1)
    def __len__(self) -> int:
        return self.__count

    # Complexity: O(N)
    def __repr__(self) -> str:
        return f'OrderedSet({list(self) if self else ""})'

    # Complexity: O(N)
    def add(self, value: T) -> None:
        if value in self:
            return
        self.__count += 1
        new_node: OrderedSet.Node[T] = OrderedSet.Node(value)
        new_node.prev = self.__sentinel.prev
        new_node.next = self.__sentinel
        self.__sentinel.prev.next = new_node
        self.__sentinel.prev = new_node

    # Complexity: O(N)
    def __iter__(self) -> Iterator[T]:
        current: OrderedSet.Node[T] = self.__sentinel.next
        while current is not self.__sentinel:
            yield current.info
            current = current.next

    # Complexity: O(N)
    def __contains__( self, value: object) -> bool:
        for elem in self:
            if elem == value:
                return True
        return False

    def discard(self,value: T) -> None:
        if value not in self: 
         return 
        current: OrderedSet.Node[T] = self.__sentinel.next
        adelante:OrderedSet.Node[T]=current.next 
        atras:OrderedSet[T]= current.prev

        if current.info == value:
            adelante.prev= atras
            atras.next = adelante
            return 

        while current.info != value:
            atras = current
            current = adelante
            adelante = adelante.next
        if current.info == value:
            atras.next= adelante
            adelante.prev = atras

    def remove(self, value: T) -> None:
        current = self.__sentinel.next
        while (current != self.__sentinel):
            if current.info == value:
                current.prev.next = current.next
                current.next.prev = current.prev
                del current
                self.__count -= 1
                return
            current = current.next
        raise KeyError(f"Value {value} not contained in the set.")

    def __eq__(self, other: object) -> bool:
        return set(self) == set(other)


    def __le__(self,other: OrderedSet[T]) -> bool:
        for i in self:
            if i not in other:
                return False
        return True

    def __lt__(self,other: OrderedSet[T]) -> bool:
        for i in self:
            if i not in other:
                return False
        return self != other
    
    def __ge__( self,other: OrderedSet[T]) -> bool:
        for i in other:
            if i not in self:
                return False
        return True


    def __gt__(self, other: OrderedSet[T]) -> bool:
        for i in other:
            if i not in self:
                return False
        return other != self

    def isdisjoint(self,other: OrderedSet[T]) -> bool:
        for i in other:
            if i in self:
                return False
        return True

    def __and__(self,other: OrderedSet[T]) -> OrderedSet[T]:
        Newlist: OrderedSet[T] = OrderedSet()
        for i in self:
            if i in other:
                Newlist.add(i)
        return Newlist
        
    def __or__(self,other: OrderedSet[T]) -> OrderedSet[T]:
        Newlist: OrderedSet[T] = OrderedSet()
        for i in self:
            Newlist.add(i)
        for y in other:
            Newlist.add(y)
        return Newlist
  

    def __sub__(self,other: OrderedSet[T]) -> OrderedSet[T]:
        Newlist: OrderedSet[T] = OrderedSet()
        for i in self:
            if i not in other:
                Newlist.add(i)
        return Newlist

    def __xor__(self,other: OrderedSet[T]) -> OrderedSet[T]:
        xor: OrderedSet = OrderedSet()
        for a in self:
            if a not in other:
                xor.add(a)
        for b in other:
            if b not in self:
                xor.add(b)
        return xor

    def clear(self) -> None:
        self.__sentinel = OrderedSet.Node(cast(T, None))
        self.__count = 0

    def pop(self) -> T:
        last = self.__sentinel.prev
        if self.__sentinel.prev == None:
            raise KeyError("Set is empty")
        self.__sentinel.prev = self.__sentinel.prev.prev
        self.remove(last.info)
        return last.info

if __name__ == "__main__":
    a = OrderedSet([4, 8, 15, 16, 23, 42])
    print(a)
    a.clear()
    print(a)