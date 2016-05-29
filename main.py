from algorithm.Homography import Homography
from skimage import io

images = [
    ["Images/im01.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]]
]
for image in images:
    homography = Homography(image[0], image[1], image[2])
    img = homography.transform_image()
    io.imsave(image[0]+"_close.jpg", img)
    img = homography.transform_image("bilineal")
    io.imsave(image[0] + "_bilineal.jpg", img)
