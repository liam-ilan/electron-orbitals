from hydrogen import R


def get_render_radius(n, l):
  # find the radius to render (the radius that contains signficant probibility of an electron)
  render_radius = 5 * n
  current_radius = 0
  check_step = render_radius / 50

  # max R(r)
  max_R = 0

  while current_radius < render_radius:
    curr_R = R(current_radius, n, l)**2
    for_R = R(current_radius + check_step, n, l)**2
    max_R = max(curr_R, for_R, max_R)

    # if R'(r) > 0 (rising)
    if for_R - curr_R > 0:

      # render radius = 4 * last peak
      current_radius += check_step
      render_radius = 5 * current_radius
    else:
      current_radius += check_step

  # remove buffer space from render radius
  while R(render_radius, n, l)**2 < max_R / 100000:
    render_radius -= render_radius * 0.01

  print('Rendering for a radius of ' + str(render_radius) + ' a₀')
  return render_radius
