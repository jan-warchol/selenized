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
bg           25 -10 -16   #154053   #143242
black        35 -12 -19   #245970   #1f475e
br_black     60  -7  -9   #7c95a0   #6b838f
fg           75  -6  -6   #a8bcc3   #99afb7
white        75  -6  -6   #a8bcc3   #99afb7
br_white     85  -6  -6   #c4d8df   #b9cfd8

red          61  63  40   #fc5851   #f33e3f
green        69 -37  53   #78b93e   #6bae27
yellow       74   6  65   #d8b033   #cda11d
blue         61   0 -55   #4e97f5   #4183f5
magenta      65  59 -21   #f16dc5   #e652bb
cyan         73 -40  -4   #41c7b9   #42beaa

br_red       66  63  40   #ff675d   #ff4c4a
br_green     74 -37  53   #85c74c   #79be33
br_yellow    79   6  65   #e7be42   #dfb02a
br_blue      66   0 -55   #5ea4ff   #4f92ff
br_magenta   70  59 -21   #ff7bd3   #f960cc
br_cyan      78 -40  -4   #52d5c7   #50ceba
```



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/fhYxsbD.png)

```
Color        CIE L*a*b*   sRGB      Apple RGB
----------   ----------   -------   ---------
bg           15  -8 -13   #072938   #0b1f2b
black        25 -10 -16   #154053   #143242
br_black     50  -7  -9   #637b86   #526873
fg           65  -6  -6   #8ea1a8   #7d9098
white        65  -6  -6   #8ea1a8   #7d9098
br_white     75  -6  -6   #a8bcc3   #99afb7

red          51  63  40   #dc3a3a   #cd222c
green        59 -37  53   #5c9e21   #518f0d
yellow       64   6  65   #ba9610   #aa8400
blue         51   0 -55   #267dd8   #2268d2
magenta      55  59 -21   #d451aa   #c3379c
cyan         63 -40  -4   #12ab9e   #269e8c

br_red       56  63  40   #ec4946   #e03035
br_green     64 -37  53   #6aac30   #5e9e1b
br_yellow    69   6  65   #c9a323   #bb920e
br_blue      56   0 -55   #3c8ae6   #3276e3
br_magenta   60  59 -21   #e25fb8   #d444ab
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

red          56  63  40   #ec4946   #e03035
green        64 -37  53   #6aac30   #5e9e1b
yellow       69   6  65   #c9a323   #bb920e
blue         56   0 -55   #3c8ae6   #3276e3
magenta      60  59 -21   #e25fb8   #d444ab
cyan         68 -40  -4   #2eb9ab   #34ad9b

br_red       64  63  40   #ff6158   #ff4646
br_green     72 -37  53   #80c246   #74b72e
br_yellow    77   6  65   #e1b83c   #d7aa25
br_blue      64   0 -55   #589efe   #4a8cff
br_magenta   68  59 -21   #fa76ce   #f15ac5
br_cyan      76 -40  -4   #4cd0c1   #4bc8b4
```

