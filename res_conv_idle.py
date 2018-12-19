#Things to add:
#                 select which section to jump to (choose calculation at beginning)


import math
import time
#import photoconv

# User-defined functions
def mm2in(mm):
        return mm / 25.4            # returns inches

def in2mm(inches):
    return float(inches) * 25.4     # returns mm

def E_calc():                       # determines which side of image will be cropped for printing
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
def E_print():
    print('\nYour image will be enlarged by a factor of', E)
    print('\nYour image will be constrain-cropped in the', crop_dir, 'direction', crop_prcnt, '%, or', crop_inches, 'inches')

def scan_format():
    err = 1
    format = 0
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

print('A good printer can print at a max dpi of 400. That\'s 7.87 lp/mm in the x and y directions, and 5.57 lp/mm in the diagonal.\n')

# time.sleep(5)

print('This is the most you are going to get from an inkjet print. Scanning at 400 dpi, however, will only yeild such resolution if the size remains unaltered, at 36mm x 24mm. \n')

# time.sleep(7)

print('The larger you want your print to be, the higher the resolution the scan needs to be. \n')

# time.sleep(5)

print('This program does a variety of calculations to help determine proper resolution settings and print sizing.\n')

#time.sleep(3)

input("Press ENTER to continue")

print('\n')

print('------------------------------------------\n')


# Calculate Enlargement Latitude: E=R/L

print('We can calculate the Enlargement Latitude of a scanned negative (how much we can enlarge the original image before we notice degradation in quality). This is measured by the Legibility Rating L on a scale of 1-8, with 8 being no perceivable loss in quality. The number of times this number fits into the image resolution in dots per mm is the enlargement latitude.\n')

#in2mm = 0.0394
#mm2in = 25.4

ppi = float(input('scanning resolution? (DPI):'))

ppmm = ppi / 25.4   # 25.4 mm = 1 inch
lpmm = ppmm         # lines per mm = pixels per mm
lppmm = lpmm / 2    # line pairs per mm half that
lppmm_hyp = math.hypot(lppmm, lppmm) / 2

print('\n', round(lppmm, 2), 'lp/mm in x and y directions \n', round(lppmm_hyp, 2),  'diagonal\n')


            # Calculate aspect ratio

# ask user for print dimensions
l_new = float(input("Length of print?:"))
h_new = float(input("Height of print?:"))

# ask user to input negative format
format = str(input('Please enter the format of the negative you are scanning ("35mm", "6x4.5", "6x6", "6x7", "6x9", "4x5", "5x7", "8x10", "600", or "SX-70" (Polaroid)):'))

# collect negative format, conv 2 inches if needed
h_orig = 0        # these variables exist
l_orig = 0

scan_format()

x_pixels = ppi * l_new
y_pixels = ppi * h_new

img_res = [x_pixels, y_pixels]
print('\nThe image pixel size (x, y) is', img_res)

#min_lgblty = input('Minimum acceptable Legibility Rating? (1-8):')

R = lpmm

E_ = float(float(R) / 8)   # Enlargement Latitude

print('Maximum enlargement factor, E=',round(E,2))
print('---------------------------------------------\n')


# Calculate image enlargement factor
print('Now we can calculate how many times the image will be sized up given input print dimensions.\n')

# determine enlargement factor E in both directions
# true  E with constrain crop will be the smallest of these two values
E_x = float(l_new) / float(l_orig)
E_y = float(h_new) / float(h_orig)
E_hyp = math.hypot(E_x, E_y)

# Calculate Legibility Factor L given scanned resolution and enlargement factor
L_x = R / E_x
L_y = R / E_y
L_hyp = R / E_hyp

# print('\nThe Legibility rating of a', l_new, 'x', h_new, 'inch print (with 1 being poor quality and 8 being the highest), is:\n\n ', round(L_x, 1),'in the x direction \n ', round(L_y, 1),'in the y direction', 'and \n ', round(L_hyp, 1), 'in the diagonal')

print('\n---------------------------------------------------------------\n')

# Calculate max print size for desired quality based on Legibility Factor Scale

print('Now we will calculate the maximum print size for desired quality \n')

L_min = input('\nEnter minimum acceptable Lability rating (1-8):')

print('\n')

E_max = float(lpmm) / float(L_min)     

new_max_x = float(E_max * l_orig)      # max length of enlarged image to retain quality
new_max_y = float(E_max * h_orig)

print('The largest print that can be made from a 35mm negative at a scanning resolution of', ppi, 'dpi with a minimum Legibility rating of', L_min, 'is:\n\n', round(new_max_x, 1), 'x', round(new_max_y, 1), 'inches \n\n')

print('\n---------------------------------------------------------------\n')

# Calculate largest print size based on minimum resolution in lp/mm 

print("This section will determine the necessary scanning resolution given desired print dimensions and target resolution in lp/mm \n")

min_lppmm = float(input('Target resolution in lp/mm?'))

print_scan_res_x = min_lppmm * E_x
print_scan_res_y = min_lppmm * E_y
print_scan_res_hyp = min_lppmm * E_hyp
print_dpi = float(print_scan_res_hyp * 2 * 25.4)

print('\nYou will need to scan your negative at', int(print_dpi), 'ppi in order to retain the desired resolution in a', l_new,'x', h_new, 'inch print')

# Tell user which side will need to be cropped to maintain aspect ratio
# If the image is enlarged more in the horizontal (x), that means the sides
# will have to be cropped to maintain aspect ratio
print('\n')
##if E_x > E_y:
##    E = E_y
##    crop_prcnt = crop_prcnt_h
##    crop_inches = crop_inches_h
##    crop_dir = 'y'
##elif E_y > E_x:
##    E = E_x
##    crop_prcnt = crop_prcnt_l
##    crop_inches = crop_inches_l
##    crop_dir = 'x'
##else:
##        print('The full frame of the image will be retained! No cropping necessary! \n')
##print('\nYour image will be enlarged by a factor of', E)
##print('\nYour image will be constrain-cropped in the', crop_dir, 'direction', crop_prcnt, '%, or', crop_inches, 'inches')
##
#E_calc()
#E_print()
#scan_res = E * 400

print('\nTo print with the maximum possible print dpi, the scanning resolution must be at least', int(scan_res), 'ppi')
