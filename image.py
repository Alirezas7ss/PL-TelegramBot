from PIL import Image, ImageDraw, ImageFont
from api import doge

font = ImageFont.truetype('temp/NotoSansJP-Medium.otf', size=50)
bg = Image.open('temp/dollar-tp.png')
white = (255, 255, 255)

def coin(api):
  if api[0] == 'DOGE':  
    doge = Image.open('temp/doge.png').resize((250, 250))
    bg.paste(doge, (180, 50), doge)
    draw = ImageDraw.Draw(bg)
    draw.text((240, 300), f'{api[0]}', font=font, fill=white)
    draw.text((710, 120), '%s' % (api[1]["price"]), font=font, fill=white)
    draw.text((1000, 120), '%s' % (api[1]["price_base"]), font=font, fill=white)
    draw.text((710, 270), '%s' % (api[2]["price"]), font=font, fill=white)
    draw.text((1000, 270), '%s' % (api[2]["price_base"]), font=font, fill=white)
    bg.save('image.jpg')

