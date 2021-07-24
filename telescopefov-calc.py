def main():
 a = int(input("enter the focal length of your telescope "))
 b = int(input("enter the aperture of your telescope "))
 c = int(input("enter the focal length of your eyepiece "))
 d = int(input("enter the true fov of your telescope "))
 e = int(input("what kind of barlow/reducer you have (type only the numbers bit (enter 1 for none)) "))
 f = d / (a / c) * 3600 / e
 print("arcsecs: ", f)

if __name__ == '__main__':
 main()
