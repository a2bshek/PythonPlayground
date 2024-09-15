#Importing required packages
from PIL import Image, ImageFont, ImageDraw
import pandas

#Font File (Change the path of font file anf teh font size)
font_ttf = ImageFont.truetype(r'font.ttf', 70)
#font color
font_color = "#000"
#Set the coordinates of the name to be printed
w,h = 1350, 865

#Function to generate certificate
def generate_Certificates(name):
    
    #Template to print names
    temp = Image.open(r'template.png')
    draw = ImageDraw.Draw(temp)
    name_width, name_height = draw.textsize(name, font=font_ttf)
    draw.text((w-name_width/2, h-name_height/2), name, fill=font_color, font=font_ttf)
    temp.save("./Cert/" + name+".png")
    print(name+' - Successfully printed')

data = pandas.read_excel("./names.xlsx")
names = list(data.Name)
for i in names:
    generate_Certificates(i)
