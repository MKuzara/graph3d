from ursina import Entity, Vec3, Mesh


class Line(Entity):
    
    def __init__(self, start: Vec3, end: Vec3):
        self.start = start
        self.end = end
        
        self.mesh = Mesh(
            vertices=[start.entity.position, end.entity.position],
            mode='line',
            static=False
        )
        super().__init__(
            model=self.mesh)
    
    def update_verticies(self):
        self.mesh.vertices = [
            self.start.entity.position,
            self.end.entity.position
        ]
        self.mesh.generate()

