pyWinSpec
=========

This module is for reading SPE files created by WinSpec with Princeton Instruments' cameras. 
It defines the structures used in the 2.6 versions of 
[WinSpec](http://www.princetoninstruments.com/products/software/). The definitions were taken 
from 2.6B version of the manual. 

The `SpeFile` class takes an input path, stores header information and returns a numpy array 
of the appropriate shape. 

Requirements
============

- Numpy
- Python 2.7

Usage
=====

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

License
=======

Copyright (c) 2013, Anton Loukianov 
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

