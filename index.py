import pytesseract      
from PIL import Image    

 # opening an image from the source path
img = Image.open('text.jpg')     
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'   
result = pytesseract.image_to_string(img)   
# write text in a text file and save it to source path   
with open('abc.txt',mode ='w') as file:     
      
                 file.write(result)
                 print(result)
