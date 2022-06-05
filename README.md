# AT2018cow
I wrote these scripts for my Master's Thesis. 

The original paper regarding AT2018cow can be found at https://arxiv.org/abs/1810.10880. 

What did I do? 

- I read the maps to arrays using function fits.getdata() from AstroPy library
- for every map of the galaxy (in specific wavelength), I chose a quite large area outside of the galaxy, and I've determined the standard deviation.
- I estimated galactial extinction for each wavelength
- I used Calzetti's atenuation law (http://www.bo.astro.it/~micol/Hyperz/old_public_v1/hyperz_manual1/node10.html)
- convert corrected map to FITS again (https://hst-docs.stsci.edu/hstdhb/4-hst-data-analysis/4-4-working-with-fits-data-in-python)

To be continued...
