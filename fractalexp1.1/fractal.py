MAX_ITER = 1000
def fractal(c,number):
    prevz = 0
    period = 0
    z = 0
    n = 0
    pallete = [[0,0,255],[0,0,0]] # put your own pallete here
    crnt = 0
    #nxt = 1
    #smooth = 0
    #max_smooth = 32
    pal_length = len(pallete)
    hue = pallete[crnt][0]
    sat = pallete[crnt][1]
    val = pallete[crnt][2]
    #hue_d = 0
    #sat_d = 0
    #val_d = 0
    #check = False
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
    #    if pallete[crnt][0] > pallete[nxt][0] and not check:
    #        hue_d = (pallete[crnt][0] - pallete[nxt][0]) / max_smooth
    #    if pallete[crnt][0] < pallete[nxt][0] and not check:
    #        hue_d = (pallete[nxt][0] - pallete[crnt][0]) / max_smooth
    #    if pallete[crnt][0] == pallete[nxt][0] and not check:
    #        hue_d = 0
    #    if pallete[crnt][1] > pallete[nxt][1] and not check:
    #        sat_d = (pallete[crnt][1] - pallete[nxt][1]) / max_smooth
    #    if pallete[crnt][1] < pallete[nxt][1] and not check:
    #        sat_d = (pallete[nxt][1] - pallete[crnt][1]) / max_smooth
    #    if pallete[crnt][1] == pallete[nxt][1] and not check:
    #        sat_d = 0
    #    if pallete[crnt][2] > pallete[nxt][2] and not check:
    #        val_d = (pallete[crnt][2] - pallete[nxt][2]) / max_smooth
    #    if pallete[crnt][2] < pallete[nxt][2] and not check:
    #        val_d = (pallete[nxt][2] - pallete[crnt][2]) / max_smooth
    #    if pallete[crnt][2] == pallete[nxt][2] and not check:
    #        val_d = 0
    #    check = True
    #    if pallete[crnt][0] > pallete[nxt][0]:
    #        hue = round(hue - hue_d)
    #    if pallete[crnt][0] < pallete[nxt][0]:
    #        hue = round(hue + hue_d)
    #    if pallete[crnt][1] > pallete[nxt][1]:
    #        sat = round(sat - sat_d)
    #    if pallete[crnt][1] < pallete[nxt][1]:
    #        sat = round(sat + sat_d)
    #    if pallete[crnt][2] > pallete[nxt][2]:
    #        val = round(val - val_d)
    #    if pallete[crnt][2] < pallete[nxt][2]:
    #        val = round(val + val_d)
    #    smooth += 1
    #    if smooth > max_smooth - 1:
    #        smooth = 0
    #        crnt += 1
    #        nxt += 1
    #        if crnt > pal_length - 1:
    #            crnt = 0
    #        if nxt > pal_length - 1:
    #            nxt = 0
    #        hue = pallete[crnt][0]
    #        sat = pallete[crnt][1]
    #        val = pallete[crnt][2]
    #        check = False
        period += 1
        crnt += 1
        #nxt += 1
        if crnt > pal_length - 1:
            crnt = 0
        #if nxt > pal_length - 1:
        #    nxt = 0
        hue = pallete[crnt][0]
        sat = pallete[crnt][1]
        val = pallete[crnt][2]
        if period > 20:
            period = 0
            prevz = z
    return n, hue, sat, val