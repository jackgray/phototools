# calc_lens_diam



whatPhone = input('What type of phone? (Type "other" to enter manually) ')

err = 1
while err == 1:         # loop while invalid input
    err = 0
    if whatPhone == str('iPhone 6'):
        # Front Camera Specs
        frontMP = 5                 # megapixels
        frontSensorSize = 1.12      # um
        frontFocalLength = 2.65     # mm
        frontFocalLength_eff = 31   # mm
        front_f = 2.2               # f = frontFocalLength / rearDiam
        # Rear Camera Specs
        rearMP = 12                 # megapixels
        rearSensorSize = 1.22       # um
        rearFocalLength = 4.15      # mm
        rearFocalLength_eff = 29    # mm
        rear_f = 2.2                # f = rearFocalLength /rearDiam
    elif whatPhone == str('iPhone 7'):
        # Front Camera Specs
        frontMP = 7                 # megapixels
        frontSensorSize = 1         # um
        frontFocalLength = 2.87     # mm
        frontFocalLength_eff = 32   # mm
        front_f = 2.2               # f = frontFocalLength / rearDiam
        # Rear Camera Specs
        rearMP = 12                 # megapixels
        rearSensorSize = 1.22       # um
        rearFocalLength = 4         # mm
        rearFocalLength_2 = 8       # (??) Secondary? mm
        rearFocalLength_eff = 28    # mm
        rearFocalLength_eff_2 = 56  # I have no idea what secondary means (from Anandtech)
        rear_f = 1.8                # f = rearFocalLength /rearDiam
    elif whatPhone == str('iPhone 7+'):
        whatPhone = str('iPhone 7')
        print('\niPhone 7 and 7+ have the same camera specs, using calculations for iPhone 7...')
        err = 1
    elif whatPhone == str('other'):
        rearFocalLength = input('Enter the focal length of your lens in millimeters: ')
        rear_f = input('What is the maximum aperture of your lens? ')
                        
    else:
        whatPhone = str(input('\nPlease enter a valid input: '))
        err = 1


rearDiam = float(rearFocalLength) / float(rear_f)

print('The diameter of the rear lens for the', whatPhone, 'is', round(rearDiam, 2), 'mm')
