import maya.cmds as mc
import math

numOfStairs=0
stepInt=0
stairWidth=6
radiusOfPoles=0.2
heightOfPoles=3
widthOfHandrail=0.3
heightOfHandrail=1.4
depthOfHandrail=0.5

#Spiral staircase variables
spiralRadius=1.5

#Rotation variables
rY=45
rX=90
rZ=90

#Movement variables
yMove=16
zMove=12

def UpdateNum(num):
    print(num)
    global numOfStairs
    numOfStairs=num
    print(numOfStairs)

def HandrailOn(*args):
    CreateHandrail()

def HandrailOff(*args):
    DeleteHandrail()

def SpiralHandrailOn(*args):
    CreateSpiralHandrail()

def SpiralHandrailOff(*args):
    DeleteSpiralHandle()

#Create a complete straight staircase, and stored in a group
def CreateStraightStaircase(*args):
    print(numOfStairs)

    straightGrp=mc.group(em=True, name="Straight_Staircase_Grp")
    
    for i in range(numOfStairs):
         stair=mc.polyCube(name="stairs", width=stairWidth)
         mc.parent(stair, straightGrp)
         mc.move(0,i,i)
        
def DeleteHandrail():
    mc.delete("Handrail_Grp")
        
def CreateHandrail():
    handrailGroup=mc.group(em=True, name="Handrail_Grp")
    
    #Creating the supports for the hand rails
    for i in range(numOfStairs):
        print("Creating poles for the handrails")
        pole1=mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
        mc.move(stairWidth/2,i+2,i)
        mc.parent(pole1, handrailGroup)
        
        pole2=mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
        mc.move(-stairWidth/2,i+2,i)
        mc.parent(pole2, handrailGroup)
        
        #Creating the hand rail
        handrail1=(mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail))
        mc.move(stairWidth/2,i+3.5,i)
        mc.rotate(rX,rY,rZ)
        mc.parent(handrail1, handrailGroup)
        
        handrail2=mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail)
        mc.move(-stairWidth/2,i+3.5,i)
        mc.rotate(rX,rY,rZ)
        mc.parent(handrail2, handrailGroup)

#Create a complete spiral staircase, and stored in a group
def CreateSpiralStaircase(*args):
    spiralGrp=mc.group(em=True, name="Spiral_Staircase_Grp")
    
    #Creating the steps for the spiral staircase
    for i in range(numOfStairs):
        spiralStep=mc.polyCube(name="spiral", width=stairWidth, depth=stairWidth/2)
        mc.move(stairWidth,i,0)
        mc.xform(ws=True, rotatePivot=(0,0,0))
        mc.rotate(0,i*15,0)
        mc.parent(spiralStep, spiralGrp)
        
    #Creating the center support for the spiral staircase
    spiralCenter=mc.polyCylinder(name="center", radius=spiralRadius, height=int(numOfStairs))
    mc.move(0,numOfStairs/2,0)
    mc.parent(spiralCenter, spiralGrp)

#Creating spiral handrails
def CreateSpiralHandrail():
    mc.group(em=True, name="SpiralStaircaseGroup")
    
    for i in range(numOfStairs+2):
        if i > 2:
            pole1=mc.polyCylinder(name="poles" + str(i), radius=radiusOfPoles, height=heightOfPoles)
            mc.move(stairWidth,i-1,stairWidth)
            mc.xform(ws=True, rotatePivot=(0,0,0))
            mc.rotate(0,i*15,0)

            handrail1=(mc.polyCube(name="handrail", width=widthOfHandrail, height=depthOfHandrail+2, depth=heightOfHandrail))
            mc.move(stairWidth,i+0.5,stairWidth)
            mc.xform(ws=True, rotatePivot=(0,0,0))
            mc.rotate(0, mc.getAttr("poles" + str(i) + ".rotateY"), 0)
            
            mc.parent(pole1, "SpiralStaircaseGroup")
            mc.parent(handrail1, "SpiralStaircaseGroup")
    
def DeleteSpiralHandle():
    mc.delete("SpiralHandrail_Grp")

#Create an indivudal step. Stored in list:steps.
def CreateStep(*args):
    if stepInt == 0:
        mc.group(n="IndividualStepGroup", em=True)
        mc.group(em=True, name="IndividialHandrailGroup")
        
    global stepInt
    stepInt=stepInt + 1
    print(stepInt)
    step=mc.polyCube(name="step", width=stairWidth)
    mc.move(0,stepInt,stepInt)
    mc.parent(step, "IndividualStepGroup")
    
    for i in range(stepInt):
        print("Creating poles for the handrails")
        pole1=mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
        mc.move(stairWidth/2,i+2,i)
        mc.parent(pole1, "IndividialHandrailGroup")
        
        pole2=mc.polyCylinder(name="poles", radius=radiusOfPoles, height=heightOfPoles)
        mc.move(-stairWidth/2,i+2,i)
        mc.parent(pole2, "IndividialHandrailGroup")
        
        #Creating the hand rail
        handrail1=(mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail))
        mc.move(stairWidth/2,i+3.5,i)
        mc.rotate(rX,rY,rZ)
        mc.parent(handrail1, "IndividialHandrailGroup")
        
        handrail2=mc.polyCube(name="handrail", width=widthOfHandrail, height=heightOfHandrail, depth=depthOfHandrail)
        mc.move(-stairWidth/2,i+3.5,i)
        mc.rotate(rX,rY,rZ)
        mc.parent(handrail2, "IndividialHandrailGroup")
    
def Reset(*args):
    global numOfStairs
    global stepInt
    numOfStairs=0
    stepInt=0
    
    mc.select(ado=True)
    mc.delete()
    mc.checkBox('Checkbox1', e=True, value=False)
    mc.checkBox('Checkbox2', e=True, value=False)
    mc.intField('EntryField', e=True, value=0)

def UpdateStairWidth(*args):
    global stairWidth
    stairWidth=mc.floatSliderGrp('sWidthGrp', q=True, v=True)
    print(stairWidth)
    
#Create UI
mc.window(visible=True, s=False, title="Staircase Tool v1.0 by Dori C.", widthHeight=(250,300), backgroundColor=(0.1,0.15,0.2))
mc.columnLayout(columnAttach=('left', 0), rowSpacing=10, columnWidth=250)
mc.button(label="Reset", command=Reset, backgroundColor=(0.7,0.0,0.0), width=250)
mc.text("Number of Stairs: ")
mc.intField('EntryField', changeCommand=UpdateNum)
mc.button(label="Straight Staircase", command=CreateStraightStaircase, width=250)
mc.checkBox('Checkbox1', label="Add Handrail", onCommand=HandrailOn, offCommand=HandrailOff, value=False)
mc.button(label="Spiral Staircase", command=CreateSpiralStaircase, width=250)
mc.checkBox('Checkbox2', label="Add Handrail", onCommand=SpiralHandrailOn, offCommand=SpiralHandrailOff, value=False)
mc.button(label="Create Step", command=CreateStep, width=250)
mc.floatSliderGrp('sWidthGrp', label="Stair Width", columnWidth=(1,0), field=True, minValue=2, maxValue=10, value=stairWidth, changeCommand=UpdateStairWidth)
