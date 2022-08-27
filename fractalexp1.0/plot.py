from PIL import Image, ImageDraw, ImageTk
from fractal import fractal, MAX_ITER
import tkinter as tk
import time
import os
ZOOM = 0.25
# Image size (pixels)
WIDTH = 512
HEIGHT = 512
OFFSETR = 0
OFFSETI = 0

# Plot window
RE_START = -1/ZOOM
RE_END = 1/ZOOM
IM_START = -1/ZOOM
IM_END = 1/ZOOM

palette = []
number = 1
print("domi9's crappy fractal explorer ver 1.0")
print("the fractal image generator code was taken from codingame.com")
im = Image.new('HSV', (WIDTH, HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
tm = time.time()
print("rendering...")
RE_START = -1/ZOOM
RE_END = 1/ZOOM
IM_START = -1/ZOOM
IM_END = 1/ZOOM
for x in range(0, WIDTH):
    for y in range(0, HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START)+OFFSETR,
                    IM_START + (y / HEIGHT) * (IM_END - IM_START)+OFFSETI)
        # Compute the number of iterations
        m = fractal(c,1)
        # The color depends on the number of iterations
        hue = int(255 * m / MAX_ITER)
        saturation = 255
        value = 255 if m < MAX_ITER else 0
        # Plot the point
        draw.point([x, y], (hue, saturation, value))
im.convert('RGB').save('img.png', 'PNG')
root = tk.Tk()
root.geometry("512x540")
# Create a photoimage object of the image in the path
image = Image.open("img.png")
test = ImageTk.PhotoImage(image)

label1 = tk.Label(image=test)
label1.image = test
tm = time.time() - tm
print("rendering finished, took",round(tm,2),"seconds")
def gen(number,save):
    if save == False:
        print("rendering...")
    else:
        print("saving... (note that it overwrites the previously saved image)")
    tm = time.time()
    global OFFSETR, OFFSETI, ZOOM, WIDTH, HEIGHT, RE_START, RE_END, IM_START, IM_END
    RE_START = -1/ZOOM
    RE_END = 1/ZOOM
    IM_START = -1/ZOOM
    IM_END = 1/ZOOM
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            # Convert pixel coordinate to complex number
            c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START)+OFFSETR,
                        IM_START + (y / HEIGHT) * (IM_END - IM_START)+OFFSETI)
            # Compute the number of iterations
            m = fractal(c,number)
            # The color depends on the number of iterations
            hue = int(255 * m / MAX_ITER)
            saturation = 255
            value = 255 if m < MAX_ITER else 0
            # Plot the point
            draw.point([x, y], (hue, saturation, value))
    if save == False:
        im.convert('RGB').save('img.png', 'PNG')
    else:
        im.convert('RGB').save('img.png', 'PNG')
        im.convert('RGB').save('output.png', 'PNG')
    image = Image.open("img.png")
    test = ImageTk.PhotoImage(image)

    label1 = tk.Label(image=test)
    label1.image = test
    
    # Position image
    label1.place(x=0, y=0)
    os.remove("img.png")
    #label1.bind("<Key>", key)
    label1.bind("<Button-1>", callback)
    tm = time.time() - tm
    if save == False:
        print("rendering finished, took",round(tm,2),"seconds")
    else:
        print("saving finished, took",round(tm,2),"seconds")
# Position image
label1.place(x=0, y=0)
os.remove("img.png")
#def motion(event):
#    x, y = event.x, event.y
#    if not y > 512:
#        print('{}, {}'.format(RE_START+(x/512)*(RE_END - RE_START)+OFFSETR, IM_START+(y/512)*(IM_END - IM_START)+OFFSETI))
#def key(event):
#    print("pressed", repr(event.char))
def callback(event):
    global OFFSETR, OFFSETI, ZOOM, WIDTH, HEIGHT, RE_START, RE_END, IM_START, IM_END, number
    if not event.y > 512:
        print("clicked at", str(RE_START+(event.x/512)*(RE_END - RE_START)+OFFSETR), str(IM_START+(event.y/512)*(IM_END - IM_START)+OFFSETI)+"j")
        OFFSETR = RE_START+(event.x/512)*(RE_END - RE_START)+OFFSETR
        OFFSETI = IM_START+(event.y/512)*(IM_END - IM_START)+OFFSETI
        gen(number,False)
def zoomin():
    global ZOOM, number
    ZOOM *= 2
    label1.destroy()
    print("current zoom level:",ZOOM)
    gen(number,False)
def zoomout():
    global ZOOM, number
    ZOOM /= 2
    label1.destroy()
    print("current zoom level:",ZOOM)
    gen(number,False)
def cf():
    global number, ZOOM, OFFSETR, OFFSETI
    ZOOM = 0.25
    OFFSETR = 0
    OFFSETI = 0
    number += 1
    if number == 2:
        print("fractal set to burning ship")
    elif number == 3:
        print("fractal set to buffalo")
    elif number == 4:
        print("fractal set to celtic")
    elif number == 5:
        print("fractal set to mandelbar")
    if number > 5:
        number = 1
        print("fractal set to mandelbrot")
    label1.destroy()
    gen(number,False)
def save():
    gen(number,True)
#root.bind('<Motion>', motion)
#label1.bind("<Key>", key)
label1.bind("<Button-1>", callback)
zoomi = tk.Button(
   root, 
   text="Zoom In", 
   command=zoomin
)
zoomi.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
zoomi.place(x=0, y=516)
zoomo = tk.Button(
   root, 
   text="Zoom Out", 
   command=zoomout
)
zoomo.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
zoomo.place(x=55, y=516)
cf = tk.Button(
   root, 
   text="Change Fractal", 
   command=cf
)
cf.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
cf.place(x=120, y=516)
save = tk.Button(
   root, 
   text="Save Image", 
   command=save
)
save.pack(
    ipadx=1,
    ipady=1,
    expand=True
)
save.place(x=209, y=516)
root.resizable(False, False)
root.title("domi9's crappy fractal explorer ver 1.0")
root.mainloop()