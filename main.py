#!/usr/bin/env python3
from src import protein_prep, ligand_prep, perform_docking
import os, time, argparse
home = os.path.expanduser("~")


def execute(protein_id, ligand_id):
    assert (os.path.isdir(home + '/MGLTools-1.5.6')), "AutoDockTools not found! Script stopped" # check if mgltools are present
    protein_prep.ProteinPreparer(protein_id).prepare_protein() # prepare protein
    ligand_prep.LigandPreparer(ligand_id).prepare_ligand() # prepare ligand
    perform_docking.VinaDocker(
        protein_id, ligand_id
    ).prepare_docking_grid_and_dock()

start = time.time()

inputdata = argparse.ArgumentParser(description="Process docking files")

inputdata.add_argument('-ip', '--protein-pdb', nargs='*',
                       help="Input protein entry from PDB", required=True, type=str)
inputdata.add_argument('-il', '--ligand-cid', nargs='*',
                       help="Input ligand CID PubChem entry", required=True, type=str)
args = inputdata.parse_args()

run = execute(args.protein_pdb[0], args.ligand_cid[0])
