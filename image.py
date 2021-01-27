"""
Loads and displays image. 

v. 2021 01 27

"""

image = pa.loadim(image_path)

print('displaying image file: ' + image_path)
print('image dimensions: {} '.format(image.shape))

pa.showimage(image,image_file)

