#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:48:06 2021

@author: adam
"""
import os
from netpyne import sim

# Make sure output directory exists
output_dir = 'data/v1_batch1/v1_batch1_0_0'
os.makedirs(output_dir, exist_ok=True)

# Read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='cfg.py', 
                                           netParamsDefault='netParams.py')

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

sim.pc.done()
#import sys
#sys.exit()
# h.quit()
