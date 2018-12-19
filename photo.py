import math

# Convert mm to in
def mm2in(mm):
    return mm / 25.4

# Convert in to mm
def in2mm(inches):
    mm = float(inches) * 25.4
    return mm

# provides negative legnth and width given film format type as dim_orig array
def askFormat(format):
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
        dim_orig = [l_orig, h_orig]
    return dim_orig


# Converts megapixels to L x H pixel dimensions as an array
def MP2LxH(MP, lxh_aspect):
    lxh_aspect = lxh_aspect.split(':')
    lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
    pix_l = math.sqrt((float(MP) * 1000000) * float(lxh_aspect))
    pix_h = math.sqrt((float(MP) * 1000000) * (1/float(lxh_aspect)))
    lxh_pixels = [pix_l, pix_h]
    return lxh_pixels

#MEGAPIXELS TO lp/mm in the diagonal
def MP2lppmm(MP, lxh_aspect, sensorSize_in):
    sensorSize_mm = in2mm(sensorSize_in)
    lxh_aspect = lxh_aspect.split(':')
    lxh_aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
    pix_l = math.sqrt((float(MP) * 1000000) * float(lxh_aspect))
    pix_h = math.sqrt((float(MP) * 1000000) * (1/float(lxh_aspect)))
    pix_diag = math.hypot(float(pix_l), float(pix_h))
 #   lxh_pixels = [pix_l, pix_h]
 #   sensorSize_l = float(sensorSize)
 #   ppmm_l = float(pix_l) / float(sensorSize_l)
 #   ppmm_h = float(pix_h) / float(sensorSize_h)
    sensorSize_mm_l = math.sqrt((float(sensorSize_mm) * float(lxh_aspect)))
    sensorSize_mm_h = math.sqrt(float(sensorSize_mm) * (1/float(lxh_aspect)))
    print(sensorSize_mm_l, sensorSize_mm_h)
    lppmm_l = (float(pix_l) / float(sensorSize_mm_l)) / 2
    lppmm_h = (float(pix_h) / float(sensorSize_mm_h)) / 2
    lppmm = math.sqrt(float(lppmm_l) * float(lppmm_h))
 #   lppmm_diag = (float(pix_diag) / float(sensorSize_mm)) / 2
    return lppmm

# Given diagonal size (inches) and aspect ratio ('L:H' format), returns
# length and height as array 'LxH'
def findLxH(C, aspect):
    aspect = collectAspect(aspect)
    C = float(in2mm(C))
    L = math.sqrt(float(C) * float(aspect))
    H = math.sqrt(float(C) * (1/float(aspect)))
    LxH = [L, H]
    return LxH

# converts aspect ratio in 'L:H' format to L/H floating number
def collectAspect(lxh_aspect):
    lxh_aspect = lxh_aspect.split(':')
    aspect = float(lxh_aspect[0]) / float(lxh_aspect[1])
    return aspect

# determine if dimensions are landscape or portrait, swap x,y variables if portrait
def setLandscape(l_new, h_new):
    if l_new > h_new:
        orientation = str('landscape')
    elif h_new > l_new:
        orientation = str('portrait')
        l_orig, h_orig = h_orig, l_orig       # swap vars to rotate input orientation to match output
        rotated = 1
    else:
        orientation = str('square')


# gives enlargment factor given input and output dimentions ('LxH') format
# true E with constrain crop will be the smallest of E_x and E_y
def enlargement(dim_new, dim_orig):
    dim_new = dim_new.split('x')
 #   dim_orig = dim_orig.split('x')
    E_x = float(in2mm(dim_new[0])) / float(dim_orig[0])
    E_y = float(in2mm(dim_new[1])) / float(dim_orig[1])
    if E_x > E_y:
        E = E_y
##        crop_prcnt = crop_prcnt_h
##        crop_inches = crop_inches_h
        crop_dir = 'y'
    elif E_y > E_x:
        E = E_x
##        crop_prcnt = crop_prcnt_l
##        crop_inches = crop_inches_l
        crop_dir = 'x'
    else:
        #print('The full frame of the image will be retained! No cropping necessary! \n')
        E = E_y
    return E

# Provides individual pixel size (um) given resolution in lp/mm
def lppmm2pixelSize(lppmm):
    pixelSize = (1 / (2 * float(lppmm))) * 1000
    return pixelSize

# converts ppi to pixel size in um
def ppi2pixelSize(ppi):
    ppmm = in2mm(ppi)
    ppum = float(ppmm) * .001
    pixSize = 1 / float(ppum)
    return pixSize

# ppi to lp/mm
def ppi2lppmm(ppi):
    ppmm = in2mm(ppi)
    lppmm = float(ppmm) / 2
    return lppmm

# lp/mm to ppi
def lppmm2ppi(lppmm):
    ppmm = float(lppmm) * 2
    ppi = mm2in(float(ppmm))
    return ppi

##*******************HARDWARE CALCS*************************

# finds D_x, the diffraction limit of resolution
# args = f-stop & wavelegnth, any number between 390nm (violet) - 700nm (red)
def Dx(f, wvlnth):
    wvlnth_um = float(wvlnth)*10**-3
    Dx = 2 * float(1.22) * float(f) * float(wvlnth_um)
    return Dx

def lensDiam(f, focalLnth):
    lensDiam = float(focalLnth) / float(f)
    return lensDiam

# calculates the f-number, or minimum aperture of a lens given its
# focal length and diameter
def fnumber(focalLnth, lensDiam):
    fstop = float(focalLenth) / float(lensDiam)
    return fstop

def DOF(fnumber, cc, focalLnth, distance_ft):
    distance = in2mm(distance_ft * float(12))
    DOF = (2 * float(fnumber) * float(cc) * math.pow(focalLnth, 2) * float(distance)) / (math.pow(focalLnth, 2) - (math.pow(fnumber, 2) * math.pow(cc, 2) * math.pow(distance, 2)))
    DOF_in = mm2in(float(DOF))
    return DOF_in

# calculates minimum angle of separation between
# two objects that can just be resolved given
# for a given wavelength of light and lens diameter
def angularSep(wvlnth, lensDiam):
    theta_min = (1.22 * float(wvlnth)) / float(lensDiam)
    return theta_min
