import maya.cmds as mc
import math

class SmartNode():
    def __init__(self,*args,**kwargs):
        type=""
        name="" 
        builder=""             
        if (len(args)>0):
            type=args[0]
        if ("name" in kwargs):
            name = kwargs["name"]
        #need a cleaner way of doing this    
        if (type == 'noise'):
           name = mc.shadingNode( "noise",asTexture = True )
        elif (type == 'place2dTexture'):
            name = mc.shadingNode("place2dTexture",asUtility  = True)
        elif (type=='expression'):
            name=mc.expression()
        elif (type=='cube'):
            (name,builder)=mc.polyCube();
                             
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
        self.e=(".O[0]=%f+%f*sin(time*%f+%f);"%(offset,amp,freq,phase))
        
class SmartRandh(SmartNode):
    def __init__(self,freq,seed=0,offset=0,amp=1):
         SmartNode.__init__(self,"expression")
         self.e=(".O[0]=%f+%f*noise(floor(time*%f)+%f);"%(offset,amp,freq,seed))
         
class SmartRandi(SmartNode):
    def __init__(self,freq,seed=0,offset=0,amp=1):
         SmartNode.__init__(self,"expression")
         self.e=("""float $offset=%f;
                    float $amp=%f;
                    float $freq=%f;
                    float $seed=%f;
                    float $cur  =$offset+$amp*noise(floor(time*$freq)+$seed);
                    float $next =$offset+$amp*noise(floor(time*$freq)+$seed+1);
                    float $phase = fmod(time*$freq,1);  
                    .O[0]=(1-$phase)*$cur + $phase*$next;
                 """%(offset,amp,freq,seed))                        