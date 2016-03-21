Selenized color coordinates
===========================

LAB values are canonical.  RGB values (both sRGB and Apple RGB) are calculated
from LAB using `utils/convert-lab-palette-to-rgbs.py` script, which employs
`python-colormath` library for color space transformations.


Selenized medium
----------------

![Selenized medium screenshot](http://i.imgur.com/5qpQRPe.png)

```
Color        CIE L*a*b*   sRGB      Apple RGB
----------   ----------   -------   ---------
bg           28  -7 -16   #27465a   #1f3649
black        38  -7 -16   #3f5e73   #324b60
br_black     63  -7 -16   #7e9db5   #6d8ca6
fg           78  -4  -9   #b2c4d1   #a4b7c7
white        78  -4  -9   #b2c4d1   #a4b7c7
br_white     88  -4  -9   #cee0ee   #c4d8ea

red          63  66  44   #ff594f   #ff3e3d
green        72 -40  54   #79c344   #6eb92b
yellow       77   6  65   #e1b83c   #d7aa25
blue         64   4 -59   #5d9cff   #4d89ff
magenta      68  58 -46   #ea79fb   #de5dfd
cyan         76 -40  -4   #4cd0c1   #4bc8b4

br_red       68  66  44   #ff685b   #ff4c48
br_green     77 -40  54   #87d151   #7cca38
br_yellow    82   6  65   #f0c64a   #eaba31
br_blue      69   4 -59   #6daaff   #5c98ff
br_magenta   73  58 -46   #f987ff   #f06cff
br_cyan      81 -40  -4   #5cdecf   #59d9c4
```



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/fhYxsbD.png)

```
Color        CIE Lab      sRGB      Apple RGB
----------   ----------   -------   ---------
bg           15  -7 -15   #07293b   #0a1f2d
black        25  -7 -15   #213f52   #1a3041
br_black     50  -7 -15   #5d7b90   #4d687e
fg           65  -4  -9   #90a0ae   #7e8f9e
white        65  -4  -9   #90a0ae   #7e8f9e
br_white     75  -4  -9   #aabbc9   #9badbe

red          50  66  44   #dd3031   #ce1725
green        59 -40  54   #559f1e   #4b9008
yellow       64   6  65   #ba9610   #aa8400
blue         51   4 -59   #2d7bdf   #2566db
magenta      55  58 -46   #c455d5   #b13bcf
cyan         63 -40  -4   #12ab9e   #269e8c

br_red       55  66  44   #ed413d   #e1272e
br_green     64 -40  54   #63ad2d   #58a018
br_yellow    69   6  65   #c9a323   #bb920e
br_blue      56   4 -59   #4188ee   #3573ec
br_magenta   60  58 -46   #d363e3   #c248e0
br_cyan      68 -40  -4   #2eb9ab   #34ad9b
```



Selenized black
---------------

![Selenized black screenshot](http://i.imgur.com/rec8DZu.png)

```
Color        CIE L*a*b*   sRGB      Apple RGB
----------   ----------   -------   ---------
bg           10   0   0   #1b1b1b   #151515
black        20   0   0   #303030   #242424
br_black     55   0   0   #848484   #717171
fg           70   0   0   #ababab   #9b9b9b
white        70   0   0   #ababab   #9b9b9b
br_white     80   0   0   #c6c6c6   #bababa

red          55  66  44   #ed413d   #e1272e
green        64 -40  54   #63ad2d   #58a018
yellow       69   6  65   #c9a323   #bb920e
blue         56   4 -59   #4188ee   #3573ec
magenta      60  58 -46   #d363e3   #c248e0
cyan         68 -40  -4   #2eb9ab   #34ad9b

br_red       63  66  44   #ff594f   #ff3e3d
br_green     72 -40  54   #79c344   #6eb92b
br_yellow    77   6  65   #e1b83c   #d7aa25
br_blue      64   4 -59   #5d9cff   #4d89ff
br_magenta   68  58 -46   #ea79fb   #de5dfd
br_cyan      76 -40  -4   #4cd0c1   #4bc8b4
```

