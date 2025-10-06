Selenized color coordinates
===========================

LAB values are canonical.  RGB values (both sRGB and Apple RGB) are calculated
from LAB using `utils/convert-lab-palette-to-rgbs.py` script, which employs
`python-colormath` library for color space transformations.



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg_0         23 -12 -12   193  77  28   #103c48   #112e38
bg_1         28 -14 -13   193  74  34   #174956   #163945
bg_2         36 -12 -11   193  51  40   #325b66   #284954
dim_0        56  -8  -6   191  20  56   #72898f   #61777c
fg_0         75  -5  -2   182   8  74   #adbcbc   #9faeae
fg_1         85  -5  -2   182   7  85   #cad8d9   #bfd0d0

red          60  63  40     2  68  98   #fa5750   #f13c3e
green        69 -38  55    92  70  73   #75b938   #69ad21
yellow       75   6  68    46  79  86   #dbb32d   #d1a416
blue         60   0 -57   213  72  97   #4695f7   #3a82f8
magenta      66  55 -15   325  52  95   #f275be   #e75bb3
cyan         73 -40  -4   174  67  78   #41c7b9   #42bdaa
orange       67  37  50    22  69  93   #ed8649   #e26f35
violet       64  30 -45   263  42  92   #af88eb   #9b72e9

br_red       66  63  40     3  65 100   #ff665c   #ff4b49
br_green     74 -38  55    92  65  78   #84c747   #78be2e
br_yellow    80   6  68    46  74  92   #ebc13d   #e4b424
br_blue      66   0 -57   214  66 100   #58a3ff   #4a91ff
br_magenta   72  55 -15   325  49 100   #ff84cd   #fb69c4
br_cyan      78 -40  -4   173  61  84   #53d6c7   #50cfba
br_orange    72  37  50    22  66  99   #fd9456   #f67e41
br_violet    69  30 -45   263  40  98   #bd96fa   #ab80fc
```



Selenized black
---------------

![Selenized black screenshot](http://i.imgur.com/rXIH87x.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg_0          8   0   0    35   0   9   #181818   #121212
bg_1         15   0   0    35   0  15   #252525   #1c1c1c
bg_2         25   0   0    35   0  23   #3b3b3b   #2d2d2d
dim_0        50   0   0    35   0  47   #777777   #636363
fg_0         75   0   0    35   0  72   #b9b9b9   #aaaaaa
fg_1         88   0   0    35   0  87   #dedede   #d6d6d6

red          56  63  40     1  70  93   #ed4a46   #e13136
green        67 -38  55    92  72  71   #70b433   #64a81d
yellow       75   6  68    46  79  86   #dbb32d   #d1a416
blue         56   0 -57   212  77  92   #368aeb   #2d76e9
magenta      64  55 -15   325  53  92   #eb6eb7   #de54ab
cyan         72 -40  -4   174  68  77   #3fc5b7   #40bba8
orange       64  37  50    22  71  90   #e67f43   #da6930
violet       60  30 -45   263  43  88   #a580e2   #9169dd

br_red       63  63  40     3  67 100   #ff5e56   #fb4343
br_green     74 -38  55    92  65  78   #83c746   #77bd2d
br_yellow    82   6  68    45  73  94   #efc541   #e9b928
br_blue      63   0 -57   214  69 100   #4f9cfe   #4289ff
br_magenta   71  55 -15   325  49 100   #ff81ca   #f767c0
br_cyan      79 -40  -4   173  60  85   #56d8c9   #53d2bd
br_orange    71  37  50    22  67  98   #fa9153   #f37b3f
br_violet    67  30 -45   263  41  96   #b891f5   #a67bf5
```




Selenized light
---------------

![Selenized light screenshot](http://i.imgur.com/kQVgD5U.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg_0         96   0  13    44  13  99   #fbf3db   #faf0d2
bg_1         91  -1  11    47  11  92   #e9e4d0   #e4dec4
bg_2         82  -2   8    56   8  81   #cfcebe   #c4c3b0
dim_0        62  -4   1   155   6  60   #909995   #7e8783
fg_0         42  -6  -6   195  24  43   #53676d   #43545a
fg_1         31  -6  -6   195  30  33   #3a4d53   #2d3c42

red          46  66  42   356  84  82   #d2212d   #c00221
green        54 -40  58    90 100  57   #489100   #3f8100
yellow       59   6  71    47 100  68   #ad8900   #9b7600
blue         46   0 -60   208 100  83   #0072d4   #005dcc
magenta      52  58 -16   323  64  79   #ca4898   #b73088
cyan         57 -42  -4   175 100  61   #009c8f   #038d7c
orange       52  39  52    23  84  76   #c25d1e   #b04713
violet       49  32 -47   262  50  78   #8762c6   #714cbc

br_red       44  66  42   354  89  80   #cc1729   #b9001e
br_green     52 -40  58    92 100  55   #428b00   #3a7b00
br_yellow    57   6  71    47 100  66   #a78300   #957000
br_blue      44   0 -60   208 100  81   #006dce   #0059c6
br_magenta   50  58 -16   323  66  77   #c44392   #b12b82
br_cyan      55 -42  -4   175 100  59   #00978a   #008777
br_orange    50  39  52    23  87  74   #bc5819   #a9430f
br_violet    47  32 -47   262  51  75   #825dc0   #6b47b6
```




Selenized white
---------------

![Selenized white screenshot](http://i.imgur.com/sc0Uv9h.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg_0        100   0   0    35   0 100   #ffffff   #ffffff
bg_1         93   0   0    35   0  92   #ebebeb   #e6e6e6
bg_2         82   0   0    35   0  80   #cdcdcd   #c2c2c2
dim_0        56   0   0    35   0  53   #878787   #747474
fg_0         30   0   0    35   0  28   #474747   #373737
fg_1         16   0   0    35   0  16   #282828   #1e1e1e

red          40  88  56   357 100  84   #d6000c   #c5000d
green        54 -53  77   108 100  59   #1d9700   #288800
yellow       65   8  95    46 100  77   #c49700   #b58400
blue         40   0 -80   214 100  89   #0064e4   #004fe0
magenta      50  77 -21   318  93  87   #dd0f9d   #cc008e
cyan         61 -56  -6   174 100  68   #00ad9c   #00a08a
orange       51  52  70    21 100  82   #d04a00   #bf3400
violet       45  42 -63   261  62  84   #7f51d6   #673ad0

br_red       33  88  56     0 100  75   #bf0000   #aa0000
br_green     47 -53  77   120 100  52   #008400   #147300
br_yellow    58   8  95    46 100  69   #af8500   #9d7100
br_blue      33   0 -80   216 100  81   #0054cf   #0040c8
br_magenta   43  77 -21   318 100  78   #c7008b   #b3007a
br_cyan      54 -56  -6   174 100  60   #009a8a   #008a77
br_orange    44  52  70    18 100  73   #ba3700   #a62300
br_violet    38  42 -63   260  67  76   #6b40c3   #542bb9
```

