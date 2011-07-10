#!/usr/bin/python
#
# a script to define some matlab compatible image functions

# copyright (C) 2010 Jean-Louis Durrieu
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import matplotlib.pyplot as plt

# The following instructions define some characteristics for the figures
# In order to be able to use latex formulas in legends and text in
# figures:
## plt.rc('text', usetex=True)
# Turn on interactive mode to display the figures:
plt.ion()
# Characteristics of the figures:
fontsize = 20;
linewidth=4
markersize = 16
# Setting the above characteristics as defaults:
plt.rc('legend',fontsize=fontsize)
plt.rc('lines',markersize=markersize)
plt.rc('lines',lw=linewidth)

def imageM(*args,**kwargs):
    """
    imageM(*args, **kwargs)

    This function essentially is a wrapper for the
    matplotlib.pyplot function imshow, such that the actual result
    looks like the default that can be obtained with the MATLAB
    function image.

    The arguments are the same as the arguments for function imshow.
    """
    # The appearance of the image: nearest means that the image
    # is not smoothed:
    kwargs['interpolation'] = 'nearest'
    # keyword 'aspect' allows to adapt the aspect ratio to the
    # size of the window, and not the opposite (which is the default
    # behaviour):
    kwargs['aspect'] = 'auto'
    kwargs['origin'] = 0
    plt.imshow(*args,**kwargs)
