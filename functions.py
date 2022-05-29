def k_lambda(wavelength):
    """Calculates the k(lambda) value for each wavelength"""
    r_v = 4.05
    if wavelength < 630:
        return 2.659 * (1.509 / wavelength - 0.198 / wavelength ** 2 - 0.011 / wavelength ** 3) + r_v
    else:
        return 2.659 * (-1.857 + 1.040/wavelength) + r_v


def a_v_map_creation(first_frequency_map, corrected, comparison_map, standard_deviation):
    """Scales a map to a certain frequency"""
    for pixel1 in range(334):
        for pixel2 in range(331):
            if comparison_map[pixel1][pixel2] == 0 or comparison_map[pixel1][pixel2] < 2 * standard_deviation:
                corrected.append(1)
            elif first_frequency_map[pixel1][pixel2] / comparison_map[pixel1][pixel2] < 2.86:
                corrected.append(2.86)
            else:
                corrected.append((first_frequency_map[pixel1][pixel2] / comparison_map[pixel1][pixel2] / 2.86) ** 2.114)


def a_lambda_calculation(a_v_map, k_lambda_for_specific_wavelength, a_lambda_output_map):
    """Calculates A_v map to A_lambda map"""
    r_v = 4.05
    for pixel in a_v_map:
        a_lambda_output_map.append((k_lambda_for_specific_wavelength * a_v_map[pixel]) / r_v)
