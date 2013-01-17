from structs import Header, AxisCalibration, ROIinfo
from os import path

import numpy as np
        

def print_headers():
    ''' Print the attribute names, sizes and offsets in the C structure
    
    Assuming that the sizes are correct and add up to an offset of 4100 bytes, 
    everything should add up correctly. This information was taken from the 
    WinSpec 2.6 Spectroscopy Software User Manual version 2.6B, page 251.

    If this table doesn't add up, something changed in the definitions of the 
    datatype widths. Fix this in winspec.structs file and let me know!
    '''

    import inspect, re, io

    A = Header()
    f.readinto(A)
    
    for i in [Header, AxisCalibration, ROIinfo]:
        fields = []

        print '{:20s}[{:4s}]\toffset'.format(str(i), 'size')
        
        for name,obj in inspect.getmembers(i):
            if inspect.isdatadescriptor(obj) and not inspect.ismemberdescriptor(obj) \
                and not inspect.isgetsetdescriptor(obj):
                
                fields.append((name, obj))

        fields.sort(key=lambda x: re.search('(?<=ofs=)([0-9]+)', str(x[1])).group(0), 
                cmp=lambda x,y: cmp(int(x),int(y))); fields

        for name, obj in fields:
            print '{:20s}[{:3d}]\toff={:4d}'.format(name, obj.size, obj.offset)

class SpeFile(object):
    ''' A file that represents the SPE file.

    All details written in the file are contained in the `header` structure. Data is 
    accessed by using the `data` property.

    Once the object is created and data accessed, the file is NOT read again. Create
    a new object if you want to reread the file.
    '''

    # Map between header datatype field and numpy datatype 
    _datatype_map = {0 : np.float32, 1 : np.int32, 2 : np.int16, 3 : np.uint16}

    def __init__(self, name):
        ''' Open file `name` to read the header.'''

        with file(name, mode='rb') as f:
            self.header = Header()
            self.path = path.realpath(name) 
            self._data = None

            # Deprecated method, but FileIO apparently can't be used with numpy
            f.readinto(self.header)

    def _read(self):
        ''' Read the data segment of the file and create an appropriately-shaped numpy array

        Based on the header, the right datatype is selected and returned as a numpy array.  I took 
        the convention that the frame index is the first, followed by the x,y coordinates.
        '''

        if self._data is not None:
            return self._data

        # In python 2.7, apparently file and FileIO cannot be used interchangably
        with file(self.path, mode='r') as f:
            f.seek(4100) # Skip header (4100 bytes)

            _count = self.header.xdim * self.header.ydim * self.header.NumFrames
            
            self._data = np.fromfile(f, dtype=SpeFile._datatype_map[self.header.datatype], count=_count)

            # Also, apparently the ordering of the data corresponds to how it is stored by the shift register
            # Thus, it appears a little backwards...
            self._data = self._data.reshape((self.header.NumFrames, self.header.ydim, self.header.xdim))

            # Orient the structure so that it is indexed like [NumFrames][x, y]
            self._data = np.rollaxis(self._data, 2, 1)

            return self._data

    ''' Data recorded in the file, returned as a numpy array. 
    
    The convention for indexes is that the first index is the frame index, followed by x,y region of 
    interest.
    '''
    data = property(fget=_read)

    def __repr__(self):
        return 'SPE File {:s}\n\t{:d}x{:d} area, {:d} frames\n\tTaken on {:s}' \
                .format(self.path, self.header.xdim, self.header.ydim, self.header.NumFrames, self.header.date)
