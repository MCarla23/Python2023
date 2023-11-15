import os
import sys


def calc_total_size(d):
    try:
        if os.path.isdir(d):
            sumi = 0
            for item in os.listdir(d):
                sumi += calc_total_size(d+'/'+item)
            return sumi
        else:
            return os.stat(d).st_size
    except FileNotFoundError:
        raise FileNotFoundError('Error: ' + d + ' not found')
    except PermissionError:
        raise PermissionError('Error: permission denied for ' + d)
    except Exception:
        raise Exception("Error: other file access issues")


try:
    dirr = sys.argv[1]
    tsize = calc_total_size(dirr)
except Exception as e:
    print(e)
else:
    print('Total size of all files in directory ' + dirr + ' is ' + str(tsize) + ' bytes.')
