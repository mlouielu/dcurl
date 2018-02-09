import string
import random
import ctypes
import sys
import _thread
import time

import perf


NUM_TRYTES = 100

join_list = []
for i in range(NUM_TRYTES):
    join_list.append(_thread.allocate_lock())

def random_tx():
    return ''.join(random.choice(string.ascii_uppercase + "9") for _ in range(2673))

def random_trytes(amount):
    return [random_tx() for _ in range(amount)]

def call_dcurl(idx, mwm):
    tmp = str(trytes_list[idx]).encode('ascii')
    libdcurl.dcurl_entry(tmp, mwm)
    join_list[idx].release()

def run(cpus, gpus, mwm, trytes):
    dcurl_path = 'libdcurl.so'
    libdcurl = ctypes.cdll.LoadLibrary(dcurl_path)
    libdcurl.dcurl_init.argtypes = [ctypes.c_int, ctypes.c_int]
    libdcurl.dcurl_entry.argtypes = [ctypes.c_int, ctypes.c_int]

    libdcurl.dcurl_init(cpus, gpus)
    for i in range(NUM_TRYTES):
        join_list[i].acquire()
        _thread.start_new_thread(call_dcurl, (i, mwm,))

    for i in range(NUM_TRYTES):
        while join_list[i].locked():
            pass

    libdcurl.dcurl_destroy()

if __name__ == "__main__":
    cpus = int(sys.argv[1])
    gpus = int(sys.argv[2])
    mwm = int(sys.argv[3])

    trytes = read_trytes()

    perf.bench_func('IOTA POW', run, cpus, gpus, mwm, trytes)
