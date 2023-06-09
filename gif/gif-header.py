from PIL import Image, ImageSequence

# Crea una lista con las imágenes individuales que se utilizarán para crear el GIF
frames = []

# Agrega las imágenes a la lista (asegúrate de que todas las imágenes tengan el mismo tamaño)
frames.append(Image.open('holamundo.png'))
frames.append(Image.open('helloworld.png'))
frames.append(Image.open('hallowelt.jpg'))


frames[0].save('animacion.gif', format='GIF', append_images=frames[1:], save_all=True, duration=200, loop=0)
