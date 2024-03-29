# AT2018cow
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

I wrote these scripts for my Master's Thesis. 

The original paper regarding AT2018cow can be found at https://arxiv.org/abs/1810.10880. 

What did I do? 

- I read the maps to arrays using function fits.getdata() from AstroPy library
- for every map of the galaxy (in specific wavelength), I chose a quite large area outside of the galaxy, and I've determined the standard deviation.
- I estimated galactial extinction for each wavelength
- I used Calzetti's atenuation law (http://www.bo.astro.it/~micol/Hyperz/old_public_v1/hyperz_manual1/node10.html)
- Converted corrected map to FITS again (https://docs.astropy.org/en/stable/io/fits/index.html)
- I've calculated aperture photometry in two circular regions
- Later on, I've selected 11 regions in space and calculated aperture photometry for them using radius=...