def main():
    import colorsys
    pallete = []
    hsv = []
    smoothener_hsv = []
    color_amnt = int(input('enter the amount of colors on your pallete'))
    current = 0
    smooth = 16
    red_d = 0
    grn_d = 0
    blu_d = 0
    rgbtohsv = ()
    hsv.clear()
    red = int(input('red'))
    grn = int(input('grn'))
    blu = int(input('blu'))
    rgbtohsv = colorsys.rgb_to_hsv(red,grn,blu)
    hsv.append(round(rgbtohsv[0]*255))
    hsv.append(round(rgbtohsv[1]*255))
    hsv.append(rgbtohsv[2])
    pallete.append(hsv)
    for n in range(0,color_amnt-1):
        hsv = []
        red = int(input('red'))
        grn = int(input('grn'))
        blu = int(input('blu'))
        rgbtohsv = colorsys.rgb_to_hsv(red,grn,blu)
        hsv.append(round(rgbtohsv[0]*255))
        hsv.append(round(rgbtohsv[1]*255))
        hsv.append(rgbtohsv[2])
        print('smoothening...')
        red = round(rgbtohsv[0]*255)
        grn = round(rgbtohsv[1]*255)
        blu = round(rgbtohsv[2])
        print(pallete[0][2])
        print(blu)
        print(hsv[2])
        if pallete[current*smooth][0] > hsv[0]:
            red_d = (pallete[current*smooth][0] - hsv[0]) / smooth
            red = pallete[current*smooth][0]
        if pallete[current*smooth][0] < hsv[0]:
            red_d = (hsv[0] - pallete[current*smooth][0]) / smooth
            red = pallete[current*smooth][0]
        if pallete[current*smooth][1] > hsv[1]:
            grn_d = (pallete[current*smooth][1] - hsv[1]) / smooth
            grn = pallete[current*smooth][1]
        if pallete[current*smooth][1] < hsv[1]:
            grn_d = (hsv[1] - pallete[current*smooth][1]) / smooth
            grn = pallete[current*smooth][1]
        if pallete[current*smooth][2] > hsv[2]:
            blu_d = (pallete[current*smooth][2] - hsv[2]) / smooth
            blu = pallete[current*smooth][2]
        if pallete[current*smooth][2] < hsv[2]:
            blu_d = (hsv[2] - pallete[current*smooth][2]) / smooth
            blu = pallete[current*smooth][2]
        for n in range(0,smooth-1):
            smoothener_hsv = []
            if pallete[current*smooth][0] > hsv[0]:
                red = round(red - red_d)
            if pallete[current*smooth][0] < hsv[0]:
                red = round(red + red_d)
            if pallete[current*smooth][1] > hsv[1]:
                grn = round(grn - grn_d)
            if pallete[current*smooth][1] < hsv[1]:
                grn = round(grn + grn_d)
            if pallete[current*smooth][2] > hsv[2]:
                blu = round(blu - blu_d)
            if pallete[current*smooth][2] < hsv[2]:
                blu = round(blu + blu_d)
            smoothener_hsv.append(red)
            smoothener_hsv.append(grn)
            smoothener_hsv.append(blu)
            pallete.append(smoothener_hsv)
        pallete.append(hsv)
        current += 1
    print(pallete)

if __name__ == '__main__':
    main()