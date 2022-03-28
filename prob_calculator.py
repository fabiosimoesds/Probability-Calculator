import random
import copy

class Hat():

    def __init__(self, **hats):
        self.repla_copy = list()
        self.contents = list()
        for keys, values in hats.items():
            for colour in range(0, values):
                self.contents.append(keys)

    def draw(self, num_draws):
        draw_balls = list()
        if num_draws <= len(self.contents):
            for rounds in range(0, num_draws):
                draw_ball = random.choice(self.contents)
                draw_balls.append(draw_ball)
                self.contents.remove(draw_ball)
            self.repla_copy = copy.copy(draw_balls)

            return draw_balls
        else:
            return self.contents

    def replace(self):
        for items in self.repla_copy:
            self.contents.append(items)






def experiment(hat='', expected_balls={}, num_balls_drawn=0, num_experiments=0):
    counter = 0
    for exper in range(1, num_experiments+1):
        occu = 0
        rand_draw = hat.draw(num_balls_drawn)
        for keys, value in expected_balls.items():
            ball_count = rand_draw.count(keys)
            if occu == 0:
                if value <= ball_count:
                    counter = 1/len(expected_balls) + counter
                    occu = 1
                else:
                    break
            else:
                if value <= ball_count:
                    counter = 1/len(expected_balls) + counter
                    occu += 1
                else:
                    counter = counter - occu/len(expected_balls)
                    break
        hat.replace()

    return counter/num_experiments