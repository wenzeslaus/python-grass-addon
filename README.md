# How to write a Python GRASS GIS 7 addon

This material was developed for FOSS4G Europe 2015 workshop.

<a href='http://europe.foss4g.org/2015/' target='_blank'>
 <img src="http://europe.foss4g.org/2015/assets/img/logo-200x200.png" alt="FOSS4G-E 2015 logo" />
</a>
<a href='http://grass.osgeo.org' target='_blank'>
 <img src="http://grass.osgeo.org/uploads/images/logo/grasslogo_big.gif" width=200 alt="GRASS GIS logo" />
</a>


## How to use this tutorial

Navigate to the directory where you want to work and clone this
repository (unless you already downloaded a copy):

    git clone git@github.com:wenzeslaus/python-grass-addon.git

Navigate to the repository directory:

    cd python-grass-addon

Start GRASS GIS, from command line, using the North Carolina dataset:

    grass7

Run (supposing that you are already in GRASS command line):

    ipython notebook


## Abstract

GRASS GIS is a leading software in analysis of geodata, it offers more than 400 modules in its core version plus many addons (i.e., user contributed modules). But what if the tool you are looking for is not present in GRASS GIS? So, simply create your own, we will show you how to do that in this workshop.

In GRASS GIS 7, Python is the default language for creating addons. There are two main Python libraries included in GRASS GIS. Python Scripting Library allows you to perform analysis and compute new data by chaining existing modules to create your own workflow.

With PyGRASS library wrapping the C functions, you can create new data sets (vector and raster) directly through Python calls, increasing considerably the power and performance of your scripts. You can conveniently mix both GRASS Python libraries with other Python libraries like NumPy, or SciPy. In this workshop, we will guide you through the basic steps of writing your own Python scripts, starting with calling and chaining GRASS GIS modules, followed by a more pythonic experience when using PyGRASS to access and modify your data directly.

You will then upgrade your script into an addon by defining a simple interface to enable automatically generated GUI. The next part of workshop will look into more advanced usage of GRASS GIS 7 capabilities, including Python spatio-temporal API to handle time series in your addons, creating your own toolbox with your newly developed addons and finally, introducing the new testing framework you should use as a responsible person to make sure your addons are in great shape.

Don't worry if we won't cover all the topics during the workshop, all materials will be accessible online and GRASS GIS community is always prepared to answer your questions!


## Required knowledge

Participants should have basic knowledge of GIS, basic knowledge of GRASS GIS and basic knowledge of Python.


## Authors

* Pietro Zambelli, European Research Academy
* Markus Neteler, Fondazione Edmund Mach
* Luca Delucchi, Fondazione Edmund Mach
* Vaclav Petras, NCSU OSGeoREL
* Anna Petrasova, NCSU OSGeoREL

Copyright (C) 2015 by authors.


## License

The documentation is dual licensed under CC BY-SA and GNU FDL.

The code samples are under GNU GPL 2 or later
(which is the license GRASS GIS is under).
