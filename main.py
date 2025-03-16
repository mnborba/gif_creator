# GIF Creator

import imageio.v3 as iio

filenames = ['fh540-1620x1620-1.png', 'fh540-1620x1620-2.png', 'fh540-1620x1620-3.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('fh540.gif', images, duration=500, loop=0)