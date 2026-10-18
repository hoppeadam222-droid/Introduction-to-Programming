import math
vp = int(20)
ang = 45
g = 9.81
time = int(0)
y = 0
x = 0
vx = vp * math.cos(ang)
vy = vp * math.sin(ang)
ymax = 0

while y >= 0:
    x = vp * math.cos(ang) * time
    y = vp * math.sin(ang) * time - (1/2)*g*(time**2)
    vy = vp * math.sin(ang) - g * time
    v = math.sqrt(vx**2 + vy**2)
    if y < 0:
        print(f"Vzdalenost dopadu: {x}")
        print(f"Maximalni vyska: {ymax}")
        print(f"Cas dopadu: {time}")
        break
    else:
        print(f"souradnice x: {x} souradnice y:  {y} rychlost: {v}")
        time = time + 0.1
    if ymax < y:
        ymax = y
    else:
        continue
    time = time + 0.001