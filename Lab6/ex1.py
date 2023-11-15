import os
import sys


def read_files(d, ex):
    try:
        if os.path.isdir(d):
            for item in os.listdir(d):
                if os.path.isfile(d + '/' + item):
                    if item.split('.').pop() == ex:
                        try:
                            file = open(d + '/' + item, 'r')
                            print('Contents of ' + d + '/' + item + ':')
                            print(file.read())
                        except Exception:
                            raise Exception('Error: at opening file')

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
    extension = sys.argv[2]
    read_files(dirr, extension)
except Exception as e:
    print(e)
else:
    print('Done.')
