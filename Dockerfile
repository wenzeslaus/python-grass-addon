# Authors:
#   Vaclav Petras


FROM wenzeslaus/grass-gis-docker:latest
MAINTAINER Vaclav Petras <wenzeslaus@gmail.com>

ADD python-grass-addon-master /notebooks
ADD nc_basic_spm_grass7 /grassdata/nc_basic_spm_grass7
