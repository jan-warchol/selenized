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
bg           24 -10 -16   198  77  32   #123e51   #123040
black        29 -11 -18   198  73  38   #1a4b60   #183a4e
br_black     37 -11 -18   199  59  45   #2f5d73   #274b60
white        56  -8 -10   199  25  60   #728c98   #607a87
fg           76  -6  -6   196  14  78   #abbfc6   #9cb2ba
br_white     86  -6  -6   196  12  89   #c8dce3   #bdd4dd

red          61  63  40     2  68  99   #fc5951   #f33e40
green        69 -38  55    92  69  73   #77bb3a   #6baf23
yellow       76   6  68    46  79  87   #ddb42f   #d3a617
blue         61   0 -57   213  71  98   #4897f9   #3c84fa
magenta      67  55 -15   325  51  96   #f477c0   #ea5db5
cyan         73 -40  -4   174  67  79   #43c8ba   #43bfab
orange       67  37  50    22  69  94   #ef874a   #e57136
violet       64  30 -45   263  42  93   #b08aed   #9d73eb

br_red       66  63  40     3  65 100   #ff685e   #ff4d4b
br_green     75 -38  55    92  64  79   #85c948   #7ac02f
br_yellow    81   6  68    46  74  93   #ecc33e   #e6b626
br_blue      66   0 -57   214  66 100   #5aa5ff   #4c92ff
br_magenta   72  55 -15   325  49 100   #ff85ce   #fd6bc6
br_cyan      79 -40  -4   173  61  84   #54d7c8   #52d1bc
br_orange    72  37  50    22  66 100   #ff9557   #f88042
br_violet    69  30 -45   263  40  99   #bf98fc   #ad82fe
```



Selenized dark
--------------

![Selenized dark screenshot](http://i.imgur.com/ZozQMRm.png)

```
Color        CIE L*a*b*   HSB           sRGB      AppleRGB
----------   ----------   -----------   -------   --------
bg           14  -8 -13   198  91  21   #052736   #091e29
black        19  -9 -14   198  80  26   #0d3343   #0e2634
br_black     27  -9 -14   200  61  33   #224455   #1b3544
white        46  -7  -9   199  27  49   #5b727c   #4a5f69
fg           66  -6  -6   196  15  67   #90a4ab   #7f939b
br_white     76  -6  -6   196  14  78   #acc0c7   #9eb3bb

red          51  63  40     0  73  87   #de3b3b   #cf232d
green        60 -38  55    91  82  63   #5da01d   #529206
yellow       66   6  68    48  96  76   #c19b07   #b28900
blue         51   0 -57   210  87  87   #1e7edd   #1d6ad8
magenta      57  55 -15   324  57  85   #d85ca6   #c74397
cyan         64 -40  -4   175  86  68   #18aea0   #29a08f
orange       58  37  50    23  76  82   #d16e32   #c25823
violet       55  30 -45   263  46  82   #9671d1   #805aca

br_red       57  63  40     2  70  93   #ee4b47   #e23236
br_green     65 -38  55    91  74  68   #6baf2d   #5fa217
br_yellow    71   6  68    47  85  82   #d0a920   #c39808
br_blue      57   0 -57   212  77  93   #378bec   #2f77ea
br_magenta   63  55 -15   325  54  91   #e76bb4   #da51a7
br_cyan      69 -40  -4   174  73  74   #32bcae   #38b19e
br_orange    63  37  50    22  72  88   #e17c3f   #d4652d
br_violet    60  30 -45   263  44  88   #a47ee0   #8f68dc
```



Selenized black
---------------

![Selenized black screenshot](http://i.imgur.com/Yk9OfdL.png)

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

