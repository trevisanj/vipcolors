__all__ = ["get_randomcolor", "get_randomgray", "get_colorgetter", "get_colorschemenames", "str2rgb", "get_colorscheme",
           "get_interpolator", "get_randomgetter", "get_identifiers"]
import numpy as np
import random
import scipy.interpolate
from collections import Counter
from PIL.Image import Image
from . import colorschemes

def get_colorschemenames():
    """Returns color scheme names"""
    ret = [name[12:] for name in dir(colorschemes) if name.startswith("colorscheme_")]
    return ret


def get_colorscheme(colorschemename):
    """Return [n]x[3] array corresponding to colorschemename."""
    varname = f"colorscheme_{colorschemename.upper()}"
    if varname not in dir(colorschemes):
        raise ValueError(f"Color scheme '{colorschemename}' not recognized, please choose among {get_colorschemenames()}")
    ret = getattr(colorschemes, varname)
    # if not isinstance(ret, np.ndarray):
    #     ascheme = np.array(ret)
    return ret


def get_identifiers():
    """Returns all values recognized as identifier by get_colorgetter()"""
    return ["fixed", "random", "gray"]+get_colorschemenames()


def get_colorgetter(identifier, fixedcolor=(255, 255, 255)):
    """This is kind of a router that will return a function, which is different depending on name.

    Args:
        identifier: (case insensitive) name has some "special words": "fixed", "random", "gray".
              Otherwise, this method will understand that name is the
              name of a color map as in the colorschemes module
        fixedcolor: used only if name is "fixed". In this case, a method that always returns fixedcolor will be returned.

    Returns:
         a method
    """
    identifier = identifier.lower()
    if identifier == "fixed":
        def getcolor():
            return fixedcolor

        return getcolor
    elif identifier == "random":
        def get_color():
            return get_randomcolor()  # TODO find way to pass limits

        return get_color
    elif identifier == "gray":
        def get_color():
            return get_randomgray()  # TODO find way to pass limits

        return get_color
    else:
        return get_randomgetter(identifier)


def get_randomgetter(colorschemename):
    """Returns a function that picks randomly from specified color scheme"""
    ascheme = get_colorscheme(colorschemename)
    n = ascheme.shape[0]
    getter = get_interpolator(colorschemename, (0, n-1))

    def get_random_rgb():
        x = random.random()*(n-1)
        return getter(x)

    return get_random_rgb


def get_interpolator(colorschemename, bounds=(0., 1.)):
    """Returns a method get_rgb(x), where x may be within bounds (edges included)"""
    xmin, xmax = bounds
    ascheme = get_colorscheme(colorschemename)
    n = ascheme.shape[0]
    xx = np.linspace(xmin, xmax, n)
    # 3 interpolators, one for each RGB channel
    interpolators = [scipy.interpolate.interp1d(xx, ascheme[:, i]) for i in range(3)]

    def get_rgb(x):
        if not (xmin <= x <= xmax):
            raise ValueError(f"Argument must be within [{xmin}, {xmax}]")
        rgb = tuple(np.round([ii(x) for ii in interpolators]).astype(np.uint8))
        return rgb

    return get_rgb


def get_randomcolor(minvalue=0, maxvalue=255):
    return tuple([random.randint(minvalue, maxvalue) for _ in range(3)])


def get_randomgray(minvalue=0, maxvalue=255):
    c = random.randint(minvalue, maxvalue)
    return tuple([c for _ in range(3)])


def str2rgb(arg):
    ret = tuple([255 if y > 255 else y for y in [int(x.strip()) for x in arg.split(",")]])
    return ret