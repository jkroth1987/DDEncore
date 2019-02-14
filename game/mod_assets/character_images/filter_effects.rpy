########################################################################
# This file was created automatically by the Dynamic Pose Tool v1.4.   #
# You may edit this file manually, but be aware it will be overwritten #
# without confirmation the next time the tool is run and your changes  #
# will be lost.                                                        #
#                                                                      #
# It is recommended to only make temporary changes for test purposes   #
# which are harmless to lose in an overwrite.                          #
########################################################################

# Filter Quick Reference List:
# bw, cloudy, dawn, evening, flip,
# ghost, gray, morning, night, sepia,
# shadow, sunset, white


init python:
    def bw(image): # Basic Ren'Py Effect
        return im.MatrixColor(image, im.matrix.desaturate())

    def cloudy(image, darken_sky = False): # Agent Gold
        custom_matrix = im.matrix.identity()
        if darken_sky:
            # This is actually a 4x5 matrix. You can split this into four rows of five to see that more clearly.
            custom_matrix = [ 0.45, 0.15, 0.4, 0.0, 0.0, 0.2, 0.5, 0.3, 0.0, 0.0, 0.25, 0.25, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0 ]
        
        image = im.MatrixColor(image, custom_matrix) # This would be more efficient if we could do "custom_matrix * im.matrix.saturation(0.7)", but for some reason that's throwing errors.
        return im.MatrixColor(image, im.matrix.saturation(0.7))

    def dawn(image): # Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(0.5, 0.4, 0.6))

    def evening(image): # Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(0.6, 0.6, 0.7))

    def flip(image): # Basic Ren'Py Effect
        return im.Flip(image, horizontal=True)

    def ghost(image, a = 0.8): # Agent Gold
        return im.MatrixColor(image,  im.matrix.desaturate() * im.matrix.tint(0.71, 1.0, 0.95) * im.matrix.opacity(a))

    def gray(image, level=0.0): # Basic Ren'Py Effect
        # Allows the user to choose their level of gray scaling. Useful for gradual effects, but needs to be applied by hand.
        return im.MatrixColor(image, im.matrix.saturation(level))

    def morning(image): # Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(0.8, 0.7, 0.6))

    def night(image): # Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(0.4, 0.4, 0.6))

    def sepia(image): # Basic Ren'Py Effect
        return im.Sepia(image)

    def shadow(image): # Agent Gold
        return im.MatrixColor(image, im.matrix.colorize("#000", "#000"))

    def sunset(image): # Koya-Sato
        return im.MatrixColor(image, im.matrix.tint(1.0, 0.8, 0.8))

    def white(image): # Agent Gold
        return im.MatrixColor(image, im.matrix.colorize("#fff", "#fff"))

    # Used for applying filters to any image, even those not defined by the tool.
    def getCharacterImage(char, expression="1a"): # MAS Dev Team
        return renpy.display.image.images.get((char, expression), None)

