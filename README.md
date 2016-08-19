# How to write a Python GRASS GIS 7 addon

This material was developed for FOSS4G Europe 2015 workshop.

<a href='http://grass.osgeo.org' target='_blank'>
 <img src="grass_gis_logo.png" width=200 alt="GRASS GIS logo" />
</a>
<a href='http://europe.foss4g.org/2015/' target='_blank'>
 <img src="foss4g_europe_2015_logo.png" alt="FOSS4G-E 2015 logo" />
</a>

## How to use this tutorial

### Using only GRASS GIS

Start GRASS GIS on you computer. Browse through IPython Notebooks as rendered on GitHub.
To do this you just need to click on one of the files with the suffix `.ipynb`.
In GRASS GIS in *Layer Manager* window, select *Python shell* in the bottom
to get an interactive Python console where you can input, edit and run the examples.
You may want to make the window bigger to have more space for the code.

### With IPython and Git

Navigate to the directory where you want to work and clone this
repository (unless you already downloaded a copy):

    git clone git@github.com:wenzeslaus/python-grass-addon.git

Navigate to the repository directory:

    cd python-grass-addon

Start GRASS GIS, from command line, using the North Carolina sample dataset:

    grass7

Run (supposing that you are already in a GRASS GIS session) on command line:

    ipython notebook

You will get a website in a web browser where you can select individual Notebooks,
edit and run the examples.


## Abstract

GRASS GIS is a leading software in analysis of geodata, it offers more than 400 modules in its core version plus many addons (i.e., user contributed modules). But what if the tool you are looking for is not present in GRASS GIS? So, simply create your own, we will show you how to do that in this workshop.

In GRASS GIS 7, Python is the default language for creating addons. There are two main Python libraries included in GRASS GIS. Python Scripting Library allows you to perform analysis and compute new data by chaining existing modules to create your own workflow.

With PyGRASS library wrapping the C functions, you can create new data sets (vector and raster) directly through Python calls, increasing considerably the power and performance of your scripts. You can conveniently mix both GRASS Python libraries with other Python libraries like NumPy, or SciPy. In this workshop, we will guide you through the basic steps of writing your own Python scripts, starting with calling and chaining GRASS GIS modules, followed by a more pythonic experience when using PyGRASS to access and modify your data directly.

You will then upgrade your script into an addon by defining a simple interface to enable automatically generated GUI. The next part of workshop will look into more advanced usage of GRASS GIS 7 capabilities, including Python spatio-temporal API to handle time series in your addons, creating your own toolbox with your newly developed addons and finally, introducing the new testing framework you should use as a responsible person to make sure your addons are in great shape.

Don't worry if we won't cover all the topics during the workshop, all materials will be accessible online and GRASS GIS community is always prepared to answer your questions!


## Required knowledge

Participants should have basic knowledge of GIS, basic knowledge of GRASS GIS and basic knowledge of Python.


## Set up a server

When organizing a workshop, it might be advantageous to use a server with IPython Notebook
rather then setting up the environment on participant's computers. When IPython Notebook
is used on a server, participants will need only a browser. All server-side work is easy
to do thanks to Docker.

    mkdir workdir
    cd workdir

    wget http://grass.osgeo.org/sampledata/north_carolina/nc_basic_spm_grass7.tar.gz
    wget https://github.com/wenzeslaus/python-grass-addon/archive/master.tar.gz

    tar xvf nc_basic_spm_grass7.tar.gz
    tar xvf master.tar.gz

Now you can get the basic GRASS GIS image. Note that if you user does not have permissions
to use docker (the usual defaut), you have to prefix the `docker` command with `sudo`. The same applies for scripts used futher on which are using the `docker` command. If you already have the image, you can skip this step.

    docker build github.com/wenzeslaus/grass-gis-docker

To create the image and containers we need some files from this repository (we got its content in previous steps). We use `mv` because we don't need those files to be compied to the containers later.

    mv python-grass-addon-master/Dockerfile .
    mv python-grass-addon-master/run_containers.sh .
    mv python-grass-addon-master/command_containers.sh .

Build a Docker image with sample dataset and Notebooks. If you are using your image for GRASS GIS (see above), be sure you have the right image name in the Dockerfile (used by following command).

    docker build -t wenzeslaus/python-grass-addon .

Create a file with users you want to create an container for. The file must contain
emails at the beginning of each line (it can be for example CSV, double quote at the beginning
is ignored).

    john@university.edu
    jsmith@example.com

Now you can start:

    ./run_containers.sh workshop_atendees.txt 9000

Alternatively, you can just specify number of conatiners you want to create:

    ./run_containers.sh 15 9000

This will give you list of URLs and passwords with associated usernames. Usernames are
used only to keep track of containers and to distribute the credentials. Note that
the atendees will have to get through "untrusted connection" dialog in their browsers
because the certificate used is self-signed.

The above command will also create a file named `containers_workshop_atendees.txt`
(or `containers_dateandtime.txt`) with names of conatiners.
For further actions, if they are simple enough,
you can use a prepared script. For example, to get rid of the containers use:

    ./command_conatiners.sh stop containers_workshop_atendees.txt
    ./command_conatiners.sh rm containers_workshop_atendees.txt


## Instructions for participants when IPython Notebook server is used

You have obtained URL which looks like:

    https://fatra.cnr.ncsu.edu:9503

Type it precisely to the web browser including the *s* at the end of
`https`, note also that port number is specified (the number at the end
separated from domain by a colon.

You browser will warn you about invalid security certificate. In this
case, you can safely add security exception. The reason for
the message is that the certificate is self-signed.

Finally, enter the password you were provided with. Then you should
see a list of notebooks as displayed by IPython Notebook.


## When and where the workshop was presented

* North Carolina State Univeristy, test run (2 hours)
* FOSS4G Europe 2015, Como, Italy (4 hours)
* North Carolina State Univeristy, workshop for a geovisualization class (2 hours), [recording available](https://www.youtube.com/watch?v=PX2UpMhp2hc)


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
