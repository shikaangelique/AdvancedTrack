gravity = 0.0001

class QueenSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.target_position = target_posn
        (x, y) = target_posn
        self.position = (x, 0)
        self.y_velocity = 0

    def update(self):
        self.y_velocity += gravity
        (x, y) = self.position
        new_y_pos = y + self.y_velocity

        (target_x, target_y) = self.target_position
        dist_to_go = target_y - new_y_pos

        if dist_to_go < 0:
            self.y_velocity = -0.65*self.y_velocity
            new_y_pos = target_y + dist_to_go

        self.position = (x, new_y_pos)
        return

    def draw(self, target_surface):
        target_surface.blit(self.image, self.position)

    def contains_point(self, point):
        (my_x, my_y) = self.position
        my_width = self.image.get_width()
        my_height = self.image.get_height()
        (x, y) = point
        return (my_x <= x < my_x + my_width and
                my_y <= y < my_y + my_height)

    def handle_click(self):
        self.y_velocity += -0.3



