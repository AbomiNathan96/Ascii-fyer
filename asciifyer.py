from PIL import Image
import io, os # librarys

ASCI = '@%#*+=-:. ' # characters to use

File = input('file name?')

def char(x,y):#turns a color value into text  linerly like: 0-50 > "#" 50-100 > " "
    for z in range(len(ASCI)):
        Z = z + 1 
        if img.getpixel((x,y)) < Z*(255/(1+len(ASCI))):
            return ASCI[z]+' '
    return'  '

txtfile = io.open(os.path.splitext(File)[0]+'.txt','w')

img = Image.open(File)

img = img.reduce(int(input('reduce?')))

img = img.convert('L')

Temp = ''
for y in range(img.height):
    for x in range(img.width):
        Temp = Temp + char(x,y)# turns each pixel into a text cahracter
    Temp = Temp + '\n'

txtfile.write(Temp)
txtfile.close()
