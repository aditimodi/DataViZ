#!/usr/bin/env python
#coding: utf-8

import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cf
import matplotlib.pyplot as plt
import xarray as xr
from cdo import *
import matplotlib as mpl
import sys

cdo = Cdo()
plt.style.use('/home/cccr/aditi/AM_DataViz/style_sheets/styleSheetDoublecolumn.mplstyle')

# Read data1 and data2
# Define the following variables
lon1 = data1.lon
lat1 = data1.lat
lon2 = data2.lon
lat2 = data2.lat
title1 = 'Title for Plot 1'       
title2 = 'Title for Plot 2'       
colormap_title = 'Colormap Title' 
suptitle = 'Main declarative message of the figure'        
savefigpath = '/path/to/save/figure.png' 

# levels = np.arange(0, 1, 0.05)  
# cmap = plt.get_cmap('viridis')   
colormap_percentage = ["#fee391", "#df9114", "#9d6100", "#452b00","#1a1000"]
cmap = ListedColormap(colormap_percentage)
cmap.set_under(color='white')
boundaries = [0.01, 10, 20, 30,40,99]  # Intervals as specified
norm = BoundaryNorm(boundaries, cmap.N)

fig = plt.figure()

# Plot 1
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())
X1, Y1 = np.meshgrid(lon1, lat1)
DATA1 = ax1.contourf(X1, Y1, data1, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())
ax1.coastlines(color=None)
ax1.add_feature(cf.LAND, zorder=1, edgecolor='grey', facecolor='#E5E5E5')
ax1.text(0.02, 0.95, '(a)', transform=ax1.transAxes, va='top', ha='left')
gl1 = ax1.gridlines(draw_labels=True)
gl1.top_labels = False
gl1.right_labels = False
ax1.set_title(title1)

# Plot 2
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
X2, Y2 = np.meshgrid(lon2, lat2)
DATA2 = ax2.contourf(X2, Y2, data2, cmap=cmap, norm=norm, transform=ccrs.PlateCarree())
ax2.coastlines(color=None)
ax2.add_feature(cf.LAND, zorder=1, edgecolor='grey', facecolor='#E5E5E5')
ax2.text(0.02, 0.95, '(b)', transform=ax2.transAxes, va='top', ha='left')
gl2 = ax2.gridlines(draw_labels=True)
gl2.top_labels = False
gl2.right_labels = False
ax2.set_title(title2)

# Adjust subplots and colorbar
plt.subplots_adjust(wspace=0.2)
cbar_ax = fig.add_axes([0.18, 0.1, 0.6, 0.03])
cb=plt.colorbar(DATA2, cax=cbar_ax, orientation="horizontal", label=colormap_title)
cb.set_ticks(boundaries)
cb.outline.set_color('white')
cb.outline.set_linewidth(2)
cb.dividers.set_color('white')
cb.dividers.set_linewidth(4)

# Suptitle and save
plt.suptitle(suptitle, x=0.5, y=0.95, weight='bold', fontsize=18)
plt.savefig(savefigpath)
