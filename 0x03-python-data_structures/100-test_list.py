import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctype.py_object]
l = ['hello', 'world']
lib.print_python_list_info(l)
del l[l]
lib.print_python_list_infor(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "Holderton"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info

