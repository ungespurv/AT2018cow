# AT2018cow
I wrote these scripts for my Master's Thesis. 

The original paper regarding AT2018cow can be found at https://arxiv.org/abs/1810.10880. 

What did I do? 

- I read the maps to arrays using function fits.getdata() from AstroPy library
- for every map of the galaxy (in specific wavelength), I chose a quite large area outside of the galaxy, and I've determined the standard deviation.
- I estimated galactial extinction for each wavelength
- I used Calzetti's atenuation law (http://www.bo.astro.it/~micol/Hyperz/old_public_v1/hyperz_manual1/node10.html)
- Using the "a_lambda_calculation" function, I was able to get A_lambda maps for all of the emission wavelenghts


To be continued...
