#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lib.graffiti import generate_graffiti_address


string = "Zero"

print('Write graffiti "' + string + '" to blockchain by sending some haks to:\n')
print(generate_graffiti_address(string))
