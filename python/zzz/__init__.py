import os
import shutil
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


def known_hosts(ipkey=None, tag_backup=True):
    '''
    since windows-platform doesn't support drop ssh-key from powershell

    usage
        python -c "import zzz; zzz.known_hosts()" #query all known-hosts
        python -c "import zzz; zzz.known_hosts('[123.45.67.89]:2022')" #pop [123.45.67.89]:2022
    '''
    # see https://stackoverflow.com/a/33243564/7290857
    known_hosts_path = os.path.expanduser(os.path.join('~','.ssh','known_hosts'))
    with open(known_hosts_path) as fid:
        z0 = [x.strip() for x in fid]
        z0 = [x.split() for x in z0 if x]
    if ipkey is None:
        print('ipkey\t key-type\t data')
        for ipkey, key_type, data in z0:
            print(ipkey, key_type, data[:10], sep='\t')
    else:
        tmp0 = [x for x,y in enumerate(z0) if y[0]==ipkey]
        if len(tmp0)==0:
            print('ipkey="{}" not found'.format(ipkey))
        else:
            if tag_backup:
                shutil.copyfile(known_hosts_path, 'known_hosts') #copy to local
            assert len(tmp0)==1
            z0.pop(tmp0[0])
            with open(known_hosts_path, 'w', encoding='utf-8') as fid:
                for x in z0:
                    fid.write(' '.join(x) + '\n')
