#!/usr/bin/env python
"""
/*******************************************************************************
 * Copyright (c) cortical.io GmbH. All rights reserved.
 *  
 * This software is confidential and proprietary information.
 * You shall use it only in accordance with the terms of the
 * license agreement you entered into with cortical.io GmbH.
 ******************************************************************************/
"""
class Fingerprint(object):
    def __init__(self, positions=None):
        #Get Fingerprint Positions.
        self.positions = positions # list[int]
        
