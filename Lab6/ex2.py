import os
import sys


def rename_files(d):
    nr = 0
    name = 'image'
    try:
        if os.path.isdir(d):
            for item in os.listdir(d):
                if os.path.isfile(d + '/' + item):
                    nr += 1
                    parts = item.split('.')
                    last = parts.pop()
                    print(item + " a fost redenumit in " + name + str(nr) + '.' + last)
                    os.rename(d + '/' + item, d + '/' + name + str(nr) + '.' + last)

    except FileNotFoundError:
        raise Exception('Error: ' + d + ' not found')
    except PermissionError:
        raise Exception('Error: permission denied for ' + d)
    except OSError as o:
        raise Exception('Error: OSError', o)
    except Exception:
        raise Exception('Error: other file access issues')


try:
    dirr = sys.argv[1]
    rename_files(dirr)
except Exception as e:
    print(e)
else:
    print('Done.')
