MAX_ITER = 200
def fractal(c,number):
    prevz = 0
    period = 0
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        if number == 1:
            z = z**2 + c #mandelbrot
        elif number == 2:
            z = (abs(z.real) + abs(z.imag) * 1j)**2 + c #burning ship
        elif number == 3:
            z = (abs(z.real**2 - z.imag**2)+abs(z.real * z.imag) * -2j) + c # buffalo
        elif number == 4:
            z = (abs(z.real**2 - z.imag**2)+(z.real*z.imag*2j)) + c # celtic
        elif number == 5:
            z = (z.real+z.imag*-1j)**2 + c #mandelbar
        if z == prevz:
            n = MAX_ITER
            break
        n += 1
        period += 1
        if period > 20:
            period = 0
            prevz = z
    return n