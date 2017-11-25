import numpy as np
from Reinforcement.Bot import Bot as bot


class GameInfo:
    def __init__(self, game_ticket, index):
        # ball info
        ball = game_ticket.gameball
        self.ball_loc = ball.Location
        self.ball_vel = ball.Velocity
        self.ball_ang_vel = ball.AngularVelocity
        self.ball_accel = ball.Acceleration

        # player info
        self.player = bot(index, game_ticket)

        # opponent info
        opponent_index = 0  # index can only be 0/1
        if index == 0:
            opponent_index = 1

        self.opponent = bot(opponent_index, game_ticket)

    def get_input_matrix(self):
        ball_lst = [self.ball_loc.X,
                    self.ball_loc.Y,
                    self.ball_loc.Z,
                    self.ball_vel.X,
                    self.ball_vel.Y,
                    self.ball_vel.Z,
                    self.ball_ang_vel.X,
                    self.ball_ang_vel.Y,
                    self.ball_ang_vel.Z,
                    self.ball_accel.X,
                    self.ball_accel.Y,
                    self.ball_accel.Z]

        all_lst = ball_lst + self.player.get_bot_matrix() + self.opponent.get_bot_matrix()
        return np.array(all_lst)
