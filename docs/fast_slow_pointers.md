# Fast and slow pointers

## The Core Idea

Two pointers that move through data at different speeds - typically one moves twice as fast as the other. This creates a mathematical relationship that solves certain problems elegantly.

**Common Uses**: 

1. Cycle Detection

Floyd's Cycle Detection Algorithm (aka "tortoise and hare")

```bash
    '
Linked list with cycle:
1 → 2 → 3 → 4 → 5
        ↑       ↓
        8 ← 7 ← 6
```

slow: moves 1 step at a time
fast: moves 2 steps at a time


If there's a cycle, fast will eventually "lap" slow and they'll meet
If no cycle, fast reaches the end (null)


2. Find middle of linked list

If ptr12 walks at double the speed of ptr1, when ptr2 reaches the end, ptr1 will be at the middle.