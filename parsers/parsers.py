import io
from models.graph import Graph
from models.node import Node
from random import randint
from parsers.generators import BaseGraphGenerator

class DotBaseParser:

    def __init__(self, data=None):
        gen = BaseGraphGenerator(50)
        gen.generate()
        with open('generated.dot', 'r') as f:
            data = f.read()
        self.data = data

    def parse(self):
        nodes = []
        name, data = self.data.split('{')
        graph = Graph(name=name.strip())
        
        data = data.strip('}')
        data = data.split('\n')
        
        for line in data:
            if len(line) < 4:
                continue
            a, b = line.split('--')
            n1 = graph.filter_nodes(a.strip())
            n2 = graph.filter_nodes(b.strip())
            if not n1:
                n1 = Node(name=a.strip(),
                        graph=graph,
                        position=(
                            randint(0,50), 
                            randint(0,50), 
                            randint(0,50)))
            if not n2:
                n2 = Node(name=b.strip(),
                    graph=graph,
                    position=(
                        randint(0,50), 
                        randint(0,50), 
                        randint(0,50)))
            graph.add_relation(n1, n2)
        
        print('Done :)')
        return graph

            