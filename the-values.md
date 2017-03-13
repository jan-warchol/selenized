Selenized color coordinates
===========================

LAB values are canonical.  RGB values (both sRGB and Apple RGB) are calculated
from LAB using `utils/convert-lab-palette-to-rgbs.py` script, which employs
`python-colormath` library for color space transformations.

Please note that orange and violet are not used in configs of terminal
emulators - they are intended for use with GUI applications (see
[FAQ](README.md#where-are-orange-and-violet)).



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/yM0vadH.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg           23 -12 -12   193  77  28   #103c48   #112e38
black        28 -13 -13   193  72  34   #184956   #163945
br_black     36 -13 -13   194  57  41   #2d5b69   #254a57
white        56  -8  -6   191  20  56   #72898f   #61777c
fg           75  -5  -2   182   8  74   #adbcbc   #9faeae
br_white     85  -5  -2   182   7  85   #cad8d9   #bfd0d0

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
bg            8   0   0    35   0   9   #181818   #121212
black        15   0   0    35   0  15   #252525   #1c1c1c
br_black     25   0   0    35   0  23   #3b3b3b   #2d2d2d
white        50   0   0    35   0  47   #777777   #636363
fg           75   0   0    35   0  72   #b9b9b9   #aaaaaa
br_white     88   0   0    35   0  87   #dedede   #d6d6d6

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

