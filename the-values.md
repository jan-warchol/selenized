Selenized color coordinates
===========================

LAB values are canonical.  RGB values (both sRGB and Apple RGB) are calculated
from LAB using `utils/convert-lab-palette-to-rgbs.py` script, which employs
`python-colormath` library for color space transformations.

Please note that orange and violet are not used in configs of terminal
emulators - they are intended for use with GUI applications (see
[FAQ](README.md#where-are-orange-and-violet)).



Selenized medium
----------------

![Selenized medium screenshot](http://i.imgur.com/U4y7JTc.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg           25 -10 -16   198  74  33   #154053   #143242
black        32 -12 -19   198  74  41   #1b5269   #194157
br_black     42 -12 -19   199  58  51   #366981   #2c566f
white        58  -7  -9   199  24  61   #77919c   #667e8b
fg           75  -6  -6   196  14  77   #a8bcc3   #99afb7
br_white     85  -6  -6   196  12  88   #c4d8df   #b9cfd8

red          61  63  40     2  68  99   #fc5851   #f33e3f
green        69 -37  53    92  66  73   #78b93e   #6bae27
yellow       74   6  65    46  76  85   #d8b033   #cda11d
blue         61   0 -55   214  68  96   #4e97f5   #4183f5
magenta      65  59 -21   320  55  95   #f16dc5   #e652bb
cyan         73 -40  -4   174  67  78   #41c7b9   #42beaa
orange       67  37  50    22  69  93   #ee8649   #e47036
violet       64  33 -48   264  44  95   #b387f2   #9f70f2

br_red       66  63  40     3  65 100   #ff675d   #ff4c4a
br_green     74 -37  53    92  62  78   #85c74c   #79be33
br_yellow    79   6  65    45  72  90   #e7be42   #dfb02a
br_blue      66   0 -55   215  64 100   #5ea4ff   #4f92ff
br_magenta   70  59 -21   320  52 100   #ff7bd3   #f960cc
br_cyan      78 -40  -4   173  61  84   #52d5c7   #50ceba
br_orange    72  37  50    22  66  99   #fd9456   #f77e41
br_violet    69  33 -48   265  42 100   #c195ff   #af7eff
```



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/ZozQMRm.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg           15  -8 -13   198  87  22   #072938   #0b1f2b
black        22 -10 -16   198  80  30   #0f3a4c   #102c3c
br_black     32 -10 -16   200  58  39   #295063   #213f50
white        48  -7  -8   198  25  50   #607781   #4f646e
fg           65  -6  -6   196  16  66   #8ea1a8   #7d9098
br_white     75  -6  -6   196  14  77   #a8bcc3   #99afb7

red          51  63  40   360  74  86   #dc3a3a   #cd222c
green        59 -37  53    92  79  62   #5c9e21   #518f0d
yellow       64   6  65    47  92  73   #ba9610   #aa8400
blue         51   0 -55   211  82  85   #267dd8   #2268d2
magenta      55  59 -21   319  62  83   #d451aa   #c3379c
cyan         63 -40  -4   175  90  67   #12ab9e   #269e8c
orange       57  37  50    23  77  81   #cf6c31   #bf5622
violet       54  33 -48   264  49  84   #976ed5   #8156ce

br_red       56  63  40     1  71  93   #ec4946   #e03035
br_green     64 -37  53    92  72  67   #6aac30   #5e9e1b
br_yellow    69   6  65    46  82  79   #c9a323   #bb920e
br_blue      56   0 -55   213  74  90   #3c8ae6   #3276e3
br_magenta   60  59 -21   320  58  89   #e25fb8   #d444ab
br_cyan      68 -40  -4   174  75  73   #2eb9ab   #34ad9b
br_orange    62  37  50    22  73  87   #df793d   #d1632b
br_violet    59  33 -48   264  46  89   #a57ae3   #9063e0
```



Selenized black
---------------

![Selenized black screenshot](http://i.imgur.com/Yk9OfdL.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg           10   0   0    35   0  11   #1b1b1b   #151515
black        19   0   0    35   0  18   #2d2d2d   #222222
br_black     30   0   0    35   0  28   #474747   #373737
white        50   0   0    35   0  47   #777777   #646464
fg           70   0   0    35   0  67   #ababab   #9b9b9b
br_white     82   0   0    35   0  80   #cccccc   #c1c1c1

red          53  63  40     1  72  89   #e3413f   #d52830
green        63 -37  53    92  73  66   #67a82d   #5b9a18
yellow       69   6  65    46  83  79   #c9a223   #bb910d
blue         53   0 -55   212  78  87   #3182de   #296ed9
magenta      58  59 -21   319  59  86   #dd5ab2   #cd3fa5
cyan         68 -40  -4   174  76  72   #2cb8aa   #33ac9a
orange       60  37  50    22  74  85   #da7539   #cb5f28
violet       57  33 -48   264  47  87   #9e75dd   #895dd8

br_red       59  63  40     2  69  97   #f6534d   #ec393c
br_green     69 -37  53    92  67  72   #77b93e   #6bad27
br_yellow    75   6  65    46  75  86   #dab235   #d0a31f
br_blue      59   0 -55   214  70  94   #4892f0   #3b7eef
br_magenta   64  59 -21   320  55  94   #ee6ac3   #e24fb8
br_cyan      74 -40  -4   174  67  79   #43c9bb   #44c0ac
br_orange    66  37  50    22  70  93   #ec8548   #e16f35
br_violet    63  33 -48   264  45  93   #af84ee   #9b6ded
```

