import random
from pathlib import Path
import time

random.seed()
x = random.randint(1, 1000000)
Path(f'c:{x}.txt').touch()
time.sleep(5)