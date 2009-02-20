from SmartNode import *
import math

cube = SmartNode("cube")
sinusx = SmartSinus(1,amp=2)
sinusz = SmartSinus(1,amp=2,phase=math.pi/2)
randiy = SmartRandi(8,amp=.5,offset=1)
cube.tx = sinusx.out[0]
cube.tz = sinusz.out[0]
cube.sy = randiy.out[0]
cube.sz=cube.sx = 1/randiy.out[0]
