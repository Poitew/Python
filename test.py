import random
import sys

num = int(random.random() * 10)

if num > 8:
    print("Bad")
    sys.exit(1)
else:
    print("Good")
    sys.exit(0)