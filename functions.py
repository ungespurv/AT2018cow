import astropy.coordinates
import numpy as np
from astropy import units as u
from astropy.io import fits


def a_v_map_creation(first_frequency_map, comparison_map, standard_deviation):
    """Scales a map to a certain frequency"""
    tmp_list = np.copy(first_frequency_map)
    tmp_comparison = np.copy(comparison_map)
    for row in range(len(tmp_list)):
        for value in range(len(tmp_list[0])):
            if (
                tmp_comparison[row][value] <= 0
                or tmp_comparison[row][value] < 2 * standard_deviation
            ):
                tmp_list[row][value] = 1
            elif first_frequency_map[row][value] / tmp_comparison[row][value] < 2.86:
                tmp_list[row][value] = 1
            else:
                tmp_list[row][value] = (
                    (first_frequency_map[row][value] / tmp_comparison[row][value])
                    / 2.86
                ) ** 2.114
    # f_Ha = tmp_list # teraz jest f_Ha
    print(tmp_list[193][176])
    tmp_list = np.apply_along_axis(
        lambda x: 2.5 * np.log10(x), axis=-1, arr=tmp_list
    )  # -> A_V
    print(first_frequency_map[193][176])
    print(tmp_list[193][176])
    return tmp_list


def k_lambda(wavelength):
    """Calculates the k(lambda) value for each wavelength"""
    r_v = 4.05
    wavelength = wavelength * 0.001
    if wavelength < 0.63:
        return (
            2.659
            * (
                -2.156
                + 1.509 / wavelength
                - 0.198 / wavelength**2
                + 0.011 / wavelength**3
            )
            + r_v
        )
    else:
        return 2.659 * (-1.857 + 1.040 / wavelength) + r_v


def a_lambda_calculation(a_v_map, k_lambda_for_specific_wavelength):
    """Calculates A_v map to A_lambda map"""
    r_v = 4.05
    tmp_list = np.copy(a_v_map)
    tmp_list = np.apply_along_axis(
        lambda x: (k_lambda_for_specific_wavelength * x) / r_v, axis=0, arr=tmp_list
    )
    return tmp_list


def create_fits_file(a_lambda_map, filename):
    """Creates a .fits file from a corrected A_lambda map of the galaxy"""
    tmp_map = np.copy(a_lambda_map)
    hdu = fits.PrimaryHDU(tmp_map)
    fits.HDUList([hdu]).writeto(filename, overwrite=True)
    return 1


def luminosity_from_flux(flux, redshift):
    """Calculates the luminosity from the famous equation."""
    tmp_map = np.copy(flux)
    distance = astropy.coordinates.Distance(z=redshift)
    distance = distance.to(u.cm).value
    # 0.0136
    # 19.500477
    # 1.878712872817573e+26
    tmp_map = np.apply_along_axis(
        lambda x: 4.0 * np.pi * (distance**2) * x / (1 + redshift) * 10e-20,
        axis=0,
        arr=tmp_map,
    )
    return tmp_map


def calculate_sfr(l_map):
    """Calculates SFR"""
    constant = 7.9e-42
    tmp_map = np.copy(l_map)
    return constant * tmp_map


def metallicity(l_ha, l_n_ii, l_s_ii):
    """Calculates a value of 12+log(O/H)"""
    y = np.log10(l_n_ii / l_s_ii) + 0.264 * (
        np.log10(l_n_ii / l_ha)
    )  # jeśli s_ii lub h_ii <0, to nie da sie wyliczyc metalicznosci/
    desired_value = 8.77 + y + 0.45 * (y + 0.3) ** 5
    # desired_value = 8.77 + y
    return desired_value
