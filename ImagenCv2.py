import cv2

imagen = cv2.imread('logo.jpg',0)

cv2.imshow('Imagen', imagen)
cv2.imwrite('grises.jpg',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()