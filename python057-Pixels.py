from PIL import Image

imagen = Image.open("josevicente.jpg")
pixeles = imagen.load()
print(imagen.size)

print(pixeles[0,0])

pixeles[0,0] = (255,255,255)

imagen.save("josevicenteguardado.png")

