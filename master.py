from astropy.io import fits
import math as m
import functions

f_Ha = []
f_Hb = []
f_N_II = []
f_O_III = []
f_S_II = []

H_alfa = fits.getdata('AT2018cow_Ha.fits')  # 656.46 nm II
H_beta = fits.getdata('AT2018cow_Hb.fits')  # 486.1 nm I
N_II = fits.getdata('AT2018cow_NII.fits')  # 648.4 nm II
O_III = fits.getdata('AT2018cow_OIII.fits')  # 500.7nm I
S_II = fits.getdata('AT2018cow_SII.fits')  # 671.731  II
emission_wavelengths = [656.46, 486.1, 648.4, 500.7, 671.731]
H_alfa_standard_deviation = 13.507
H_beta_standard_deviation = 30.983
N_II_standard_deviation = 12.99717
O_III_standard_deviation = 27.53118
S_II_standard_deviation = 9.193647

functions.a_v_map_creation(H_alfa, f_Ha, H_beta, H_beta_standard_deviation)
functions.a_v_map_creation(H_beta, f_Hb, H_beta, H_beta_standard_deviation)
functions.a_v_map_creation(N_II, f_N_II, H_beta, H_beta_standard_deviation)
functions.a_v_map_creation(O_III, f_O_III, H_beta, H_beta_standard_deviation)
functions.a_v_map_creation(S_II, f_S_II, H_beta, H_beta_standard_deviation)

A_V_f_Ha = [2.5 * m.log10(x) for x in f_Ha]
A_V_f_Hb = [2.5 * m.log10(x) for x in f_Hb]
A_V_f_n_ii = [2.5 * m.log10(x) for x in f_N_II]
A_V_f_o_iii = [2.5 * m.log10(x) for x in f_O_III]
A_V_f_s_ii = [2.5 * m.log10(x) for x in f_S_II]

k_lambda_values = []
for length in emission_wavelengths:
    k_lambda_values.append(functions.k_lambda(length))


A_lambda_f_Ha = []
A_lambda_f_Hb = []
A_lambda_f_n_ii = []
A_lambda_f_0_iii = []
A_lambda_f_s_ii = []
functions.a_lambda_calculation(A_V_f_Ha, k_lambda_values[0], A_lambda_f_Ha)
functions.a_lambda_calculation(A_V_f_Hb, k_lambda_values[1], A_lambda_f_Hb)
functions.a_lambda_calculation(A_V_f_n_ii, k_lambda_values[2], A_lambda_f_n_ii)
functions.a_lambda_calculation(A_V_f_o_iii, k_lambda_values[3], A_lambda_f_0_iii)
functions.a_lambda_calculation(A_V_f_s_ii, k_lambda_values[4], A_lambda_f_s_ii)
print(A_lambda_f_s_ii)
