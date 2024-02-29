n = 3       # 물건 3개
target = 30 # knapsack limit, 30kg
things = [(5, 50), (10, 60), (20, 140)]

things.sort(key = lambda x : (x[1] / x[0]), reverse = True)

sum = 0

for kg, price in things:
    per_price = price / kg
    # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣기

    if target < kg:
        sum += target * per_price
        break

    sum += price
    target -= kg

print(int(sum))