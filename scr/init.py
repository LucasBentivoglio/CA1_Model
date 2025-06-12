#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:48:06 2021

@author: adam
"""
import os
from netpyne import sim

# Read cfg and netParams from command line arguments if available; otherwise use default
simConfig, netParams = sim.readCmdLineArgs(simConfigDefault='scr/cfg.py', 
                                           netParamsDefault='scr/netParams.py')

# Make sure output directory exists
output_dir = simConfig.saveFolder
os.makedirs(output_dir, exist_ok=True)

# Create network and run simulation
sim.createSimulateAnalyze(netParams=netParams, simConfig=simConfig)

sim.pc.done()
#import sys
#sys.exit()
# h.quit()
