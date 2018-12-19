import math

megaPix = input('How many megapixels is your camera? ')
lxh_aspect = input('What is the aspect ratio of the camera? (Ex. 3:2, 4:3, 16:9, etc) ')
lxh_aspect = lxh_aspect.split(':')
lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
print(round(lxh_aspect, 2))
pix_l = math.sqrt((float(megaPix) * 1000000) * float(lxh_aspect))
pix_h = math.sqrt((float(megaPix) * 1000000) * (1/float(lxh_aspect)))
pix_diag = math.hypot(float(pix_l), float(pix_h))
print(round(pix_l, 2), round(pix_h, 2))

megaPix_check = float(pix_h) * float(pix_l) * 0.000001
print('megapix check = ', megaPix_check)

printDims = input('What size will the image be printed at (inches)? ')
printDims = printDims.split('x')
print_h = float(printDims[0])
print_l = float(printDims[1])
print(print_h, print_l)
print_diag = math.hypot(float(print_h), float(print_l))

print_ppi = float(pix_diag) / float(print_diag)
print('Resolution of a ', printDims, 'print = ', round(print_ppi, 2), 'ppi')

# CONVERT PRINT ppi TO lp/mm
ppmm = float(print_ppi) / float(25.4)
lppmm = float(ppmm) / 2
print('\n or ', round(lppmm, 2), ' lp/mm')

