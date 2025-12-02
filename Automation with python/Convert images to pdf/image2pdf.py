import img2pdf

#list of the images
image_files=[
    'a.png',
     'b.jpeg'
     ]
#Ouput pdf file
output_name=input("Enter the desired pdf filename (without.pdf):")
output_pdf=f"{output_name}.pdf"

#convert and save
with open(output_pdf,'wb') as f:
    f.write(img2pdf.convert(image_files))
    print(f"PDF has been saved")