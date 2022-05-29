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
emission_wavelengths = [486.1, 648.4, 500.7, 671.731]
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

A_V_corrected = []
for length in emission_wavelengths:
    A_V_corrected.append(functions.k_lambda(length))

A_lambda = []

