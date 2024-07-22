from PIL import Image

filename = r"datasets/VOC/JPEGImages/01_open_circuit_04.jpg"
img = Image.open(filename)
print(img.format)
