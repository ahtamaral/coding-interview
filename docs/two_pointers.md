# Two pointers

## The Core Idea

Instead of using nested loops (which would be O(n²)), you use two indices that move through your data intelligently, reducing time complexity to O(n).
Common Scenarios

1. Opposite Ends (Moving Toward Each Other)

Start one pointer at the beginning, one at the end, and move them inward.

**Example:** Check if a string is a palindrome

"racecar"
 ↑     ↑
 L     R

Compare characters at L and R
- If equal: move both inward (L++, R--)
- If not equal: it's not a palindrome
```
