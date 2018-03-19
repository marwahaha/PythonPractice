import os
from tqdm import tqdm, trange
from time import sleep

def dosomething(buf):
    """Do something with the content of a file"""
    sleep(0.00001)
    pass

def walkdir(folder):
    """Walk through each files in a directory"""
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))


def process_content_with_progress3(inputpath, blocksize=1024):
    # Preprocess the total files sizes
    sizecounter = 0
    for filepath in tqdm(walkdir(inputpath), unit="files"):
        sizecounter += os.stat(filepath).st_size

    # Load tqdm with size counter instead of file counter
    with tqdm(total=sizecounter,
              unit='B', unit_scale=True, unit_divisor=1024) as pbar:
        for filepath in walkdir(inputpath):
            with open(filepath, 'rb') as fh:
                buf = 1
                while (buf):
                    buf = fh.read(blocksize)
                    dosomething(buf)
                    if buf:
                        pbar.set_postfix(file=filepath[-10:], refresh=False)
                        pbar.update(len(buf))

process_content_with_progress3("/mnt/temp")