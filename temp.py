# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import dicom
import os
import numpy

ds = dicom.read_file("C:/Users/ASUS/Downloads/bmode.dcm")
ds1 = dicom.read_file("C:/Users/ASUS/Downloads/ttfm.dcm")

print(ds)
print(ds1)
