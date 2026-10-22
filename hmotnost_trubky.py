def circle_area(d):
    r = d/2
    s = r**2 * 3.14
    return s

def tube_cross_section(d_out, d_in):
    tcs = circle_area(d_out) - circle_area(d_in)
    return tcs

def tube_mass(d_out, d_in, length, density = 7850):
    hmotnost = (circle_area(d_out) - circle_area(d_in)) * length * density
    return hmotnost
vysledky = tube_mass(0.06, 0.05, 6)
print(vysledky)

