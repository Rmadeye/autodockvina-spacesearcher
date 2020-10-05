#!/usr/bin/env python3
from src import protein_prep, ligand_prep, perform_docking
import os, tempfile

home = os.path.expanduser("~")


def execute(PDB_list: list, CID_list: list):
    assert (os.path.isdir(
        home + '/MGLTools-1.5.6')), "AutoDockTools not found! Script stopped"  # check if mgltools are present

    for CID_entry in CID_list:
        with tempfile.TemporaryDirectory(dir=os.getcwd()) as tmpdir:
            ligand_prep.LigandPreparer(CID_entry, dir=tmpdir).prepare_ligand()
            for PDB_entry in PDB_list:
                protein_prep.ProteinPreparer(PDB_entry, dir=tmpdir).prepare_protein()
                perform_docking.VinaDocker(protentry=PDB_entry,
                                           ligentry=CID_entry,
                                           protein_pdbqt=tmpdir + '/' + PDB_entry,
                                           ligand_pdbqt=tmpdir + '/' + CID_entry,
                                           dir=tmpdir
                                           ).dock_merge_plip()


if __name__ == '__main__':
    ligand = ['2244']
    proteins = ['3e4e', '1w0e', '2xml', '6c01', '4qbq', '1fx9', '4ln7', '2a8x', '1hkb', '3dkg', '6d6t', '3ggf', '2igq',
                '4nh9']
    execute(proteins, ligand)
