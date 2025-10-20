# DSA Cheatsheet

## Strategies

- [Two pointers (arrays/strings)](./docs/two_pointers.md)
- [Sliding window](./docs/sliding_window.md)
- [Fast and slow pointer (linked lists, cycles)](./docs/fast_slow_pointers.md)
- Hash maps for O(1) lookups
- BFS/DFS for trees and graphs
- Binary search variations


Concepts:
- Single pass: Iterate through the input only once. Solve the problem in a single traversal from start to end. For example, see leetcode problem 1 solution.

## Linked list

Search: O(n)
Insert: O(n), but can be O(1) in known positions
Delete: O(n), but can be O(1) in known positions

Obs: Linked lists have poor cache locality because their nodes can be scattered throughout memory, whereas arrays are stored in contiguous blocks of memory.

## Array

Access: O(1) -> Directly through index
Search (unsorted): O(n)
Search (sorted): O(log n) -> Binary search
Insert: O(1) (end) or O(n) (beginning, middle) -> Needs to rellocate memory
Delete: O(1) (1) or O(n) (beginning, middle) -> Needs to rellocate memory

## Hash table
Search: O(1)
Insert: O(1)
Delete: O(1)

C++:    std::unordored_map
    - Can be accessed via [] or via .at(). They differ in behavior. [] Creates the element. .at() raises an exception.
Python: dictionary

Python: Built-in dictionaries
    - Can be accessed via [key] or .get(key, default_value)
 






----------------------------------------
for idx, element in enumerate(myList):
    Forma útil de percorrer lista em python, pegando tanto elemento quanto indice.

