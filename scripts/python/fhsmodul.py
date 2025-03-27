import hou

def myFunction(scale):
    myNode = hou.node("/obj").createNode("null", "myNode")
    myNode.setName("mynode", unique_name=True)
    myNode.parm("scale").set(scale)
    myNode.parm("childcomp").set(1)
    
    myNode2 = hou.node("/obj").createNode("cam", "cam")
    myNode2.setInput(0, myNode)
    myNode2.setColor(hou.Color(1,0,0))
    
    
def callFunction50():
    with hou.undos.group("Create 50 Nodes"):
        for i in range(0, 50):
            myFunction(i)
        
        hou.node("/obj").layoutChildren()