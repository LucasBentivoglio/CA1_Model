#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:34:42 2021

@author: adam
"""
from netpyne import specs
from netpyne.batch import Batch

#froam neuron import h
#h.nrnmpi_init()

def batchTauWeight():

    params = specs.ODict()
    
    seedbase = 576667
    
    #params['artifperpyr'] = [130 + x*4 for x in range(20)] 
    params['artifperpyr'] = [140]
    params['seedval'] = list(range(0 + seedbase, 100 + seedbase, 100)) 
    
    b = Batch(params=params, cfgFile='src/cfg.py', netParamsFile='src/netParams.py',)

 
    b.batchLabel = 'v1_batch1'
    b.saveFolder = 'data/v1_batch1'
    b.method = 'grid'
    
    doslurm = True    
    if doslurm:
        b.runCfg = {
            'type': 'hpc_slurm',
            'allocation': 'TG-MED240050',
            'partition': 'compute',
            'walltime': '2:00:00',
            'nodes': 8,
            'coresPerNode': 128,
            'email': 'lucas16edu@gmail.com',
            'folder': '/home/lbentivoglio/CA1_Model_Teste/',
            'script': 'src/init.py',
            'mpiCommand': 'mpirun',
            'custom': '#SBATCH --mem=240G\n#SBATCH --export=ALL\n#SBATCH --partition=compute',
            'skip': False
        }
    # else:
   

    
    #     b.runCfg = {  'type': 'mpi_direct',
    #             'cores': 10,
    #             'mpiCommand': 'mpiexec --use-hwthread-cpus',
    #                     'script': 'src/init.py',
    #                     'skip': True}
    
    

    # Run batch simulations
    b.run()
    #h.quit()
# Main code
if __name__ == '__main__':
        batchTauWeight()
        import sys
        sys.exit()
