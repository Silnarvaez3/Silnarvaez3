from PIL import Image, ImageSequence

# Crea una lista con las imágenes individuales que se utilizarán para crear el GIF
frames = []


# Tamaño deseado para las imágenes (ancho, alto)
size_deseado = (300, 300)


# Agrega las imágenes a la lista después de redimensionarlas al tamaño deseado
imagen1 = Image.open('holamundo.png').resize(size_deseado)
imagen2 = Image.open('helloworld.png').resize(size_deseado)
imagen3 = Image.open('hallowelt.jpg').resize(size_deseado)

frames.append(imagen1)
frames.append(imagen2)
frames.append(imagen3)





frames[0].save('animacion.gif', format='GIF', append_images=frames[1:], save_all=True, duration=500, loop=0)
