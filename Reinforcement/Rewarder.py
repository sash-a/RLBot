class Rewarder:
    def __init__(self, matrix_old, matrix_new, state):
        self.m_old = matrix_old
        self.m_new = matrix_new
        self.state = state

    def hit_ball(self):
        # towards goal?
        # save?
        # speed?

        # if !hit ball return
        # etc
        pass

    def scored(self):
        # opponent or self scored?
        # goal speed?
        pass

    def reward(self):
        # compare old matrix to new matrix and edit column values according to reward and difference between values
        pass
