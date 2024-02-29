people = [15, 30, 50, 10]
min_sum = 0

people.sort(reverse=True)
while people:
    min_sum += people[-1] * (len(people) - 1)
    people.pop()

print(min_sum)