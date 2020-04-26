from PIL import Image
import os
import bitstring

image_name = 'flag.jpg'
current_path = os.path.dirname(__file__)
with open(os.path.join(current_path,image_name),'rb') as f:
        bin_content = bitstring.Bits(f)
        im = Image.new("RGB",(1024,780),(255,0,0))
        pim = im.load()
        for i,val in enumerate(bin_content.bin):
            if val == '0':
                pim[i%1024,i/1024] = (0,255,0)
        im.save(os.path.join(current_path,'red_green.png'))
