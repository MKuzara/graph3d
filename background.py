from ursina import Entity, scene, color


class Background(Entity):

    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            color=color.color(201, .849, .337),
            scale=1000,
            double_sided=True
        )
