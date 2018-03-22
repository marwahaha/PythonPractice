import os
from tqdm import tqdm, trange
from time import sleep

def dosomething(buf):
    """Do something with the content of a file"""
    sleep(0.01)
    pass

def walkdir(folder):
    """Walk through each files in a directory"""
    for dirpath, dirs, files in os.walk(folder):
        for filename in files:
            yield os.path.abspath(os.path.join(dirpath, filename))

def process_content_with_progress2(inputpath, blocksize=1024):
    # Preprocess the total files count
    filecounter = 0
    for filepath in walkdir(inputpath):
        filecounter += 1

    for filepath in tqdm(walkdir(inputpath), total=filecounter, unit="files"):
        with open(filepath, 'rb') as fh:
            buf = 1
            while (buf):
                buf = fh.read(blocksize)
                dosomething(buf)