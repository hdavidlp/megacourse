import cv2
import glob

base_dir = 'sample_images/'
output_dir = 'output_images/'

images=glob.glob(base_dir + "*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite(output_dir + "resized_" + image,re)