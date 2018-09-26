import os
import sys

try:
    n = int(sys.argv[1])
except Exception:
    n = 8
try:
    speed = int(sys.argv[2])
except Exception:
    speed = 10


while True:
    try:
        os.system("python3 graphic-client.py {} {}".format(n, speed))
    except KeyboardInterrupt:
        quit()
