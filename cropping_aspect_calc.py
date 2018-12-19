
# define functions


def mm2in(mm):
    return mm / 25.4

# ask user to input negative format


format = str(input('Please enter the format of the negative you are scanning ("35mm",\
 "6x4.5", "6x6", "6x7", "6x9, "4x5", "5x7", "8x10", "600", or "SX-70"):'))

# convert input to
if format == '35mm':
        h_orig = mm2in(24)        # original height in in. (1in=25.4mm)
        l_orig = mm2in(36)         # original length
elif format == '6x6':
        h_orig = float(60 / 25.4)        # mm / 25.4 mm/in to
        l_orig = float(60 / 25.4)         # to convert mm to inches
elif format == '6x7':
        h_orig = float(60 / 25.4)
        l_orig = float(70 / 25.4)
elif format == '6x4.5':
        h_orig = float(60 / 25.4)
        l_orig = float(45 / 25.4)
elif format == '6x9':
        h_orig = float(60 / 25.4)
        l_orig = float(90 / 25.4)
elif format == '4x5':
        h_orig = float(4)
        l_orig = float(5)
elif format == '5x7':
        h_orig = 5
        l_orig = 7
elif format == '8x10':
        h_orig = float(8)
        l_orig = float(10)
elif format == '600' or 'SX-70':        # 3.1"x3.1" polaroid
        h_orig = float(3.1)
        l_orig = float(3.1)
else:
        print('Please type a valid format: \
          "35mm", "6x4.5", "6x6", "6x7", "6x9", or "8x10"')

# collect print dimensions
h_new = float(input('Height of output print? (inches):'))
l_new = float(input('Length of output print? (inches):'))

# determine if user means landscape or portrait, swap x,y variables if portrait

if l_new > h_new:
        orientation = str('landscape')
elif h_new > l_new:
        orientation = str('portrait')
        h_switch = l_orig
        l_switch = h_orig
#        print('h_switch=', h_switch)
#        print('l_switch=', l_switch)
else:
        orientation = str('square')

if orientation == 'portrait':
        l_orig = l_switch
        h_orig = h_switch
        print('l_orig=', l_orig)
        print('h_new=', h_orig)
else:
        f = 0

E_y = float(h_new) / float(h_orig)
E_x = float(l_new) / float(l_orig)

# print('E_x=',round(E_x,2))
# print('E_y=',round(E_y,2))
# print('orientation=',orientation)
# check for change in aspect ratio
aspect_orig = float(l_orig / h_orig)
aspect_new = float(l_new) / float(h_new)
# print('\n')
# print('Original aspect ratio =',aspect_orig)
# print('New aspect ratio =',aspect_new)
print('\n')

if aspect_orig != aspect_new:
        print('Your print dimensions do not match the aspect\
         ratio of the original, therefore the image must be cropped.')

# calculate amount of cropping to fill print \
# dimensions without altering aspect ratio


crop_inches_l = (float(h_new) * float(aspect_orig)) - float(l_new)
crop_prcnt_l = (crop_inches_l / (float(h_new) * aspect_orig)) * 100

crop_inches_h = (float(l_new) / float(aspect_orig)) - float(h_new)
crop_prcnt_h = (crop_inches_h / (float(l_new) / float(aspect_orig))) * 100

print('E_x =', round(E_x, 2))
print('E_y =', round(E_y, 2))

# Tell user which side will need to be cropped to maintain aspect ratio
# If the image is enlarged more in the horizontal (x), that means the sides
# will have to be cropped to maintain aspect ratio
print('\n')
if E_x > E_y:
        E_print = round(E_y, 2)
        crop_prcnt_print = round(crop_prcnt_h, 2)
        crop_inches_print = crop_inches_h
        crop_dir = 'y'
        # print('Your image will be enlarged by a factor of', round(E_y, 2),
        #     'and will be cropped in the y direction',
        #     round(crop_prcnt_h, 2), '%, \
        #     or', crop_inches_h, 'inches.\n')
        # scan_res = float(E_x) * 400
        # print('To print with the maximum possible print dpi,\
        #   the scanning resolution must be at least', int(scan_res), 'ppi')
elif E_y > E_x:
        # print('Your image will be enlarged by a factor of', round(E_x, 2),
        #     'and will be cropped on the sides by',
        #     round(crop_prcnt_l, 2),
        #    '%, or', round(crop_inches_l, 2), 'inches. \n')
        # scan_res = float(E_y) * 400
        # print('To print with the maximum possible print dpi, the scanning\
        # resolution must be at least', int(scan_res), 'ppi')

        E_print = round(E_x, 2)
        crop_prcnt_print = round(crop_prcnt_l, 2)
        crop_inches_print = crop_inches_l
        scan_res_print = float(E_y)
        crop_dir = str('x')
else:
        print('The full frame of the image will be retained! \
        No cropping necessary!')

print('Your image will be enlarged by a factor of', E_print,
      'and will be cropped in the y direction', round(crop_prcnt_print, 2),
      '%, or', crop_inches_print, 'inches.\n')

scan_res = float(E_print) * 400
print('To print with the maximum possible print dpi, the scanning \
      resolution must be at least', int(scan_res), 'ppi')
