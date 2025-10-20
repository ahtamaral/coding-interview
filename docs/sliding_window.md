# Sliding window

## The Core Idea
Maintain a "window" (subarray or substring) that slides through your data. Instead of recalculating everything for each possible subarray (which would be O(n²)), you add new elements and remove old ones as the window moves, achieving O(n).

Think of it like a literal window moving across your data:

```bash
Array: [1, 3, 2, 5, 1, 1, 4]
        [------]              window of size 3
           [------]           slide right: remove 1, add 5
              [------]        slide right: remove 3, add 1
```

Window can be fixed size or dynamic size.

### 1. Fixed-Size Window
The window size is constant throughout.

**Example: Maximum sum of k consecutive elements**
```
Array: [2, 1, 5, 1, 3, 2], k = 3

Initial window: [2, 1, 5] = 8
Slide: remove 2, add 1 → [1, 5, 1] = 7
Slide: remove 1, add 3 → [5, 1, 3] = 9
Slide: remove 5, add 2 → [1, 3, 2] = 6

Max = 9
```
### 2. Dynamic-Size Window (Most Common in Interviews!)
The window expands and contracts based on conditions.

**Example: Longest substring without repeating characters**
```
String: "abcabcbb"

Window: "a"       → valid, expand
Window: "ab"      → valid, expand
Window: "abc"     → valid, expand (length 3 ✓)
Window: "abca"    → invalid! 'a' repeats
                    → shrink from left until valid: "bca"
Window: "bcab"    → invalid! 'b' repeats
                    → shrink: "cab"
