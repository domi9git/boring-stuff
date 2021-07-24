fov = int(input("enter a number in arcseconds "))
arcsecs = fov
while arcsecs > 60:
    arcsecs -= 60
arcsecs = round(arcsecs, 6)
arcmins = fov / 60
while arcmins > 60:
    arcmins -= 60
arcmins = (arcmins * 60 - arcsecs) / 60
arcmins = round(arcmins, 6)
deg = (fov-(arcsecs + arcmins * 60)) / 3600
deg = round(deg, 6)
if arcsecs == 60:
 arcsecs -= 60
 arcmins += 1
if arcmins == 60:
 arcmins -= 60
 deg += 1
if arcmins == -0.0:
 arcmins = 0.0
arcsecs = str(arcsecs)
arcmins = str(arcmins)
deg = str(deg)
print("arcsecs: ", arcsecs)
print("arcmins: ", arcmins)
print("degrees: ", deg)