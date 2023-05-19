import matplotlib.pyplot as plt
from hydrogen import cartesian_prob, cartesian_prob_real
from get_render_radius import get_render_radius


def render_3d(n, l, m, path, mode):
  print('Rendering ' + mode + ' 3d model for (' + str(n) + ', ' + str(l) +
        ', ' + str(m) + ')')

  render_radius = get_render_radius(n, l) + 2

  # width, height, and depth in number of steps
  s = 100

  # step = size of pixel in a_0
  step = 2 * render_radius / s

  # generate list of x, y, and z coordinates
  axis_set = [(float(i) - s / 2) * step for i in range(s + 1)]

  # lists to dump data
  x_data, y_data, z_data, p_data = [], [], [], []

  # keep track of progress
  point_count = len(axis_set)**3
  current_point = 0

  print('Calculating probabilities')
  # make data
  for x in axis_set:
    for y in axis_set:
      for z in axis_set:
        # calc p
        if mode == 'real':
          p = cartesian_prob_real(n, l, m, x, y, z)
        elif mode == 'complex':
          p = cartesian_prob(n, l, m, x, y, z)

        # append data
        p_data.append(p)
        x_data.append(x)
        y_data.append(y)
        z_data.append(z)

        current_point += 1

    # log progress
    print('Calculated ' + str(round(current_point / point_count * 100)) + '% of points')

  print('Rendering figure')
  # find net probability
  sum_p = sum(p_data)

  # normalize data such that sum(p) = 1
  p_data = [p / sum_p for p in p_data]

  # find max p
  max_p = max(p_data)

  # make figure
  plt.figure(dpi=600)
  ax = plt.axes(projection='3d')

  # plot
  scatter = ax.scatter3D(x_data,
                         y_data,
                         z_data,
                         edgecolors='none',
                         depthshade=False)

  # color
  scatter.set_facecolors([[
    max((x_data[p[0]] + render_radius) / (2 * render_radius), 0),
    max((y_data[p[0]] + render_radius) / (2 * render_radius), 0),
    max((z_data[p[0]] + render_radius) / (2 * render_radius), 0),
    (p[1] / max_p)**0.5 / 15
  ] for p in enumerate(p_data)])

  # labels
  plt.title(f'Electron Cloud of ({n}, {l}, {m}) {mode.capitalize()} Hydrogen Orbital')
  ax.set_xlabel(r'x ($a_{0}$)')
  ax.set_ylabel(r'y ($a_{0}$)')
  ax.set_zlabel(r'z ($a_{0}$)')

  # save
  print('Saving')
  plt.savefig(path)
  
  # close
  print('Closing')
  plt.close()

  print('Done')