import numpy as np


class Homography(object):
    def get_homography(self, points, points_):
        matrix_h = np.zeros((8, 8))
        for i in range(4):
            point = points[i]
            x = point[0]
            y = point[1]
            point_ = points_[i]
            x_ = point_[0]
            y_ = point_[1]
            index_a = i + i
            index_b = index_a + 1

            matrix_h[index_a, 0] = x
            matrix_h[index_a, 1] = y
            matrix_h[index_a, 2] = 1
            matrix_h[index_a, 6] = (-x) * x_
            matrix_h[index_a, 7] = (-y) * x_

            matrix_h[index_b, 3] = x
            matrix_h[index_b, 4] = y
            matrix_h[index_b, 5] = 1
            matrix_h[index_b, 6] = (-x) * y_
            matrix_h[index_b, 7] = (-y) * y_

        return matrix_h