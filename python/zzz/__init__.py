import os
import pickle
import urllib.request
import urllib.error
import numpy as np

def check_internet_available(timeout=1):
    host = 'https://www.google.com' #dnsloopup google.com #172.217.161.142 (20190817)
    try:
        urllib.request.urlopen(host, timeout=timeout)
        return True
    except urllib.error.URLError:
        return False


def hfp(**kwargs):
    # TODO fail on winOS
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


def to_np(x):
    # not a good idea to use isinstance()
    # if use isinstance(), here have to import all of them (tf/torch/cupy)
    tmp0 = str(type(x))[8:-2]
    if tmp0.startswith('tensorflow'):
        ret = x.numpy()
    elif tmp0.startswith('torch'):
        ret = x.detach().to('cpu').numpy()
    elif tmp0.startswith('cupy'):
        ret = x.get()
    else:
        ret = np.asarray(x)
    return ret

def hfe(x, y, eps=1e-5):
    x = to_np(x)
    y = to_np(y)
    ret = np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))
    return ret

# a simple hfe()
# hfe = lambda x,y,eps=1e-3: np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))


def moving_average(np0, num=3):
    # see https://stackoverflow.com/q/13728392/7290857
    kernel = np.ones(num) / num
    ret = np.convolve(np.asarray(np0), kernel, mode='same')
    return ret
