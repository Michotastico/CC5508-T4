from algorithm.Homography import Homography
from skimage import io

images = [
    ["Images/im01.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im02.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im03.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im04.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im05.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im06.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im07.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im08.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im09.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

    ["Images/im10.jpg",
     [[155, 130], [250, 120], [105, 555], [250, 580]],
     [[145, 120], [242, 120], [145, 480], [242, 480]]],

]
for image in images:
    print "Applying on image: ", image[0]
    homography = Homography(image[0], image[1], image[2])
    img = homography.transform_image()
    io.imsave(image[0]+"_close.jpg", img)
    img = homography.transform_image("bilineal")
    io.imsave(image[0] + "_bilineal.jpg", img)
