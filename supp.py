import os
import time


def screen_name(name):
    named_tuple = time.localtime()  # get struct_time
    tm = time.strftime("__%m_%d_%Y__%H_%M_%S", named_tuple)
    return 'scr_%s_%s.png' % (name, tm)
