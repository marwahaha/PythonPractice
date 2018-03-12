import pytsk3
import pyewf


class EWFImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle):
        self._ewf_handle = ewf_handle
        super(EWFImgInfo, self).__init__(url="",
                                         type=pytsk3.TSK_IMG_TYPE_EXTERNAL)

    def close(self):
        self._ewf_handle.close()

    def read(self, offset, size):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()

def main(image, img_type, offset):
    #If there are multiple e01 image files, they will be put together in a list
    if img_type == "ewf":
        filenames = pyewf.glob(image)

        #Making the handle object
        ewf_handle = pyewf.handle()
        ewf_handle.open(filenames)

        #Open the PYTSK3 handle on ewf image
        img_info = EWFImgInfo(ewf_handle)

    else:
        img_info = pytsk3.Img_Info(image)

    #Filesystem handle to iterate through the filesystem
    fs = pytsk3.FS_Info(img_info ,offset)