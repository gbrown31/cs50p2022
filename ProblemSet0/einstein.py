def main():
    m = input("m: ")
    print("E:", calculateJoules(int(m)))

def calculateJoules(mass=0):
    speedOfLight = 300000000
    return mass * pow(speedOfLight, 2)

main()