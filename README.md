# AT2018cow
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

I wrote these scripts for my Master's Thesis. 

The original paper regarding AT2018cow can be found at https://arxiv.org/abs/1810.10880. 

What did I do? 

- I read the maps to arrays using function fits.getdata() from AstroPy library
- for every map of the galaxy (in specific wavelength), I chose a quite large area outside of the galaxy, and I've determined the standard deviation.
- I estimated galactial extinction for each wavelength
- I used Calzetti's atenuation law (http://www.bo.astro.it/~micol/Hyperz/old_public_v1/hyperz_manual1/node10.html)
- convert corrected map to FITS again (https://docs.astropy.org/en/stable/io/fits/index.html)
- I've calculated aperture photmotrey in two circular regions Apertura pierwsza (X:148, Y:169, R=80.17) = 5.214709577201061 -> cała galaktyka (bez szumu)
Apertura druga (X:145, Y:175, R=7.24) = 1.8994402738527763 -> jasna część w środku


Current commit only for better debugging! (28.12.22)
To be continued...
