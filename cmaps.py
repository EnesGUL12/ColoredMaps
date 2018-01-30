# Project: Colored maps, task from Charles Wetherell book
#
# https://github.com/EnesGUL12/ColoredMaps.git
#
# dr.doberman, EnesGUL, Faf_Faf
#


MAP_NODES = [
    ["WA", 0, 0],
    ["ID", 2, 0],
    ["MT", 3, 0],
    ["ND", 4, 0],
    ["MN", 5, 0],
    ["WI", 6, 0],
    ["MI", 7, 0],
    ["NY", 9, 0],
    ["VT", 10, 0],
    ["ME", 11, 0],
    ["OR", 0, 1],
    ["NV", 1, 1],
    ["UT", 2, 1]
    ["MY", 3, 1]
    ["SD", 4, 1]
    ["IA", 5, 1]
    ["IL", 6, 1]
    ["OH", 7, 1]
    ["PA", 8, 1]
    ["NJ", 9, 1]
    ["MA", 10, 1]
    ["NH", 11, 1]
    ["CA", 0, 2]
    ["AZ", 2, 2]
    ["CO", 3, 2]
    ["NE", 4, 2]
    ["MO", 5, 2]
    ["IN", 6, 2]
    ["WV", 8, 2]
    ["DE", 9, 2]
    ["CT", 10, 2]
    ["RI", 11, 2]
    ["NM", 3, 3]
    ["KA", 4, 3]
    ["AR", 5, 3]
    ["KY", 7, 3]
    ["VA", 8, 3]
    ["MD", 9, 3]
    ["OK", 4, 4]
    ["LA", 5, 4]
    ["MS", 6, 4]
    ["TN", 7, 4]
    ["NC", 8, 4]
    ["DC", 9, 4]
    ["TX", 4, 5]
    ["AL", 6, 5]
    ["GA", 7, 5]
    ["SC", 8, 5]
    ["FL", 7, 6]
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
    