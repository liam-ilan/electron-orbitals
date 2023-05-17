import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.ticker as ticker
from hydrogen import cartesian_prob, cartesian_prob_real
from get_render_radius import get_render_radius


def render_cross_section(n, l, m, path):
  print('Rendering cross section for (' + str(n) + ', ' + str(l) +
        ', ' + str(m) + ')')
  render_radius = get_render_radius(n, l)

  # width and height in number of steps
  s = 400

  # step = size of pixel in a_0
  step = 2 * render_radius / s

  # grid to render
  arr = []

  print('Calculating probabilities')
  arr = [[
    cartesian_prob(n, l, m, (float(x) - s / 2) * step, 0,
                    (float(z) - s / 2) * step) for x in range(s + 1)
  ] for z in range(s + 1)]

  # set resolution and aspect ratio

  print('Rendering figure')
  plt.figure(dpi=600)

  # heat map
  img = plt.imshow(
    arr,
    cmap='magma',
    interpolation='nearest',
    extent=[-render_radius, render_radius, -render_radius, render_radius],
    norm=colors.PowerNorm(1 / 3))

  # make color bar, and always render in scientific notation
  cbar = plt.colorbar(img, location='bottom')
  cbar.ax.ticklabel_format(scilimits=(0,0), style='sci', useMathText=True)
  plt.setp(cbar.ax.get_xticklabels(), rotation=30, horizontalalignment='right', fontsize='small')

  # labels and title
  plt.xlabel(r'x ($a_{0}$)')
  plt.ylabel(r'z ($a_{0}$)')
  plt.title('XZ Plane Cross Section of a (' + str(n) + ', ' + str(l) + ', ' +
            str(m) + ') Hydrogen Orbital')

  # save
  print('Saving')
  plt.savefig(path)

  # close
  print('Closing')
  plt.close()
  print('Done')