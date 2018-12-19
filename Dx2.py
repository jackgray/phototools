import numpy as np
import photo

visualSpectrum = np.arange(390, 710, 10)
frange = np.arange(1, 33)

##print(visualSpectrum)
##print(frange)
##
##mux = [visualSpectrum * frange]

Dx_f = map(photo.Dx, frange, visualSpectrum)
#Dx_wvlnth = map(photo.Dx, visualSpectrum)

Dxf_list = list(map(photo.Dx, frange, visualSpectrum))
#Dxwvlnth_list = list(map(photo.Dx, visualSpectrum))


print('Dx_f = ', np.reshape(Dxf_list, (8,4)))
#print('Dx_wvlnth = ', Dxwvlnth_list)
