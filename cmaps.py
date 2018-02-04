# Project: Colored maps, task from Charles Wetherell book
#
# https://github.com/EnesGUL12/ColoredMaps.git
#
# dr.doberman, EnesGUL, Faf_Faf
#

import sys

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
    ["UT", 2, 1],
    ["WY", 3, 1],
    ["SD", 4, 1],
    ["IA", 5, 1],
    ["IL", 6, 1],
    ["OH", 7, 1],
    ["PA", 8, 1],
    ["NJ", 9, 1],
    ["MA", 10, 1],
    ["NH", 11, 1],
    ["CA", 0, 2],
    ["AZ", 2, 2],
    ["CO", 3, 2],
    ["NE", 4, 2],
    ["MO", 5, 2],
    ["IN", 6, 2],
    ["WV", 8, 2],
    ["DE", 9, 2],
    ["CT", 10, 2],
    ["RI", 11, 2],
    ["NM", 3, 3],
    ["KA", 4, 3],
    ["AR", 5, 3],
    ["KY", 7, 3],
    ["VA", 8, 3],
    ["MD", 9, 3],
    ["OK", 4, 4],
    ["LA", 5, 4],
    ["MS", 6, 4],
    ["TN", 7, 4],
    ["NC", 8, 4],
    ["DC", 9, 4],
    ["TX", 4, 5],
    ["AL", 6, 5],
    ["GA", 7, 5],
    ["SC", 8, 5],
    ["FL", 7, 6]
]
MAP_LINKS = {
    "WA": ["ID", "OR"],
    "ID": ["MT", "WY", "UT", "NV", "OR", "WA"],
    "MT": ["ND", "SD", "WY", "ID"],
    "ND": ["MN", "SD", "MT"],
    "MN": ["WI", "IA", "SD", "ND"],
    "WI": ["MI", "IL", "IA", "MN"],
    "MI": ["OH", "IN", "WI"],
    "NY": ["VT", "MA", "CT", "NJ", "PA"],
    "VT": ["NH", "MA", "NY"],
    "ME": ["NH"],
    "OR": ["WA", "ID", "NV", "CA"],
    "NV": ["ID", "UT", "AZ", "CA", "OR"],
    "UT": ["ID", "WY", "CO", "AZ", "NV"],
    "WY": ["MT", "SD", "NE", "CO", "UT", "ID"],
    "SD": ["ND", "MN", "IA", "NE", "WY", "MT"],
    "IA": ["MN", "WI", "IL", "MO", "NE", "SD"],
    "IL": ["WI", "IN", "MO", "IA"],
    "OH": ["MI", "PA", "WV", "KY", "IN"],
    "PA": ["NY", "NJ", "DE", "MD", "WV", "OH"],
    "NJ": ["NY", "DE", "PA"],
    "MA": ["VT", "NH", "RI", "CT", "NY"],
    "NH": ["ME", "MA", "VT"],
    "CA": ["OR", "NV", "AZ"],
    "AZ": ["UT", "NM", "CA", "NV"],
    "CO": ["WY", "NE", "KA", "OK", "NM", "UT"],
    "NE": ["SD", "IA", "MO", "KA", "CO", "WY"],
    "MO": ["IA", "IL", "KY", "TN", "AR", "OK", "KA", "NE"],
    "IN": ["IL", "MI", "OH", "KY"],
    "WV": ["PA", "MD", "VA", "KY", "OH"],
    "DE": ["NJ", "MD", "PA"],
    "CT": ["MA", "RI", "NY"],
    "RI": ["CT", "MA"],
    "NM": ["CO", "OK", "TX", "AZ"],
    "KA": ["NE", "MO", "OK", "CO"],
    "AR": ["MO", "TN", "MS", "LA", "TX", "OK"],
    "KY": ["OH", "WV", "VA", "TN", "MO", "IN"],
    "VA": ["WV", "MD", "DC", "NC", "TN", "KY"],
    "MD": ["DE", "DC", "VA", "WV", "PA"],
    "OK": ["KA", "MO", "AR", "TX", "NM", "CO"],
    "LA": ["AR", "MS", "TX"],
    "MS": ["TN", "AL", "LA", "AR"],
    "TN": ["KY", "VA", "NC", "GA", "AL", "MS", "AR", "MO"],
    "NC": ["VA", "SC", "GA", "TN"],
    "DC": ["MD", "VA"],
    "TX": ["OK", "AR", "LA", "NM"],
    "AL": ["MS", "TN", "GA", "FL"],
    "GA": ["TN", "NC", "SC", "FL", "AL"],
    "SC": ["NC", "GA"],
    "FL": ["GA", "AL"]
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

    def Paint(self):
        acol = set([0, 1, 2, 3, 4])
        ucol = set()
        for p in self.peers:
            if p.color != -1:
                ucol.add(p.color)

        acol -= ucol
        if len(acol) == 0:
            print("Not enough colors!!!")
            sys.exit(1)
        self.color = acol.pop()

        for p in self.peers:
            if p.color == -1:
                p.Paint()



def map_create():
    map = dict()
    # Пройти по MAP_NODES
    for mi in MAP_NODES:
        # Cоздать новый узел
        map[mi[0]] = Node(mi[0], mi[1], mi[2])
    
    # Пройти по MAP_LINKS 
    for n in MAP_LINKS:    
        # Связать узлы
        for ll in MAP_LINKS[n]:
            map[n].AddPeer(map[ll])

    return map
    


def get_cmap():
    """
    Creates colored map
    
    Return colored map of USA as Nodes dictionary
    """
    cmap = map_create()

    cmap["WA"].Paint()

    return cmap    