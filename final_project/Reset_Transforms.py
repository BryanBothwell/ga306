import maya.cmds 

def Reset_Transforms():

    cmds.xform(centerPivots=True)
    cmds.makeIdentity(apply=True, translate=1, rotate=1, scale=1, normal=0)
    cmds.delete(constructionHistory=True)
    
Reset_Transforms()