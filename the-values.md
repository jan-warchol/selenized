Selenized color coordinates
===========================

LAB values are canonical.  RGB values (both sRGB and Apple RGB) are calculated
from LAB using `utils/convert-lab-palette-to-rgbs.py` script, which employs
`python-colormath` library for color space transformations.


Selenized medium
----------------

![Selenized medium screenshot](http://i.imgur.com/NI8RQaT.png)

```
Color        CIE L*a*b*   sRGB      AppleRGB  HSB
----------   ----------   -------   --------  -----------
bg           25 -10 -16   #154053   #143242   198  74  33
black        35 -12 -19   #245970   #1f475e   199  68  44
br_black     60  -7  -9   #7c95a0   #6b838f   199  22  63
fg           75  -6  -6   #a8bcc3   #99afb7   196  14  77
white        75  -6  -6   #a8bcc3   #99afb7   196  14  77
br_white     85  -6  -6   #c4d8df   #b9cfd8   196  12  88

red          61  63  40   #fc5851   #f33e3f     2  68  99
green        69 -37  53   #78b93e   #6bae27    92  66  73
yellow       74   6  65   #d8b033   #cda11d    46  76  85
blue         61   0 -55   #4e97f5   #4183f5   214  68  96
magenta      65  59 -21   #f16dc5   #e652bb   320  55  95
cyan         73 -40  -4   #41c7b9   #42beaa   174  67  78

br_red       66  63  40   #ff675d   #ff4c4a     3  65 100
br_green     74 -37  53   #85c74c   #79be33    92  62  78
br_yellow    79   6  65   #e7be42   #dfb02a    45  72  90
br_blue      66   0 -55   #5ea4ff   #4f92ff   215  64 100
br_magenta   70  59 -21   #ff7bd3   #f960cc   320  52 100
br_cyan      78 -40  -4   #52d5c7   #50ceba   173  61  84
```



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/y2dMcsE.png)

```
Color        CIE L*a*b*   sRGB      AppleRGB  HSB
----------   ----------   -------   --------  -----------
bg           15  -8 -13   #072938   #0b1f2b   198  87  22
black        25 -10 -16   #154053   #143242   198  74  33
br_black     50  -7  -9   #637b86   #526873   199  26  53
fg           65  -6  -6   #8ea1a8   #7d9098   196  16  66
white        65  -6  -6   #8ea1a8   #7d9098   196  16  66
br_white     75  -6  -6   #a8bcc3   #99afb7   196  14  77

red          51  63  40   #dc3a3a   #cd222c   360  74  86
green        59 -37  53   #5c9e21   #518f0d    92  79  62
yellow       64   6  65   #ba9610   #aa8400    47  92  73
blue         51   0 -55   #267dd8   #2268d2   211  82  85
magenta      55  59 -21   #d451aa   #c3379c   319  62  83
cyan         63 -40  -4   #12ab9e   #269e8c   175  90  67

br_red       56  63  40   #ec4946   #e03035     1  71  93
br_green     64 -37  53   #6aac30   #5e9e1b    92  72  67
br_yellow    69   6  65   #c9a323   #bb920e    46  82  79
br_blue      56   0 -55   #3c8ae6   #3276e3   213  74  90
br_magenta   60  59 -21   #e25fb8   #d444ab   320  58  89
br_cyan      68 -40  -4   #2eb9ab   #34ad9b   174  75  73
```



Selenized black
---------------

![Selenized black screenshot](http://i.imgur.com/PVKtHEC.png)

```
Color        CIE L*a*b*   sRGB      AppleRGB  HSB
----------   ----------   -------   --------  -----------
bg           10   0   0   #1b1b1b   #151515    35   0  11
black        20   0   0   #303030   #242424    35   0  19
br_black     55   0   0   #848484   #717171    35   0  52
fg           70   0   0   #ababab   #9b9b9b    35   0  67
white        70   0   0   #ababab   #9b9b9b    35   0  67
br_white     80   0   0   #c6c6c6   #bababa    35   0  78

red          56  63  40   #ec4946   #e03035     1  71  93
green        64 -37  53   #6aac30   #5e9e1b    92  72  67
yellow       69   6  65   #c9a323   #bb920e    46  82  79
blue         56   0 -55   #3c8ae6   #3276e3   213  74  90
magenta      60  59 -21   #e25fb8   #d444ab   320  58  89
cyan         68 -40  -4   #2eb9ab   #34ad9b   174  75  73

br_red       61  63  40   #fc5851   #f33e3f     2  68  99
br_green     69 -37  53   #78b93e   #6bae27    92  66  73
br_yellow    74   6  65   #d8b033   #cda11d    46  76  85
br_blue      61   0 -55   #4e97f5   #4183f5   214  68  96
br_magenta   65  59 -21   #f16dc5   #e652bb   320  55  95
br_cyan      73 -40  -4   #41c7b9   #42beaa   174  67  78
```

