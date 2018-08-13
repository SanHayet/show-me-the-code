from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageFilter

def add_num(img):
    draw = ImageDraw.Draw(img)
    #设置字体
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=150)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-100, 10), '5', font=myfont, fill=fillcolor)
    img.save('aobb.jpg', 'jpeg')
    #print(width, height)
    return 0

if __name__ == '__main__':
    image = Image.open('aob.jpg')
    add_num(image)
