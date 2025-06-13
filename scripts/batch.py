#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:34:42 2021

@author: adam
"""

from netpyne import specs
from netpyne.batch import Batch
from pathlib import Path  
import os

#froam neuron import h
#h.nrnmpi_init()

def batchTauWeight():

    # --- Início da Lógica de Caminho Dinâmico ---
    # Obtém o caminho absoluto do script atual (batch.py)
    script_path = Path(__file__).resolve()
    # Define o diretório raiz do projeto (CA1_Model) subindo um nível (de 'scripts')
    project_root = script_path.parent.parent

    # Cria os caminhos absolutos para os arquivos de configuração
    cfg_file = project_root / 'src' / 'cfg.py'
    net_params_file = project_root / 'src' / 'netParams.py'
    
    # Cria o caminho absoluto para o diretório de saída
    batch_label = 'v1_batch1'
    output_dir = project_root / 'data' / 'processed' / batch_label
    
    # Garante que o diretório de saída exista
    # `parents=True` cria diretórios pais, se necessário. `exist_ok=True` não gera erro se o diretório já existir.
    output_dir.mkdir(parents=True, exist_ok=True)
    # --- Fim da Lógica de Caminho Dinâmico ---

    params = specs.ODict()
    
    seedbase = 576667
    
    # Example: only one value of artifperpyr and one seed
    params['artifperpyr'] = [140]
    params['seedval'] = list(range(0 + seedbase, 100 + seedbase, 100))  # This gives [576667]
    
    # Define batch object with parameters to explore
    b = Batch(params=params, cfgFile=str(cfg_file), netParamsFile=str(net_params_file))
    
    # Define os metadados do lote
    b.batchLabel = batch_label
    b.saveFolder = str(output_dir)  # Usa o caminho absoluto para a pasta de salvamento
    b.method = 'grid'

    # Automatically create output folder if it doesn't exist
    #if not os.path.exists(b.saveFolder):
    #    os.makedirs(b.saveFolder)
    
    # LOCAL EXECUTION (not SLURM)
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
            'folder': '/home/lbentivoglio/CA1_Model/',
            'script': 'src/init.py',
            'mpiCommand': 'mpirun',
            'custom': '#SBATCH --mem=240G\n#SBATCH --export=ALL\n#SBATCH --partition=compute',
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
