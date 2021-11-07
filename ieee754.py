def IEEE754(num):
    num=float(num)
    bias = 127
    num_bite = 32
    num_exposant = 8
    num_mantisse = 23
    if num < 0:
        signe = "1"
        num = num - (num * 2)
    else:
        signe = "0"


    n = 0
    fdec = ""
    unite = int(num)
    decimale = num - unite


    while True:
        decimale = decimale * 2

        intdec = str(int(decimale))
        fdec = fdec + intdec
        if decimale >= 1.0:
            decimale = decimale - 1.0
        if decimale == 0.0:
            break

    unite = bin(unite)[2:]
    fdec = bin(int(fdec))[2:]

    mantise = float(unite + "." + fdec)

    while mantise > 2:
        mantise = mantise * 10 ** -1
        n = n + 1
    mantise = str(round(mantise - 1, 12))[2:]


    for i in range(num_mantisse - len(mantise)):
        mantise = mantise + "0"

    exposant = str(round(int(bin(bias + n)[2:]), num_exposant))

    final = signe + exposant + mantise

    return(final)
