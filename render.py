import os
import tempfile

from IPython.core.display import Image

from grass.script import core as gcore
from grass.pygrass.modules.shortcuts import display as d
from grass.pygrass.modules.shortcuts import general as g


def view(rasters=None, vectors=None,
         pngfile=None, width=640, height=480,
         transparent=True, read_file=True, truecolor=True,
         engine='cairo', compression=9, rkw=None, vkw=None):
    """Return an IPython image object rendered by GRASS.

    Parameters
    -----------

    rasters: list
        List with the raster name to be rendered
    vectors: list
        List with the vector name to be rendered
    pngfile: path
        Path to the PNG file, default create a temporary file
    width: int
        Width size of the image
    height: int
        Height size of the image
    """

    def display():
        for raster in rasters if rasters else []:
            d.rast(map=raster, **(rkw if rkw else {}))
        for vector in vectors if vectors else []:
            d.vect(map=vector, **(vkw if vkw else {}))

    pngfile = (tempfile.mkstemp(suffix='.png')[1] if pngfile is None
               else pngfile)

    # set the enviornmental variables
    os.environ['GRASS_RENDER_IMMEDIATE'] = engine
    os.environ['GRASS_RENDER_FILE'] = pngfile
    os.environ['GRASS_RENDER_FILE_COMPRESSION'] = str(compression)
    os.environ['GRASS_RENDER_WIDTH'] = str(width)
    os.environ['GRASS_RENDER_HEIGHT'] = str(height)
    os.environ['GRASS_RENDER_TRANSPARENT'] = 'TRUE' if transparent else None
    os.environ['GRASS_RENDER_READ_FILE'] = 'TRUE' if read_file else None
    os.environ['GRASS_RENDER_TRUECOLOR'] = 'TRUE' if truecolor else None
    os.environ['GRASS_RENDER_PNG_AUTO_WRITE'] = 'TRUE'

    monitor = gcore.gisenv().get('MONITOR', None)
    if monitor:
        g.gisenv(unset='MONITOR')
        display()
        g.gisenv(set='MONITOR=%s' % monitor)
    else:
        display()
    return Image(pngfile)
