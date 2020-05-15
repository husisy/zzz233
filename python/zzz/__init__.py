import os
import pickle
import urllib.request
import urllib.error

def check_internet_available(timeout=1):
    host = 'https://www.google.com' #dnsloopup google.com #172.217.161.142 (20190817)
    try:
        urllib.request.urlopen(host, timeout=timeout)
        return True
    except urllib.error.URLError:
        return False


def hfp(**kwargs):
    z0 = globals()
    for k,v in kwargs.items():
        if k in z0:
            print('WARNING: "{}" alreay in globals()'.format(k))
        z0[k] = v


def to_pickle(**kwargs):
    if os.path.exists('tbd00.pkl'):
        with open('tbd00.pkl', 'rb') as fid:
            z0 = pickle.load(fid)
        z0.update(**kwargs)
    else:
        z0 = kwargs
    with open('tbd00.pkl', 'wb') as fid:
        pickle.dump(z0, fid)


def from_pickle(key):
    with open('tbd00.pkl', 'rb') as fid:
        return pickle.load(fid)[key]
