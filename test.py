import random
import sys

num = int(random.random() * 10)

print(num)
if num > 6:
    print("Bad")
    sys.exit(1)
else:
    print("Good")
    sys.exit(0)
