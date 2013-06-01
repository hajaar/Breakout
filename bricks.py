__author__ = 'kartikn'

import pygame


class Brick(pygame.Rect):
    def __init__(self, left, top, width, height, window_width, window_height):
        super(Brick, self).__init__(left, top, width, height)
        self.window_width = window_width
        self.window_height = window_height
        self.coefficient_of_restitution = 0
        self.type = 0
        self.x_vel = 0
        self.y_vel = 0
        self.color = (0, 0, 0)
        self.line_width = 0
        self.warp = False

    def updatePosition(self):
        self.left += self.x_vel
        self.top += self.y_vel
        self.boundaryConditions()

    def boundaryConditions(self):
        if self.warp:
            if self.left <= 0 or self.right >= self.window_width:
                self.x_vel = -self.x_vel
            if self.top <= 0 or self.bottom >= self.window_height:
                self.y_vel = -self.y_vel
        else:
            if self.left == 0 and self.x_vel < 0:
                self.left = self.window_width
            if self.right == self.window_width and self.x_vel > 0:
                self.right = 0
            if self.top == 0 and self.y_vel < 0:
                self.top = self.window_height
            if self.bottom == self.window_height and self.y_vel > 0:
                self.bottom = 0

    def bounceSelf(self, brick_list):
        for brick in brick_list:
            if self.collidelist(brick_list):
                self.x_vel = -self.x_vel
                self.y_vel = -self.y_vel

