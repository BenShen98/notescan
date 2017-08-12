import zbar
from PIL import Image
import cv2
import numpy
from func import *


im=cv2.imread('cache/t15.jpg')
# im=cv2.imread('cache/page_0.jpg')

# im=cv2.imread('cache/page-0.jpg')


image=cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)


ret,image=cv2.threshold(image,127,255,0)

# viewPage(image)

scanner=zbar.Scanner()

results=scanner.scan(image)

print(results)

# for result in results:
#     print(1)
#     print(result.type, result.data, result.quality, result.position)
#     for point in result.position:
#         cv2.circle(image, point, 5, (0, 0, 255), -1)
#         viewPage(image)
