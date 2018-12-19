# MODULE


def filmFormat(format):
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


# collect print dimensions as single input
def outSize(hxl_input):
    hxl_input = input('Enter dimensions (height x length):')
    hxl_new = hxl_input.split('x')
    h_new = float(hxl_new[0])
    l_new = float(hxl_new[1])
    
# Tell user which side will need to be cropped to maintain aspect ratio
# If the image is enlarged more in the horizontal (x), that means the sides
# will have to be cropped to maintain aspect ratio
def Ecalc(E_x, E_y):
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

def opti_res(E, printRes):
    scanRes = E * printRes
    print('\nTo print with the maximum possible print dpi, the scanning resolution must be at least', int(scan_res), 'ppi')

# Convert mm to in
def mm2in(mm):
    return mm / 25.4

# Convert in to mm
def in2mm(inches):
    return inches * 25.4

# converts ppi to lp/mm
def ppi2lppmm(ppi)
    return (float(ppi) / 25.4) / 2

# converts ppi to pixel size
def ppi2pixsize(ppi):
    print('Your scanner is composed of thousands of individual sensors.\
the size of these sensors determine the size of the pixels. Pixel size\
is related to the inverse of pixel density, or dpi/ppi.')
    ppmm = ppi / 25.4
    ppum = ppmm * .001
    pix_size_um = 1/ppum
    return pix_size_um

 #   1/(p/mm) = mm/p -->

def pixIn():
    pixIn_x = h_orig * ppi
    pixIn_y = l_orig * ppi

def pixOut():
    pixOut_x = float(h_new) * float(ppi)
    pixOut_y = float(l_new) * float(ppi)
    
# Convert megapixels to pixel dimensions
def MP2LxH(MP, lxh_aspect):
    lxh_aspect = lxh_aspect.split(':')
    lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
    pix_l = math.sqrt((float(MP) * 1000000) * float(lxh_aspect))
    pix_h = math.sqrt((float(MP) * 1000000) * (1/float(lxh_aspect)))
    # Join pix_l and pix_h as one variable delimited by 'x'
    lxh_pixels = str(float(pix_l)) + str('x') + str(float(pix_h))
    lxh_pixels = lxh_pixels.split('x')
    return lxh_pixels

