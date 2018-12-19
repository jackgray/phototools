# iPhone Sensor Info
# the 12MP chip on the iPhone 7 and 7+ uses the Sony Exmor RS technology,
# a Bayer RGB color filter array and on-sensor phase detection
# Its die size is 5.16 mm x 6.25 mm as measured from the edges of the die stack

# This program will tell you the expected print resolution in lp/mm based on
# it's sensor capabilities only. Other factors, such as lens resolving power,
# are at play. That is beyond the scope of this script.

import math

def in2mm(inches):
    return inches * 25.4

def mm2in(mm):
    return mm / 25.4

rearSensor_l = 6.25     # mm
rearSensor_h = 5.16     # mm
rearSensor_hyp = math.hypot(rearSensor_l, rearSensor_h)
rearSensor_aspect = float(rearSensor_l) / float(rearSensor_h)
print('\n', rearSensor_aspect)
print('\n hypot = ', rearSensor_hyp)
print('\n', 4/3)


### Calculate native lp/mm from pixel size
##pixSize = input('Enter the individual pixel width in micrometers: ')
##pixSize_m = float(pixSize)*10**-6
##print(pixSize_m, 'meters')

rearMP = input('How many megapixels is the camera?' )

lxh_aspect = input('What is the aspect ratio of the camera? (Ex. 3:2, 4:3, 16:9, etc) ')
lxh_aspect = lxh_aspect.split(':')
lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
print(round(lxh_aspect, 2))
pix_l = math.sqrt((float(rearMP) * 1000000) * float(lxh_aspect))
pix_h = math.sqrt((float(rearMP) * 1000000) * (1/float(lxh_aspect)))
pix_diag = math.hypot(float(pix_l), float(pix_h))
print(int(pix_l), 'x', int(pix_h))

megaPix_check = float(pix_h) * float(pix_l) * 0.000001
print('megapix check = ', megaPix_check)

ppmm_l = float(pix_l) / float(rearSensor_l)
ppmm_h = float(pix_h) / float(rearSensor_h)
lppmm_l = float(ppmm_l) / 2
lppmm_h = float(ppmm_h) / 2
print('the native resolution on the sensor 1/3" sensor before enlargement is ',int(lppmm_l), ' x ', lppmm_h, 'lp/mm')


# Now that we have native lp/mm for the sensor, we can find the effective
# resolution after enlargement

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
        rearSensor_l, rearSensor_h = rearSensor_h, rearSensor_l       # swap vars to rotate input orientation to match output
        rotated = 1
else:
    orientation = str('square')

# determine enlargement factor E in both directions
# true  E with constrain crop will be the smallest of these two values
E_x = float(l_new) / float(mm2in(rearSensor_l))
E_y = float(h_new) / float(mm2in(rearSensor_h))

print('\norientation=', orientation)

# check for change in aspect ratio
aspect_orig = float(rearSensor_l / rearSensor_h)
aspect_new = float(l_new) / float(h_new)

print('\n')
f=1
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


printRes_lppmm_h = float(lppmm_h) / float(E)
printRes_lppmm_l = float(lppmm_l) / float(E)

print('the effective resolution after enlargement is ', int(printRes_lppmm_h), ' x ', int(printRes_lppmm_l), 'lp/mm')
