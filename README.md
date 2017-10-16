# Image Resizer

Script to resize image and save output


#### Run script:
```
python image_resize.py [-h] [-width WIDTH] [-height HEIGHT] [-scale SCALE] [-output OUTPUT] filename

```
| Argument         | Description                   | 
|----------------- | ----------------------------- | 
| -width WIDTH:    | Width of the output picture   |  
| -height HEIGHT:  | Height of the output picture  |  
| -scale SCALE:    | Scale of the output picture   |  
| -output OUTPUT:  | Name of the output image file |  

WIDTH and/or HEIGHT should not be use simultaneously with SCALE

#### Output:

``Result image is saved <filename>``

Where `<filename>` is output filename

#### Run script example:
```
python image_resize.py pic.jpg -width 100 -height 200 pic_result.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
