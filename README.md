# Hydrogen Electron Orbital Renderer
High quality renders of electron orbitals around Hydrogen, as well as the software to generate them.
| ![Cross Section of 5f Orbital](./img/cross/5_3_2.png) | ![Probability Distribution of a 5f Complex Orbital](./img/3d-complex/5_3_2.png) | ![Probability Distribution of a 5f Real Orbital](./img/3d-real/5_3_2.png) |
| ----- | ----- | ----- |
| Cross Section of a 5f Orbital | Probability Distribution of 5f Complex Orbital | Probability Distribution of a 5f Real Orbital |

## About

## Render Your Own Orbitals
The software used to generate these renders was built with Python, Scipy, Numpy, and Matplotlib. To install all nescacary packages through pip,
``` python
pip install -r requirements.txt
```

From there, run `python3 generator/main.py` to generate renders for all 140 orbitals.

### Notes for modifying the software
- `generator/render_3d.py` and `generator/render_cross_section.py` contain methods to render their respective orbtials.
- `hydrogen.py` contains methods for computing the probability density functions of real and complex orbitals, in both cartesian and polar coordinates. Credit to [Prof. Davit Potoyan and Mr. Zachery Crandall](https://dpotoyan.github.io/Chem324/H-atom-wavef.html) for the radial function.
- `get_render_radius.py` contains an algorithim for finding what bounding radius should be rendered