from ursina import *
from models.graph import Graph
from models.node import Node
from models.lines import Line
from ui.left_panel import LeftPanel
from ui.top_panel import TopPanel
from background import Background
from parsers.parsers import DotBaseParser

NUM = 1000000000

app = Ursina()

from camera import Player


from ursina.prefabs.first_person_controller import FirstPersonController

def update():
    graph.apply_forces()

Background()
ec = Player(rotation_smoothing=2, enabled=True, rotation=(0,0,0))    
LeftPanel()
TopPanel()
    

parser = DotBaseParser()
graph = parser.parse()

app.run()