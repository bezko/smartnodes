from SmartNode import *
noise = SmartNode("noise")
pt = SmartNode("place2dTexture")
noise.uv = pt.outUV
noise.uvFilterSize = pt.outUvFilterSize

pt.repeatU = 16
pt.repeatV = SmartSinus(.5,amp=2,offset=3).out[0]
pt.repeatU = SmartSinus(1.3,amp=2,offset=5).out[0]
noise.threshold = .5
noise.spottyness = .4;
noise.sizeRand = .66;
