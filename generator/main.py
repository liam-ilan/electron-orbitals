from render_cross_section import render_cross_section
from render_3d import render_3d
import os

# n: [1, 7]
# l: [0, n - 1]
# m: [-l, l]

# total image count: 420

count = 0

for n in range(1, 8):
  for l in range(0, n):
    for m in range(-l, l + 1):
      count += 1
      print(f'Rendering Orbital {count}/140')
      
      render_3d(n, l, m, './img/3d-real/' + f'{n}_{l}_{m}.png', 'real')
      render_3d(n, l, m, './img/3d-complex/' + f'{n}_{l}_{m}.png', 'complex')
      render_cross_section(n, l, m, './img/cross/' + f'{n}_{l}_{m}.png')

# test
# n = 2
# l = 1
# m = -1
# render_3d(n, l, m, './img/test/' + f'test-3d.png', 'real')
# render_cross_section(n, l, m, './img/test/' + f'test-cross.png')