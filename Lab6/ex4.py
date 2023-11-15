import os
import sys

fr = {}


def nr_of_files(d):
    try:
        if os.path.isdir(d):
            for item in os.listdir(d):
                nr_of_files(d+'/'+item)
        elif os.path.isfile(d):
            ext = os.path.splitext(d)[1]
            if ext in fr:
                fr[str(ext)] += 1
            else:
                fr[str(ext)] = 1
        os.stat(d)

    except FileNotFoundError:
        raise Exception('Error: ' + d + ' not found')
    except PermissionError:
        raise Exception('Error: permission denied for ' + d)
    except Exception:
        raise Exception("Error: other file access issues")


try:
    dirr = sys.argv[1]
    nr_of_files(dirr)
except Exception as e:
    print(e)
else:
    print('The number of files with each extension in the given directory ' + dirr + ' is: ' + str(fr) + '.')
