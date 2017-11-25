class Bot:
    def __init__(self, index, game_ticket):
        self.index = index
        car = game_ticket.gamecars[index]

        self.location = car.Location

        self.pitch = float(car.Rotation.Pitch)
        self.yaw = float(car.Rotation.Yaw)
        self.roll = float(car.Rotation.Roll)

        self.velocity = car.Velocity  # v3
        self.ang_velocity = car.AngularVelocity  # v3

        self.is_ground = car.bOnGround  # bool
        self.is_jump = car.bJumped  # bool
        self.is_double_jump = car.bDoubleJumped  # bool

        self.boost = car.Boost  # int

    def get_bot_matrix(self):
        return [self.location.X,
                self.location.Y,
                self.location.Z,
                self.pitch,
                self.yaw,
                self.roll,
                self.velocity.X,
                self.velocity.Y,
                self.velocity.Z,
                self.ang_velocity.X,
                self.ang_velocity.Y,
                self.ang_velocity.Z,
                self.is_ground,
                self.is_jump,
                self.is_double_jump,
                self.boost  # TODO opponents boost should not be visible
                ]
