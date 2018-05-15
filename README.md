# pyWinSpec

This module is for reading SPE files created by WinSpec with Princeton Instruments' cameras. 
It defines the structures used in the 2.6 versions of 
[WinSpec](http://www.princetoninstruments.com/products/software/). The definitions were taken 
from 2.6B version of the manual. 

In principle, this package can also read the LightField data, as long as no
additional metadata is written per-frame. The header field of these files does 
not store any information however. Pull requests that add support of the 3.x file format are welcome

The `SpeFile` class takes an input path, stores header information and returns a numpy array 
of the appropriate shape.

# Requirements

- Numpy
- Python 2.7 or 3.5+

# Usage

    >>> from winspec import SpeFile
    >>> SpeFile('baseline.SPE')
    SPE File /Users/aloukian/Documents/pywinspec/baseline.SPE
        268x1 area, 10000 frames
        Taken on 16Jan2013
    >>> SpeFile('baseline.SPE').data
    array([[[16862],
            [16945],
            [16927],
            ..., 
            [13513],
            [13476],
            [13440]],
            ..., 
            [[17223],
            [17293],
            [17283],
            ..., 
            [13736],
            [13703],
            [13665]]], dtype=uint16)


# Changelog

- *0.2.1* - added wavelength axis field
- *0.2* - backport improvements from the analysis package, port to python 3.
    *WARNING* When the ADC setting is set to '100 KHz,' the pixel data are now
    reversed by winspec to undo the reversal done by the camera. 
- *0.1* - first commit, working on python 2.7

# License

Copyright (c) 2013-2018, Anton Loukianov
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

