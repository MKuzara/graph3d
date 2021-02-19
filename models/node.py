from ursina import Entity, color, Vec3, time, ursinamath
import math
from .lines import Line


FORCE = 200
MIN_DISTANCE = 20

class NodeEntity(Entity):

    def __init__(self, position=(1, 1, 1)):
        super().__init__(model='sphere',
                         color=color.white,
                         position=Vec3(position))
        
    def apply_force(self, parent, nodes=[]):
        '''
        (connected)    pulling force - distance * log10( distance / desired_distance )\n
        (disconnected) pushing force - min_connected_node_distance / distance^2 * dt * difference.normalized
        '''
        global FORCE
        temp = FORCE * len(parent.children)
        for node in parent.children:
            difference = self.position - node.entity.position
            distance = self.calc_distance(difference)

            
            if distance > 100:
                temp = distance / 10
            try:
                force = temp * math.log10(distance / 5)
            except ValueError as err:
                print(err)
            node.entity.velocity = node.entity.velocity + \
                self.calc_velocity(force, difference)
        temp = FORCE * len(parent.children)
        # pushing force nodes
        for node in nodes:
            if node == parent:
                continue
            # difference Vec3
            difference = self.position - node.entity.position
            # distance float
            distance = self.calc_distance(difference)
            if distance != 0:
                if distance < MIN_DISTANCE:
                    # force = min_distance / distance^2
                    temp = MIN_DISTANCE / math.pow(distance, 2) 
                
                # applied_force = force / distance^2
                applied_force = temp / math.pow(distance, 2) * 2
                # velocity = applied_force * dt * diff.normalized
                node.entity.velocity = node.entity.velocity - \
                    self.calc_velocity(applied_force, difference)

            FORCE = temp

    def update_position(self):
        self.position = self.position + self.velocity
    
    def calc_distance(self, difference):
        return math.sqrt(
                math.pow(difference.x, 2) + \
                math.pow(difference.y, 2) + \
                math.pow(difference.z, 2)
            )
    
    def calc_velocity(self, force, difference):
        return Vec3(
                force * time.dt * difference.normalized().x,
                force * time.dt * difference.normalized().y,
                force * time.dt * difference.normalized().z,
            )


class Node:

    def __init__(self, name, graph, position = (1, 1, 1), children=[]):
        self._name = name
        self.entity = NodeEntity(
            position=Vec3(position))
        graph.append_node(self)
        self._graph = graph,
        self.velocity = Vec3.zero()
        self.children = []
    
    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def graph(self):
        return self._graph

    
    @graph.setter
    def graph(self, value):
        self._graph = value
    
    def add_child(self, node):
        if node not in self.children \
                and self not in node.children:
            self.children.append(node)
            node.children.append(self)
            line = Line(self, node)
            return line
    
    def apply_force(self, nodes):
        self.entity.apply_force(self, nodes)
    
    def update_position(self):
        self.entity.update_position()
    
    def zero_velocity(self):
        self.entity.velocity = Vec3.zero()
    