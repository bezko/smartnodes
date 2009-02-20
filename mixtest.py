from SmartNode import *

plane = SmartNode("plane")
lambert = SmartNode(name="lambert1")
pt = SmartNode("place2dTexture") 
noise1 = SmartNode("noise")
noise1.colorGainB = 0
noise2 = SmartNode("noise")
noise2.noiseType= 3
noise2.colorGainG = 0 
 
#this needs to be automated somehow
(noise1.uv,noise1.uvFilterSize) = (noise2.uv,noise2.uvFilterSize) = (pt.outUV,pt.outUvFilterSize)
mix = SmartMix(noise1,noise2,blend=7)

lambert.color = mix.outColor
