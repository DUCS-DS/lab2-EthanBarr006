
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""
    if len(lst) <= 1:
        return True
    
    increasing = decreasing = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            increasing = False
        if lst[i] > lst[i-1]:
            decreasing = False
    return increasing or decreasing

print(monotonic([1, 2, 3, 4, 5]))
print(monotonic([5, 4, 3, 2, 1]))

monotonic([2, 2, 3, 4, 5])
