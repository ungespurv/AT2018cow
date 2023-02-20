from astropy.io import fits
from photutils.aperture import CircularAperture, aperture_photometry

sfr_map = fits.getdata("sfr_Ha.fits")
radius = 5
points = [
    (196, 156),
    (159, 153),
    (144, 174),
    (201, 129),
    (115, 209),
    (104, 202),
    (108, 155),
    (100, 147),
    (119, 187),
    (152, 216),
    (146, 219),
]
results = []
for coordinates in points:
    aperture = CircularAperture(coordinates, radius)
    phot = aperture_photometry(sfr_map, aperture)
    results.append(phot["aperture_sum"].value)

print(results)
