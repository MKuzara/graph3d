from ursina import Entity, Vec3
from models.node import Node
from models.lines import Line


class Graph:
    
    def __init__(self, name='', nodes: list = []):
        self.name = name
        self._nodes = nodes
        self._name = 'graph1'
        self.lines = []

    def __str__(self):
        return self._name

    def append_node(self, node: Node):
        self._nodes.append(node)
    
    def add_relation(self, first, second):
        if first in self.nodes and second in self.nodes:
            self.lines.append(first.add_child(second))

    def node_exists(self, name):
        names = [node.name for node in self._nodes]
        if name in names:
            return True
        return False
    
    def filter_nodes(self, name):
        for node in self._nodes:
            if node.name == name:
                return node
        return False
    
    @property
    def nodes(self):
        return self._nodes

    def apply_forces(self):
        for node in self._nodes:
            node.zero_velocity()
        
        for node in self._nodes:
            node.apply_force(self._nodes)

        for node in self._nodes:
            node.update_position()
        
        for line in self.lines:
            line.update_verticies()

    