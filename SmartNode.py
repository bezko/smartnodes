import maya.cmds as mc
import math

class SmartNode():
    def __init__(self,type,*args,**kwargs):
        name =""
        if (type == 'noise'):
           name = mc.shadingNode( "noise",asTexture = True )
        elif (type == 'place2dTexture'):
            name = mc.shadingNode("place2dTexture",asUtility  = True)
        elif (type=='expression'):
            name=mc.expression()                     
        self.__dict__['nodeName'] = name
        
        
    def __setattr__(self, name, value):
        plug = self.__dict__['nodeName'] + "." + name
        if isinstance(value,SmartPlug):
            mc.connectAttr( str(value), str(plug) )
        else:
            dataType =  mc.getAttr(str(plug),type=True)
            if dataType == 'float':
                 mc.setAttr(str(plug),value)
            else:    
                mc.setAttr(str(plug),value,type=dataType)
    def __getattr__(self, name):
        return SmartPlug(self.__dict__['nodeName'] + "." + name)   
    def __str__(self):
        return  self.__dict__['nodeName']
    
class SmartPlug():
    def __init__(self,name):
        self.__dict__['plugName'] = name  
    def __str__(self):
        return self.__dict__['plugName']
    def __getitem__(self,key):
        return SmartPlug("%s[%d]" %(self.__dict__['plugName'],key))
    
        
   
class SmartSinus(SmartNode):
    def __init__(self,freq,phase=0,offset=0,amp=1):                
        SmartNode.__init__(self,"expression")        
        freq = freq * 2 * math.pi           
        self.e=(".O[0]=%d+%d*sin(time*%d+%d);"%(offset,amp,freq,phase))       