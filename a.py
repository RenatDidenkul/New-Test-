def average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)

numbers = list(map(int, input().split()))
print("Середнє значення списку:", average(numbers))
    