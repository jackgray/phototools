# Convert megapixels to pixel dimensions
import math
import photo

##def MP2LxH(MP, lxh_aspect):
##    lxh_aspect = lxh_aspect.split(':')
##    lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
##    pix_l = math.sqrt((float(MP) * 1000000) * float(lxh_aspect))
##    pix_h = math.sqrt((float(MP) * 1000000) * (1/float(lxh_aspect)))
##    # Join pix_l and pix_h as one variable delimited by 'x'
##    lxh_pixels = str(float(pix_l)) + str('x') + str(float(pix_h))
##    lxh_pixels = lxh_pixels.split('x')
##    return lxh_pixels   


##lxh_pixels = photomodule.MP2LxH(input('Enter MP: '), input('Enter aspect: '))
##
##print(lxh_pixels)
##print('lxh_pixels = ', int(lxh_pixels[0]), ' x ', int(lxh_pixels[1]))


##lppmm = photomodule.MP2lppmm(input('Enter MP: '), input('Aspect ratio? '), input('Size of sensor in inches? '))
##print('Resolution = ', lppmm, 'lp/mm')
##
##pixelSize = photomodule.lppmm2pixelSize(lppmm)
##print('pixel size = ', pixelSize, 'um')
##
##LxH = photo.findLxH(.33333, '4:3')
##print(round(LxH[0], 2), 'mm x', round(LxH[1], 2), 'mm')
##
##sensor_diag = math.hypot(LxH[0], LxH[1])
##print('sensor diag = ', photo.mm2in(sensor_diag))
##
##LxH = photo.findLxH(sensor_diag, '4:3')
##print('new LxH = ', photo.in2mm(LxH[0]))
##
##ppi = photomodule.lppmm2ppi(lppmm)
##print(ppi, 'ppi')
##
##lppmm = photomodule.ppi2lppmm(ppi)
##print('lp/mm = ', lppmm)
##
##pixelSize = photomodule.ppi2pixelSize(ppi)
##print('pix size = ', pixelSize)


# compute enlargment from sensor to print

#dim_orig = photomodule.askFormat(input('Input negative format (ex 35mm, 6x6, 6x7, etc.: '))
##print('negative size is ', photomodule.in2mm(dim_orig[0]), 'x', photomodule.in2mm(dim_orig[1]), 'mm')
##
##E = photomodule.enlargement(input('what size is the print (inches)? '), dim_orig)
##print('E = ', E)


lensDiam = photo.lensDiam(1.8, 50)
print(lensDiam)

theta_min = photo.angularSep(500, lensDiam)
print(theta_min)
