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
black        35 -12 -19   199  68  44   #245970   #1f475e
br_black     60  -7  -9   199  22  63   #7c95a0   #6b838f
fg           75  -6  -6   196  14  77   #a8bcc3   #99afb7
white        75  -6  -6   196  14  77   #a8bcc3   #99afb7
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
black        25 -10 -16   198  74  33   #154053   #143242
br_black     50  -7  -9   199  26  53   #637b86   #526873
fg           65  -6  -6   196  16  66   #8ea1a8   #7d9098
white        65  -6  -6   196  16  66   #8ea1a8   #7d9098
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
black        20   0   0    35   0  19   #303030   #242424
br_black     55   0   0    35   0  52   #848484   #717171
fg           70   0   0    35   0  67   #ababab   #9b9b9b
white        70   0   0    35   0  67   #ababab   #9b9b9b
br_white     80   0   0    35   0  78   #c6c6c6   #bababa

red          56  63  40     1  71  93   #ec4946   #e03035
green        64 -37  53    92  72  67   #6aac30   #5e9e1b
yellow       69   6  65    46  82  79   #c9a323   #bb920e
blue         56   0 -55   213  74  90   #3c8ae6   #3276e3
magenta      60  59 -21   320  58  89   #e25fb8   #d444ab
cyan         68 -40  -4   174  75  73   #2eb9ab   #34ad9b
orange       62  37  50    22  73  87   #df793d   #d1632b
violet       59  33 -48   264  46  89   #a57ae3   #9063e0

br_red       61  63  40     2  68  99   #fc5851   #f33e3f
br_green     69 -37  53    92  66  73   #78b93e   #6bae27
br_yellow    74   6  65    46  76  85   #d8b033   #cda11d
br_blue      61   0 -55   214  68  96   #4e97f5   #4183f5
br_magenta   65  59 -21   320  55  95   #f16dc5   #e652bb
br_cyan      73 -40  -4   174  67  78   #41c7b9   #42beaa
br_orange    67  37  50    22  69  93   #ee8649   #e47036
br_violet    64  33 -48   264  44  95   #b387f2   #9f70f2
```

