import os
import math
def paint_calc(height, width, cover):
    x = (height*width)/cover
    return x

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

result = math.ceil(paint_calc(height=test_h, width=test_w, cover=coverage))

print(f"You'll need {result} cans of paint")

os.system('pause')