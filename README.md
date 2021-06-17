# vipcolors

A collections of color schemes with interpolation resources.

  - Language: Python3
  - Color format: ```(r, g, b)``` with integer values between within [0, 255]. 
    - Interpolations round values to return tuple of integers as well
    - There are functions to convert to **hex** (HTML) format and **pygame** format as well (are there?)

```
>>> import vipcolors
>>> print(vipcolors.get_colorschemenames())
['ALAMOS', 
'AUTUMN', 
'CABLES', 
'CAGANDO', 
'CHANAR', 
'COLD', 
'DARKSAD', 
'DRYEUCALIPTUS', 
'DRYLEAVES', 
'HORSESHIT', 
'JUANMA', 
'MATI', 
'MCY', 
'NICOBUDA', 
'POLVO', 
'PSYKITCHEN', 
'SAD', 
'SKY', 
'SOLE', 
'SUNSET',
'THISFLOWER', 
'VIOLA', 
'WINTER']
```

```
>>> vipcolors.get_colorscheme("HORSESHIT")
array([[162, 140, 141],
       [ 37,  33,  36],
       [205, 197, 201],
       [100,  90, 102],
       [125, 115, 130],
       [ 72,  65,  72],
       [189, 170, 169],
       [228, 229, 233],
       [144, 145, 177]])
```

```
>>> f = vipcolors.get_interpolator("JUANMA", (0, 10))
>>> print(f)
<function vipcolors.get_interpolator.<locals>.get_rgb(x)>
>>> print(f(0))
(60, 6, 5)
>>> print(f(10))
(157, 185, 209)
```
