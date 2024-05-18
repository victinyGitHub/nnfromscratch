import random

a = [1,2,3,4,5]

a_prev = a.copy()

b = [5, 4, -100, 2, 899]

difference = 5

def update():
    global a, a_prev, difference
    a_prev = a.copy()
    a = list(map(lambda x: x + difference, a))
    print(a)

update()

current = 0
def explore():
    global current

    d = random.random()

    up = current + d
    down = current - d

    pred = lambda current: list(map(lambda x: x + current, a_prev))
    predcurrent = pred(current)
    predup = pred(up)
    preddown = pred(down)

    reality_pred_difference = lambda pred: sum( [x - y for (x, y) in zip(a, pred)] )
    rpd = reality_pred_difference

    best_rpd = min(abs(rpd(predup)), abs(rpd(preddown)), abs(rpd(predcurrent)))
    if (best_rpd == rpd(predup)):
        current = up
    elif (best_rpd == rpd(preddown)):
        current = down

while True:
    input()
    print("Current = " + str(current))
    print(a)
    update()
    explore()
    print("Updated current: ", current)
    print("Target: ", difference)