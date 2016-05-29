import matplotlib.pyplot as plt
from algorithm.Homography import Homography

point = [[128, 168], [566, 135], [579, 248], [121, 251]]
point_ = [[100, 100], [500, 100], [500, 200], [100, 200]]
homography = Homography("Imagenes/im01.jpg", point, point_)
original_image =homography.get_original()
image = homography.transform_image()

fig, (im1, im2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
im1.imshow(original_image, cmap=plt.cm.gray)
im2.imshow(image, cmap=plt.cm.gray)

fig.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)

plt.show()