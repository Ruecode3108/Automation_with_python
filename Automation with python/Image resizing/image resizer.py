from PIL import Image
#load image
input_path="moon_emoji.jfif"
output_path="moon_emoji.jfif"
new_size=(300,300)

img=Image.open(input_path)
resized_img=img.resize(new_size)
resized_img.save(output_path)
print("Image resized successfully!")