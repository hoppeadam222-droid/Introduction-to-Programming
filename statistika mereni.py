values = [2, 4, 4, 4, 5, 5, 7, 9]

def mean(values):
    for i in values:
        sum = 0
        sum = sum + values[i]
        delitel = i
    arit_prumer = sum/delitel
    return arit_prumer

def median(values):
    if len(values) % 2 != 0:
        clen = len(values)//2
        med = values[clen]
    else:
        cleny = len(values)//2
        med = (values[cleny - 1] + values[cleny + 1])/2
    return med

prumer = mean(values)
print(prumer)
print(median(values))
