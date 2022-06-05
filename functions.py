import numpy as np


def a_v_map_creation(first_frequency_map, comparison_map, standard_deviation):
    """Scales a map to a certain frequency"""
    tmp_list = first_frequency_map
    for row in range(len(first_frequency_map)):
        for value in range(len(first_frequency_map[0])):
            if comparison_map[row][value] == 0 or comparison_map[row][value] < 2 * standard_deviation:
                tmp_list[row][value] = 1
            elif first_frequency_map[row][value] / comparison_map[row][value] < 2.86:
                tmp_list[row][value] = 2.86
            else:
                tmp_list[row][value] = ((first_frequency_map[row][value] / comparison_map[row][value]) / 2.86) ** 2.114
    tmp_list = np.apply_along_axis(lambda x: 2.5 * np.log10(x), axis=0, arr=tmp_list)
    return tmp_list


def k_lambda(wavelength):
    """Calculates the k(lambda) value for each wavelength"""
    r_v = 4.05
    if wavelength < 630:
        return 2.659 * (1.509 / wavelength - 0.198 / wavelength ** 2 - 0.011 / wavelength ** 3) + r_v
    else:
        return 2.659 * (-1.857 + 1.040 / wavelength) + r_v


def a_lambda_calculation(a_v_map, k_lambda_for_specific_wavelength):
    """Calculates A_v map to A_lambda map"""
    r_v = 4.05
    tmp_list = a_v_map
    tmp_list = np.apply_along_axis(lambda x: (k_lambda_for_specific_wavelength * x) / r_v, axis=0, arr=tmp_list)
    return tmp_list
