"""VideoCapture.py

by Markus Gritsch <gritsch@iue.tuwien.ac.at>

"""

import vidcap
import time, string

default_textpos = 'bl' # t=top, b=bottom;   l=left, c=center, r=right
textcolor = 0xffffff
shadowcolor = 0x000000

def now():
    """Returns a string containing the current date and time.

    This function is used internally by VideoCapture to generate the timestamp
    with which a snapshot can optionally be marked.

    """
    weekday = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
    #weekday = ('Mo', 'Di', 'Mi', 'Do', 'Fr', 'Sa', 'So')
    #weekday = ('-', '-', '-', '-', '-', '-', '-')
    y, m, d, hr, min, sec, wd, jd, dst = time.localtime(time.time())
    return '%s:%s:%s %s %s.%s.%s' % (string.zfill(hr, 2), string.zfill(min, 2), string.zfill(sec, 2), weekday[wd], d, m, y)

class Device:
    """Create instances of this class which will then represent video devices.

    For the lifetime of the instance, the device is blocked, so it can not be
    used by other applications (which is quite normal Windows behavior).
    If you want to access the device from another program, you have to delete
    the instance first (e.g. del cam).

    """
    def __init__(self, devnum=0, showVideoWindow=0):
        """devnum:  VideoCapture enumerates the available video capture devices
                    on your system.  If you have more than one device, specify
                    the desired one here.  The device number starts from 0.

           showVideoWindow: 0 ... do not display a video window (the default)
                            1 ... display a video window

                            Mainly used for debugging, since the video window
                            can not be closed or moved around.

        """
        self.dev = vidcap.new_Dev(devnum, showVideoWindow)

    def displayPropertyPage(self):
        """deprecated

        Use the methods displayCaptureFilterProperties() and
        displayCapturePinProperties() instead.

        """
        print 'WARNING: displayPropertyPage() is deprecated.'
        print '         Use displayCaptureFilterProperties() and displayCapturePinProperties()'
        print '         instead!'
        self.dev.displaypropertypage()

    def displayCaptureFilterProperties(self):
        """Displays a dialog containing the property page of the capture filter.

        For VfW drivers you may find the option to select the resolution most
        likele here.

        """
        self.dev.displaycapturefilterproperties()

    def displayCapturePinProperties(self):
        """Displays a dialog containing the property page of the capture pin.

        For WDM drivers you may find the option to select the resolution most
        likele here.

        """
        self.dev.displaycapturepinproperties()

    def setResolution(self, width, height):
        """Sets the capture resolution. (without dialog)

        (contributed by Don Kimber <kimber@fxpal.com>)

        """
        self.dev.setresolution(width, height)

    def getBuffer(self):
        """Returns a string containing the raw pixel data.

        You probably don't want to use this function, but rather getImage() or
        saveSnapshot().

        """
        return self.dev.getbuffer()

if __name__ == '__main__':
    import shutil
    shutil.copy('VideoCapture.py', 'C:\Python20\Lib')
    shutil.copy('VideoCapture.py', 'C:\Python21\Lib')
    shutil.copy('VideoCapture.py', 'C:\Python22\Lib')
    shutil.copy('VideoCapture.py', 'C:\Python23\Lib')
    shutil.copy('VideoCapture.py', 'C:\Python24\Lib')
    shutil.copy('VideoCapture.py', 'C:\Python25\Lib')
    #~ cam = Device(devnum=0)
    #~ #cam.displayPropertyPage() ## deprecated
    #~ #cam.displayCaptureFilterProperties()
    #~ #cam.displayCapturePinProperties()
    #~ #cam.setResolution(768, 576) ## PAL
    #~ #cam.setResolution(352, 288) ## CIF
    #~ cam.saveSnapshot('test.jpg', quality=75, timestamp=3, boldfont=1)