import numpy as np
from skimage import io


class Homography:

    def __init__(self, image, points, points_):
        self.image = io.imread(image)
        self.points = points
        self.points_ = points_

    def get_original(self):
        return self.image

    def get_homography(self):
        matrix_a = np.zeros((8, 8))
        for i in range(4):
            point = self.points[i]
            x = point[0]
            y = point[1]
            point_ = self.points_[i]
            x_ = point_[0]
            y_ = point_[1]
            index_a = i + i
            index_b = index_a + 1

            matrix_a[index_a, 0] = x
            matrix_a[index_a, 1] = y
            matrix_a[index_a, 2] = 1
            matrix_a[index_a, 6] = (-x) * x_
            matrix_a[index_a, 7] = (-y) * x_

            matrix_a[index_b, 3] = x
            matrix_a[index_b, 4] = y
            matrix_a[index_b, 5] = 1
            matrix_a[index_b, 6] = (-x) * y_
            matrix_a[index_b, 7] = (-y) * y_

        array_b = np.zeros((8, 1))
        array_b[0, 0] = self.points_[0][0]
        array_b[1, 0] = self.points_[0][1]
        array_b[2, 0] = self.points_[1][0]
        array_b[3, 0] = self.points_[1][1]
        array_b[4, 0] = self.points_[2][0]
        array_b[5, 0] = self.points_[2][1]
        array_b[6, 0] = self.points_[3][0]
        array_b[7, 0] = self.points_[3][1]

        array_x = np.linalg.solve(matrix_a, array_b)

        matrix_ans = np.zeros((3, 3))
        matrix_ans[0, 0] = array_x[0, 0]
        matrix_ans[0, 1] = array_x[1, 0]
        matrix_ans[0, 2] = array_x[2, 0]

        matrix_ans[1, 0] = array_x[3, 0]
        matrix_ans[1, 1] = array_x[4, 0]
        matrix_ans[1, 2] = array_x[5, 0]

        matrix_ans[2, 0] = array_x[6, 0]
        matrix_ans[2, 1] = array_x[7, 0]
        matrix_ans[2, 2] = 1

        print matrix_a
        print array_b
        print array_x

        return matrix_ans

    def transform_image(self, interpolate="close"):
        print self.image.shape
        height, width, layer = self.image.shape
        new_image = np.zeros(self.image.shape)
        matrix_h = self.get_homography()

        if interpolate == "close":
            method = interpolate_close_neighbor
        else:
            method = interpolate_bi_lineal

        for x in range(height):
            for y in range(width):
                point = np.zeros((3, 1))
                point[0, 0] = x
                point[1, 0] = y
                point[2, 0] = 1
                new_point = np.dot(matrix_h, point)
                new_point = [new_point[0, 0], new_point[1, 0]]
                new_point = method(new_point, self.image)
                if x == 168 and y == 128:
                    print point
                    print new_point
                if new_point[0] >= height or new_point[1] >= width:
                    continue
                for z in range(layer):
                    new_image[new_point[0], new_point[1], z] = self.image[x, y, z]

        return new_image


def interpolate_close_neighbor(position, matrix):
    return [int(position[0]), int(position[1])]


def interpolate_bi_lineal(position, matrix):
    return position


def fix_precision(matrix):
    ans = matrix.astype(np.float16)
    ans = ans.astype(np.uint8)
    return ans
