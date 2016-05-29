from algorithm.Homography import Homography
from skimage import io

point = [[155, 130], [250, 120], [105, 555], [250, 580]]
point_ = [[145, 120], [242, 120], [145, 480], [242, 480]]
homography = Homography("Imagenes/im01.jpg", point, point_)
image = homography.transform_image()
io.imsave("Imagenes/resultado_1_close.jpg", image)
image = homography.transform_image("bilineal")
io.imsave("Imagenes/resultado_1_bilineal.jpg", image)

