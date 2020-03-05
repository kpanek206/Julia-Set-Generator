import numpy


def generate_julia():
    """generates julia set fractal"""

    w = int(input('Podaj szerokość obrazka: '))
    h = int(input('Podaj wysokość obrazka: '))
    f = float(input('Podaj cyfrę pomiędzy 0 i 1: '))
    name_input = input('Podaj nazwę pliku: ')

    re_min = -2.0
    re_max = 2.00
    im_min = -2.0
    im_max = 2.0
    name = (str(name_input) + '.pgm')
    c = complex(0.0, f)
    real_range = numpy.arange(re_min, re_max, (re_max - re_min) / w)
    image_range = numpy.arange(im_max, im_min, (im_min - im_max) / h)
    output = open(name, 'w')
    output.write('P2\n# Julia Set image\n' + str(w) + ' ' + str(h) + '\n255\n')
    for im in image_range:
        for re in real_range:
            z = complex(re, im)
            n = 255
            while abs(z) < 10 and n >= 5:
                z = z * z + c
                n -= 5
            output.write(str(n) + ' ')
        output.write('\n')
    output.close()

    print('Stworzono obrazek ' + name)


generate_julia()
