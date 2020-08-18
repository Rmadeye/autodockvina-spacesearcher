from src import protein_prep, ligand_prep, perform_docking
import os
home = os.path.expanduser("~")

def execute(protein_id, ligand_id):
    assert (os.path.isdir(home + '/MGLTools-1.5.6')), "AutoDockTools not found! Script stopped"
    protein_prep.ProteinPreparer(protein_id).prepare_protein()
    ligand_prep.LigandPreparer(ligand_id).prepare_ligand()
    perform_docking.VinaDocker('./protein_pdbqts/4pxz.pdbqt','./ligand_pdbqts/31154.pdbqt').prepare_docking_grid_and_dock()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    execute('4pxz', '31154')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
