from ursina import Entity, camera, Quad, color, Button
from .file_browser import FileBrowser

class LeftPanel(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.015),
            scale = (0.3, 1),
            origin = (0, 0),
            position = (-.74,0),
            color = color.color(0,0,.1,1),
        )

        for key, value in kwargs.items():
            setattr(self, key, value)
        self.load_button = LoadButton(self)


class LoadButton(Button):

    def __init__(self, parent, *args, **kwargs):
        self.file_browser = None
        super().__init__(
            parent=parent,
            text='Load File',
            model='quad',
            color=color.azure,
            highlight_color = self.color.tint(.2),
            pressed_color = self.color.tint(-.2),
            origin=(0, -10.4),
            scale=(0.94, .045),
        )
    
    def on_click(self):
        self.file_browser = FileBrowser(file_types=('.dot'), enabled=True)
