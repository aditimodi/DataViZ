import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Set the figure size to be larger
plt.figure(figsize=(10, 8))

# Color 1
colors1 = ["blue", "green", "yellow", "red"]
cmap1 = ListedColormap(colors1)
ax1 = plt.subplot(4, 1, 1)
im = ax1.imshow([[0, 1, 2, 3]], cmap=cmap1)
cbar1 = plt.colorbar(im, ax=ax1, orientation='horizontal', pad=0.1, aspect=3)
cbar1.set_label('test')

# Color 2
colors2 = ["#fee391", "#df9114", "#9d6100", "#452b00", "#1a1000"]
cmap2 = ListedColormap(colors2)
ax2 = plt.subplot(4, 1, 2)
cbar2 = ax2.imshow([[0, 1, 2, 3, 4]], cmap=cmap2)
plt.colorbar(cbar2, ax=ax2, orientation='horizontal').set_label('monochrome style 1')

# Color 3
colors3 = ["#603c22", "#904f23", "#bf5d1f", "#fd8e01", "#ffb800"]
cmap3 = ListedColormap(colors3)
ax3 = plt.subplot(4, 1, 3)
cbar3 = ax3.imshow([[0, 1, 2, 3, 4]], cmap=cmap3)
plt.colorbar(cbar3, ax=ax3, orientation='horizontal').set_label('monochrome style 2')

# Color 4
colors4 = ["#ffffd4", "#fed98e", "#fe9929", "#d95f0e", "#993404"]
cmap4 = ListedColormap(colors4)
ax4 = plt.subplot(4, 1, 4)
cbar4 = ax4.imshow([[0, 1, 2, 3, 4]], cmap=cmap4)
# plt.colorbar(cbar4, ax=ax4, orientation='horizontal').set_label('monochrome style 3')

# Save the figure as a PDF
plt.tight_layout()
plt.savefig('AM_colormaps.pdf')
plt.close()
