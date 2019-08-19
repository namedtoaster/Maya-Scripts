from maya import cmds

class HUDItem(object):
    """
    This is a HUD Item object that lets us create and modify a HUD Item
    """

    def __init__(self):

        # The __init__ mentod lets us set default values
        self.transform = None
        self.constructor = None

    def createHUDItem(self):
        self.transform, self.constructor = cmds.polyPlane(subdivisionsWidth=3, subdivisionsHeight=3)
        cmds.select(clear=True)

        # Delete the center face
        cmds.select('%s.f[%s]' % (self.transform, 4))
        cmds.delete()

        edges = [[17, 10, 3], [5, 12, 19], [14, 16, 18], [9, 11, 7]]
        cmds.select(clear=True)
        for edgeSet in edges:
            edgeIndex = edges.index(edgeSet)
            print edgeSet
            for edge in edgeSet:
                cmds.select('%s.e[%s]' % (self.transform, edge), add=True)

            if edgeIndex == 0:
                cmds.move(-0.3, relative=True)
            elif edgeIndex == 1:
                cmds.move(0.3, relative=True)
            elif edgeIndex == 2:
                cmds.move(0, 0, -0.3, relative=True)
            elif edgeIndex == 3:
                cmds.move(0, 0, 0.3, relative=True)

            cmds.select(clear=True)