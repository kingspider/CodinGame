import sys
import math

defibrillators = {}
closedefibdist = 1000000
closedefib = ""

lon = input()
lat = input()
n = int(input())


def defibdistance(loclong, loclat, defiblong, defiblat):
    """ Function converts inputs to floats them fiqures out the distance from the local location """
    defiblong = float(defiblong.replace(",", "."))
    defiblat = float(defiblat.replace(",", "."))
    loclong = float(loclong.replace(",", "."))
    loclat = float(loclat.replace(",", "."))
    x = (defiblong - loclong)
    y = (defiblat - loclat)
    d = math.sqrt(x ** 2 + y ** 2) * 6371
    return d


for i in range(n):
    defib = input().split(";")
    defibrillators[defib[0]] = defib[1:]

for defib in defibrillators.keys():
    distance = defibdistance(lon, lat, defibrillators[defib][-2], defibrillators[defib][-1])
    address = defibrillators[defib][0]
    print("Defib: Distance: " + str(defib) + " : " + str(distance), file=sys.stderr)
    if distance < closedefibdist:
        closedefibdist = distance
        closedefib = address
    else:
        continue

print(closedefib)
