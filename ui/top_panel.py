from ursina import Entity, camera, Quad, color, Button


class TopPanel(Entity):
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,
            model = Quad(radius=.01),
            scale = (1.475, .06),
            origin = (0, 0),
            position = (0.15,.47),
            color = color.color(0,0,.1,1),
        )

        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.play_button = PlayButton(self)


class PlayButton(Button):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(
            parent=parent,
            text='Start',
            model='quad',
            color=color.azure,
            origin=(4.45, 0),
            scale=(.1, .7),
        )

    def on_click(self):
        self.text = 'Pause' if self.text == 'Start' else 'Start'

            