# Project: Colored maps, task from Charles Wetherell book
#
# https://github.com/EnesGUL12/ColoredMaps.git
#
# dr.doberman, EnesGUL, Faf_Faf
#


MAP_NODES = [
    ["WA", 0, 0],
    ["ID", 2, 0]
]
MAP_LINKS = {
    "WA": ["OR", "ID"],
    "ID": ["WA", "MT", "WY", "UT", "NV", "OR"]
}

class Node():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.peers = []
        self.color = -1
    
    def AddPeer(self, node):
        if not self.IsLinked(node):
            self.peers.append(node)
            node.AddPeer(self)
        elif not node.IsLinked(self):
            raise Exception("Broken link from", node.name, "to", self.name)
    
    def IsLinked(self, node):
        for n in self.peers:
            if n.name == node.name:
                return True
        
        return False



def map_create():
    map = dict()
    # Пройти по MAP_NODES
    for mi in MAP_NODES:
        # Cоздать новый узел
        map[mi[0]] = Node(mi[0], mi[1], mi[2])
    
    # Пройти по MAP_LINKS 
    for n, l in MAP_LINKS:    
        # Связать узлы
        for ll in l:
            map[n].AddPeer(map[ll])

    return map
    