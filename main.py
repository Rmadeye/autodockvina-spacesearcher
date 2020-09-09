#!/usr/bin/env python3
from src import protein_prep, ligand_prep, perform_docking
import os, time, argparse
home = os.path.expanduser("~")


def execute(protein_ids: list, ligand_id: str):
    assert (os.path.isdir(home + '/MGLTools-1.5.6')), "AutoDockTools not found! Script stopped" # check if mgltools are present
    ligand_prep.LigandPreparer(ligand_id).prepare_ligand() # prepare ligand
    for protein in protein_ids:
        protein_prep.ProteinPreparer(protein).prepare_protein() # prepare protein
        perform_docking.VinaDocker(
            protein, ligand_id
        ).prepare_docking_grid_and_dock()

# start = time.time()
#
# inputdata = argparse.ArgumentParser(description="Process docking files")
#
# inputdata.add_argument('-ip', '--protein-pdb', nargs='*',
#                        help="Input protein entry from PDB", required=True, type=str)
# inputdata.add_argument('-il', '--ligand-cid', nargs='*',
#                        help="Input ligand CID PubChem entry", required=True, type=str)
# args = inputdata.parse_args()
#
# run = execute(args.protein_pdb[0], args.ligand_cid[0])


if __name__ == '__main__':
    ligand = '11234'
    proteins = ['4pxz','1llp']
    execute(proteins, ligand)
