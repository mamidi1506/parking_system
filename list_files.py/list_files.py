import os

for root, dirs, files in os.walk('.'):
    print(f"DIR: {root}")
    for file in files:
        print(f"  FILE: {file}")
