from algorithm.Homography import Homography

homography = Homography()

print homography.get_homography([[-1,-1],[1,1],[3,3],[-3,-3]], [[2,2], [2,2], [2,2], [2,2]])