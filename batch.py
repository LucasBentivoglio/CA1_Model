#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:34:42 2021

@author: adam
"""

from netpyne import specs
from netpyne.batch import Batch
import os

#froam neuron import h
#h.nrnmpi_init()

def batchTauWeight():

    params = specs.ODict()
    
    seedbase = 576667
    
    # Example: only one value of artifperpyr and one seed
    params['artifperpyr'] = [140]
    params['seedval'] = list(range(0 + seedbase, 100 + seedbase, 100))  # This gives [576667]
    
    # Define batch object with parameters to explore
    b = Batch(params=params, cfgFile='cfg.py', netParamsFile='netParams.py')
    
    # Set batch metadata
    b.batchLabel = 'v1_batch1'
    b.saveFolder = 'data/' + b.batchLabel
    b.method = 'grid'

    # Automatically create output folder if it doesn't exist
    if not os.path.exists(b.saveFolder):
        os.makedirs(b.saveFolder)
    
    # LOCAL EXECUTION (not SLURM)
    doslurm = True    
    if doslurm:
        b.runCfg = {
            'type': 'hpc_slurm',
            'allocation': 'TG-MED240050',
            'partition': 'shared',
            'walltime': '2:00:00',
            'nodes': 24,
            'coresPerNode': 128,
            'email': 'lucas16edu@gmail.com',
            'folder': '/home/lbentivoglio/CA1_Model/',
            'script': 'init.py',
            'mpiCommand': 'mpirun',
            'custom': '#SBATCH --mem=240G\n#SBATCH --export=ALL\n#SBATCH --partition=shared',
            'skip': True
        }
    # else:
    #     b.runCfg = {
    #         'type': 'mpi_direct',
    #         'cores': 4,  # Adjust if needed
    #         'mpiCommand': 'mpiexec',  # Use 'mpiexec' for local execution
    #         'script': 'init.py',
    #         'skip': False  # <<< this must be False to actually run
    #     }
    
    # Run the batch simulations
    b.run()

# Main code
if __name__ == '__main__':
    batchTauWeight()
    import sys
    sys.exit()
