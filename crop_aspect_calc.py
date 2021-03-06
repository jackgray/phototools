import math
import time


def Ecalc():
    if E_x > E_y:
        E = E_y
        crop_prcnt = crop_prcnt_h
        crop_inches = crop_inches_h
        crop_dir = 'y'
    elif E_y > E_x:
        E = E_x
        crop_prcnt = crop_prcnt_l
        crop_inches = crop_inches_l
        crop_dir = 'x'
    else:
        #print('The full frame of the image will be retained! No cropping necessary! \n')
        E = E_y

def Eprint():
    print('\nYour image will be enlarged by a factor of', E)
    print('\nYour image will be constrain-cropped in the', crop_dir, 'direction', crop_prcnt, '%, or', crop_inches, 'inches')


def opti_res():
    spi = float(E) * float(dpi)
    print('\nTo print with the maximum possible print dpi, the scanning resolution must be at least', int(scan_res), 'ppi')

def mm2in(mm):
    return mm / 25.4


def in2mm(inches):
    return inches * 25.4

def ppi2ppmm(ppi):
    return ppi / 25.4

def megaPix():
    # inches * pixels/inches = pixels
    pix_x = float(h_orig) * dpi
    pix_y = float(l_orig) * dpi
    megaPix = (float(pix_x) * float(pix_y)) * 0.000001
    print('\nThe pixel size of this image is', int(pix_x),'x',int(pix_y), 'pixels, or', round(megaPix, 2), 'megapixels')

# def findpixelsize(maxdpi)
#       return 

# ask user to input negative format
#format = str(input('Please enter the format of the negative you are scanning ("35mm", "6x4.5", "6x6", "6x7", "6x9", "4x5", "5x7", "8x10", "600", or "SX-70" (Polaroid)):'))

### collect negative format in inches
##hxl_orig = input('Enter negative dimensions (height x length inches):')
##hxl_orig_new = hxl_orig.split('x')
##h_orig = float(hxl_orig_new[0])
##l_orig = float(hxl_orig_new[1])


err = 1
while err == 1:   # loop while input invalid
        err = 0
        if format == '35mm':
            h_orig = mm2in(24)              # original height in inches (1in=25.4mm)
            l_orig = mm2in(36)
        elif format == '6x6':
            h_orig = mm2in(60)
            l_orig = mm2in(60)
        elif format == '6x7':
            h_orig = mm2in(60)
            l_orig = mm2in(70)
        elif format == '6x4.5':
            h_orig = mm2in(45)
            l_orig = mm2in(60)
        elif format == '6x9':
            h_orig = mm2in(60)
            l_orig = mm2in(90)
        elif format == '4x5':
            h_orig = float(4)   # large format in inches
            l_orig = float(5)
        elif format == '5x7':
            h_orig = float(5)   # large format in inches
            l_orig = float(7)
        elif format == '8x10':    # large format in inches
            h_orig = float(8)
            l_orig = float(10)
        elif format == '600':
            h_orig == float(3.1)
            l_orig == float(3.1)
        elif format == 'SX-70':
            h_orig = float(3.1)
            l_orig = float(3.1)
        else:
            format = str(input('\nPlease type a valid format: "35mm", "6x4.5", "6x6", "6x7", "6x9", or "8x10":'))
            err = 1

# collect print dimensions (separately)
# h_new = float(input('Height of output print? (inches):'))
# l_new = float(input('Length of output print? (inches):'))

# collect print dimensions as single input
hxl_input = input('Enter dimensions of print (height x length):')
hxl_new = hxl_input.split('x')
h_new = float(hxl_new[0])
l_new = float(hxl_new[1])

# determine if dimensions are landscape or portrait, swap x,y variables if portrait
if l_new > h_new:
        orientation = str('landscape')
elif h_new > l_new:
        orientation = str('portrait')
        l_orig, h_orig = h_orig, l_orig       # swap vars to rotate input orientation to match output
        rotated = 1
else:
    orientation = str('square')

# determine enlargement factor E in both directions
# true  E with constrain crop will be the smallest of these two values
E_x = float(l_new) / float(l_orig)
E_y = float(h_new) / float(h_orig)

print('\norientation=', orientation)

# check for change in aspect ratio
aspect_orig = float(l_orig / h_orig)
aspect_new = float(l_new) / float(h_new)

print('\n')

if aspect_orig != aspect_new:
        print('Your print dimensions do not match the aspect ratio of the original, therefore the image must be cropped.')
else:
         f=0

# calculate amount of cropping to fill print dimensions without altering aspect ratio
crop_inches_l = (float(h_new) * float(aspect_orig)) - float(l_new)

crop_prcnt_l = (crop_inches_l / (float(h_new) * aspect_orig)) * 100

crop_inches_h = (float(l_new) / float(aspect_orig)) - float(h_new)

crop_prcnt_h = (crop_inches_h / (float(l_new) / float(aspect_orig))) * 100

print('E_x =', round(E_x, 2))
print('E_y =', round(E_y, 2))

# Tell user which side will need to be cropped to maintain aspect ratio
# If the image is enlarged more in the horizontal (x), that means the sides
# will have to be cropped to maintain aspect ratio

if E_x > E_y:
    E = E_y
    crop_prcnt = crop_prcnt_h
    crop_inches = crop_inches_h
    crop_dir = 'y'
elif E_y > E_x:
    E = E_x
    crop_prcnt = crop_prcnt_l
    crop_inches = crop_inches_l
    crop_dir = 'x'
else:
        #print('The full frame of the image will be retained! No cropping necessary! \n')
    E = E_y

if f != 0:
    print('\nYour image will be enlarged by a factor of', round(E, 2))
    print('\nYour image will be constrain-cropped in the', crop_dir, 'direction', int(crop_prcnt), '%, or', crop_inches, 'inches')
else:
    print('\nYour image will be printed at the same size it is scanned')


# SCANNING OPTIMIZATION
dpi = input('What is the max dpi of your printer?: ')

dpi = float(E) * float(dpi)
ppmm = float(dpi) / float(25.4)
ppum = float(ppmm) * float(.001)
pix_size_um = 1/float(ppum)
lppmm = float(ppmm) / 2
print('\nTo print with the maximum possible print dpi, the scanning resolution must be at least', int(dpi), 'ppi, or', round(lppmm, 2), 'lp/mm')
print('The size of each pixel will be', round(pix_size_um, 2), 'um')

megaPix()

#Ecalc()
#print()
#askdpi()
#optiScan()
