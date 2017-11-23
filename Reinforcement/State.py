import numpy as np

class Location(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_np(self):
        return np.array([self.x, self.y, self.z])
        # add functionality as need


class GameInfo(object):
    def __init__(self, game_ticket, index):
        # ball info
        self.game_ticket = game_ticket
        self.ball_loc = Location(game_ticket.gameball.Location.X,
                                 game_ticket.gameball.Location.Y,
                                 game_ticket.gameball.Location.Z)

        # player info
        self.p_index = index

        self.p_pitch = float(game_ticket.gamecars[index].Rotation.Pitch)
        self.p_yaw = float(game_ticket.gamecars[index].Rotation.Yaw)

        p_y = game_ticket.gamecars[index].Location.Y
        p_x = game_ticket.gamecars[index].Location.X
        p_z = game_ticket.gamecars[index].Location.Z
        self.p_loc = Location(p_x, p_y, p_z)

        # opponent info
        self.o_index = 0  # index can only be 0/1
        if index == 0:
            self.o_index = 1

        self.o_pitch = float(game_ticket.gamecars[self.o_index].Rotation.Pitch)
        self.o_yaw = float(game_ticket.gamecars[self.o_index].Rotation.Yaw)

        o_y = game_ticket.gamecars[self.o_index].Location.Y
        o_x = game_ticket.gamecars[self.o_index].Location.X
        o_z = game_ticket.gamecars[self.o_index].Location.Z
        self.o_loc = Location(o_x, o_y, o_z)

    def get_state_vector(self):
        return np.array([self.ball_loc,
                         self.p_loc,
                         self.p_pitch,
                         self.p_yaw,
                         self.o_loc,
                         self.o_pitch,
                         self.o_yaw])
