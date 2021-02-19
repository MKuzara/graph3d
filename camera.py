from ursina import held_keys, Vec3, time, mouse
from ursina.prefabs.editor_camera import EditorCamera



class Player(EditorCamera):

    MOVE_SPEED = 4
    FAST_MOVE_SPEED = 12
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        '''
        Free camera for ursina engine.
        Controls:\n
        w - move forward\n
        s - move back\n
        a - move left\n
        d - move right\n
        shift - move up\n
        ctrl - move down\n
        space (hold) - fast mode\n
        To rotate camera hold RMB (Right Mouse Button)
        '''
        fast_mode = True if held_keys['space'] else False
        move_speed = self.FAST_MOVE_SPEED if fast_mode else self.MOVE_SPEED
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
        ).normalized()

        if held_keys['shift']:
            vertical = Vec3.up()
        elif held_keys['control']:
            vertical = Vec3.down()
        else:
            vertical = Vec3.zero()

        self.position += self.direction * move_speed * time.dt
        self.position += vertical * move_speed * time.dt

        if mouse.right:
            self.rotation_x -= mouse.velocity[1] * self.rotation_speed
            self.rotation_y += mouse.velocity[0] * self.rotation_speed