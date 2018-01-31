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
    "WA": ["OR", "ID"],
    "ID": ["WA", "MT", "WY", "UT", "NV", "OR"],
    "MT": ["ID", "WY", "SD", "ND",],
    "ND": ["MT", "SD", "MN"],
    "MN": ["ND", "SD", "IA", "WI"],
    "WI": ["MN", "IA", "MI", "IL"],
    "MI": ["WI", "OH", "IN"],
    "NY": ["PA", "CT", "NJ", "MA", "VT"],
    "VT": ["NY", "NH", "MA"],
    "ME": ["NH"],
    "OR": ["WA", "CA", "ID", "NV"],
    "NV": ["OR", "UT", "ID", "CA", "AZ"],
    "UT": ["NV", "WY", "CO", "AZ", "ID"],
    "WY": ["SD", "NE", "CO", "UT", "MT", "ID"],
    "SD": ["WY", "NL", "ND", "MT", "MN", "IA"],
    "IA": ["MN", "WI", "IL", "MO", "NE", "SD"],
    "IL": ["WI", "IA", "MO", "IN"],
    "OH": ["IN", "MI", "KY", "PY", "WV"],
    "PA": ["OH", "WV", "DE", "MD", "NJ", "NY"],
    "NJ": ["PA", "DE", "NY"],
    "MA": ["CT", "NY", "VT", "NH", "RI"],
    "NH": ["MA", "VT", "ME"],
    "CA": ["OR", "NV", "AZ"],
    "AZ": ["NM", "CA", "NV", "UT"],
    "CO": ["UT", "WY","NE", "KA", "OK", "NM"],
    "NE": ["CO", "KA", "MO", "IA", "SO", "WY"],
    "MO": ["IA", "AR", "NE", "IE", "TN", "KY", "KA", "OK"],
    "IN": ["IL", "MI", "OH", "KY"],
    "WV": ["PA", "OH", "MD", "WA", "KY"],
    "DE": ["NJ", "PA", "MD"],
    "CT": ["NY", "MA", "RI"],
    "RI": ["CT", "MA"],
    "NM": ["AZ", "CO", "OK", "TX"],
    "KA": ["OK", "NE", "CO", "MO"],
    "AR": ["LA", "OK", "MO", "TX", "MS", "TN"],
    "KY": ["IN", "MO", "WV", "VA", "TN"],
    "VA": ["NC", "TN", "DC", "MD", "MV", "KY"],
    "MD": ["VA", "DC", "DE", "WV"],
    "OK": ["NM", "TX", "KA", "AR", "CO", "MO"],
    "LA": ["AR", "TX", "MB"],
    "MS": ["TN", "AR", "LA", "AL"],
    "TN": ["AL", "MS", "AR", "GA", "NC", "VA", "KY", "MO"],
    "NC": ["SC", "GA", "AR", "LA"],
    "DC": ["VA", "MD"],
    "TX": ["NM", "OK", "AR", "AL"],
    "AL": ["MS", "TN", "GA", "FL"],
    "GA": ["AL", "TN", "NC", "SC", "FL"],
    "SC": ["GA", "NC"],
    "FL": ["AL", "GA"]
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
    