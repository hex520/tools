盲水印 by python

文件说明
bwm.py 程序文件
hui.png 无水印的原图
wm.png 水印图
hui_with_wm.png 有盲水印的图
wm_from_hui.png 反解出来的水印图

Demo
合成盲水印图:
python2 bwm.py encode 原图 水印图 产生有盲水印的图

提取图中的盲水印 (需要原图)
python2 bwm.py decode 原图.png 有盲水印的图.png 反解出来的水印图.png
