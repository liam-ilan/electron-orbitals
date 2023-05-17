from render_cross_section import render_cross_section
from render_3d import render_3d


# n: [1, 7]
# l: [0, n - 1]
# m: [-l, l] for complex orbitals, [0, l] for real orbitals
count = 0

for n in range(1, 8):
  for l in range(0, n):
    for m in range(-l, l + 1):
      count += 1
      print(f'Rendering Orbital {count}/140')

      if m >= 0: render_3d(n, l, m, './img/3d-real/' + f'{n},{l},{m}.png', 'real')
      render_3d(n, l, m, './img/3d-complex/' + f'{n},{l},{m}.png', 'complex')
      render_cross_section(n, l, m, './img/cross/' + f'{n},{l},{m}.png')

# Test
# n = 70
# l = 69
# m = 30
# render_3d(n, l, m, './img/' + f'test-3d.png', 'real')
# render_cross_section(n, l, m, './img/' + f'test-cross.png')