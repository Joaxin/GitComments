import sys
for arg in sys.argv:
    try:
        f = open(arg, 'r', errors='ignore')
        s = f.readline()
    except OSError as err:
        print("OS error: {0}".format(err))
    except IOError:
        print('cannot open', arg)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        print(arg, 'has', len(f.readlines())+1, 'lines')
        f.close()