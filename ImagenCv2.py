import cv2

imagen = cv2.imread('logo.jpg',0) 
# La función imread de OpenCV carga una imagen del archivo especificado y la devuelve.
# puedes cambiar 'logo.jpg' por alguna imagen de tu preferencia
# el 0 cambia los colores a escala de grises, si se busca ver la imagen con los colores originales eliminar esta parte

cv2.imshow('Imagen', imagen)
# La función imshow de OpenCV muestra una imagen.
cv2.imwrite('grises.jpg',imagen)
#La función imwrite de OpenCV guarda la imagen.
cv2.waitKey(0)
cv2.destroyAllWindows()
