from SmartNode import *

lambert = SmartNode(name="lambert1")
noise = SmartNode("noise")
lambert.color = noise.outColor
pt = SmartNode("place2dTexture")
(noise.uv,noise.uvFilterSize) = (pt.outUV,pt.outUvFilterSize)
pt.repeatU = 16
pt.repeatV = SmartSinus(.5,amp=2,offset=3).out[0]
pt.rotateUV = SmartSinus(.33,amp=180,offset=5).out[0]
noise.threshold = .5
noise.spottyness = .4;
noise.sizeRand = .66;
 