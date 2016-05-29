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

        return matrix_ans

    def transform_image(self, interpolate="close"):
        height, width, layer = self.image.shape
        new_image = self.image.copy()
        new_image.fill(0)
        matrix_h = self.get_homography()

        if interpolate == "close":
            method = self.interpolate_close_neighbor
        else:
            method = self.interpolate_bi_lineal

        for y in range(height):
            for x in range(width):
                new_point = get_point([y, x], matrix_h)

                if new_point[1] >= width or new_point[1] < 0 or new_point[0] >= height or new_point[0] < 0:
                    continue

                new_value = method(new_point)
                if new_point != 0:
                    new_image[y, x] = new_value
        return new_image

    def interpolate_close_neighbor(self, position):
        height, width, layer = self.image.shape

        point = [int(position[0] + 0.5), int(position[1] + 0.5)]
        if point[1] >= width or point[1] < 0 or point[0] >= height or point[0] < 0:
            ans = 0
        else:
            ans = self.image[int(position[0] + 0.5), int(position[1] + 0.5)]
        return ans

    def interpolate_bi_lineal(self, position):
        height, width, layer = self.image.shape

        p = int(position[0]) % height
        pnext = (p + 1) % height
        q = int(position[1]) % width
        qnext = (q + 1) % width

        a = position[0] - p
        b = position[1] - q

        ans = (1 - a) * ((1 - b) * self.image[p, q] + b * self.image[p, qnext]) + \
              a * ((1 - b) * self.image[pnext, q] + b * self.image[pnext, qnext])

        return ans


def get_point(final_point, H):
    upper = (final_point[0] - H[0, 2] - (H[0, 1] - H[2, 1] * final_point[0]) *
             (final_point[1] - H[1, 2]) / (H[1, 1] - H[2, 1] * final_point[1])) * 1.0

    bottom = (H[0, 0] - H[2, 0] * final_point[0] - (H[0, 1] - H[2, 1] * final_point[0]) *
              (H[1, 0] - H[2, 0] * final_point[1]) / (H[1, 1] - H[2, 1] * final_point[1])) * 1.0
    x = upper / bottom
    y = ((final_point[1] - H[1, 2] - x *
          (H[1, 0] - H[2, 0] * final_point[1])) / (H[1, 1] - H[2, 1] * final_point[1])) * 1.0

    return [x, y]

