def first_over_budget(purchases,budget):
    for number in purchases:
        if number>budget:
            return(number)
    return(None)
print(first_over_budget([10, 80, 20], 50))# 80
print(first_over_budget([70, 90, 20], 50))  # 70, not 90
print(first_over_budget([10, 50, 20], 50))  # None
print(first_over_budget([], 50))           # None

        