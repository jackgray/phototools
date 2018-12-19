




#lppmm = input('Please enter the lp/mm to be converted to pixel size: ')
#ppi = input('Please enter the ppi to be converted to pixel size: ')

# COLLECT INPUT DIMENSIONS
hxl_orig = input('Enter input dimensions (height x length inches):')
hxl_orig_new = hxl_orig.split('x')
h_orig = float(hxl_orig_new[0])
l_orig = float(hxl_orig_new[1])
print(h_orig, l_orig)
    
# ASK USER WHAT FORMAT TO CONVERT FROM / DISPLAY SIZE OF PIXELS
decision = 0
while decision != 'lp/mm' or 'ppi':
    decision = input('Convert to pixel size from lp/mm or ppi? (type lp/mm or ppi): ') 
    if decision == str('lp/mm'):
        lppmm = input('Enter resolution in lp/mm: ')
        print(lppmm)
        # CONVERT FROM lp/mm TO PIX SIZE
        ppmm = float(float(lppmm) * 2)            # convert line pairs to lines (pixels)
        ppum = float(float(ppmm) * float(.001))   # convert mm to um
        pix_size_um = float(1/float(ppum)) # number of um per pix is the inverse of pix/um
        ppi = float(float(ppmm) * float(25.4))
        print('You entered', lppmm, 'lp/mm, which should equal', ppi, 'ppi')
        print('The size of each pixel will be', round(pix_size_um, 2), 'um')
        break
    elif decision == str('ppi'):
        ppi = input('Enter resolution in ppi or dpi: ')
        # CONVERT FROM ppi TO PIX SIZE
        ppmm = float(float(ppi) / float(25.4))
        ppum = float(float(ppmm) * float(.001))
        pix_size_um = float(1/float(ppum))
        lppmm = float(float(ppmm) / 2)
        print('You entered', ppi, 'ppi, which should equal', round(lppmm, 2), 'lp/mm')
        print('The size of each pixel will be', round(pix_size_um, 2), 'um')
        break
    else:
        print('Error: please enter either "lp/mm" or "ppi"')
    
#inputDims()
#pixSize()

hxl_orig = input('Enter input dimensions (height x length inches):')
hxl_orig_new = hxl_orig.split('x')
h_orig = float(hxl_orig_new[0])
l_orig = float(hxl_orig_new[1])

# MEGAPIXEL RESOLUTION
# inches * pixels/inches = pixels
pix_x = float(h_orig) * float(ppi)
pix_y = float(l_orig) * float(ppi)
megaPix = float(pix_x) * float(pix_y) * 0.000001
print('\nThe pixel size of this image is', int(pix_x),'x',int(pix_y), 'pixels, or', round(megaPix, 2), 'megapixels')


print(h_orig, l_orig)

#megaPix()

#MEGAPIXELS TO lp/mm
megaPix = input('How many megapixels is your camera?')
digiPix_x = (float(megaPix) / float(4/3)) / 0.000001
digiPix_y = (float(megaPix) / float(3/4)) / 0.000001
print(digiPix_x, digiPix_y)
#lppmm = float(float(ppmm) / 2)

printDims = input('What size will the image be printed at (inches)?')
printDims_new = printDims.split('x')
iphonePrint_y = float(printDims_new[0])
iphonePrint_x = float(printDims_new[1])
print(iphonePrint_y, iphonePrint_x)
iphoneDPI_x = float(digiPix_x) / float(iphonePrint_x)
iphoneDPI_y = float(digiPix_y) / float(iphonePrint_y)
print(iphoneDPI_x, iphoneDPI_y)
