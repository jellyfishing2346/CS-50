grocery = {}
while True:
    try:
        item = input()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break
for grocery, count in groceries.items():
    print(count, grocery)