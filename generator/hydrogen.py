import numpy as np
import scipy.special as spe


# radial function (from https://dpotoyan.github.io/Chem324/H-atom-wavef.html)
def R(r, n=1, l=0):
  coeff = np.sqrt(
    (2.0 / n)**3 * spe.factorial(n - l - 1) / (2.0 * n * spe.factorial(n + l)))
  laguerre = spe.assoc_laguerre(2.0 * r / n, n - l - 1, 2 * l + 1)
  return coeff * np.exp(-r / n) * (2.0 * r / n)**l * laguerre


# wave function
def psi(n, l, m, r, azimuth, zenith):
  # sph_harm gets azimuthal angle first, then zenith
  return spe.sph_harm(m, l, azimuth, zenith) * R(r, n, l)


# wave function, for real orbitals (used in chemistry)
def psi_real(n, l, m, r, azimuth, zenith):
  if m < 0:
    return (-1)**m * np.imag(psi(n, l, abs(m), r, azimuth, zenith)) * (2**0.5)
  if m > 0:
    return (-1)**m * np.real(psi(n, l, abs(m), r, azimuth, zenith)) * (2**0.5)
  if m == 0: return psi(n, l, abs(m), r, azimuth, zenith)


# probability given wave function output
def prob(res):
  return np.absolute(res)**2


# final function we are trying to calculate, returns prob(psi(...)) given cartesian coordiantes
def cartesian_prob(n, l, m, x, y, z):
  r = (x**2 + y**2 + z**2)**0.5
  azimuth = np.arctan2(y, x)
  zenith = np.arctan2((x**2 + y**2)**0.5, z)
  return prob(psi(n, l, m, r, azimuth, zenith))


# final function we are trying to calculate, for real orbitals
# returns prob(psi_real(...)) given cartesian coordiantes
def cartesian_prob_real(n, l, m, x, y, z):
  r = (x**2 + y**2 + z**2)**0.5
  azimuth = np.arctan2(y, x)
  zenith = np.arctan2((x**2 + y**2)**0.5, z)
  return prob(psi_real(n, l, m, r, azimuth, zenith))
