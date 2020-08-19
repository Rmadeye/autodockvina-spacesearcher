import urllib.request

import os, shutil
#set preparation pathways
prepare_ligand_path = '~/MGLTools-1.5.6/bin/pythonsh ~/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -A bonds_hydrogens -U nphs_lps -l'

class LigandPreparer:

    def __init__(self, ligand_file: str):
        self.ligand = ligand_file

    def prepare_ligand(self):
        url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{}/SDF'.format(self.ligand)
        urllib.request.urlretrieve(url, '{}'.format(self.ligand + '.sdf')) # downloads the file
        os.system('obabel {} -O {} --gen3d'.format(self.ligand+'.sdf', self.ligand + 'prep.pdb')) # generates 3d coords
        os.system('obminimize -ff GAFF {} > {}'.format(self.ligand + 'prep.pdb', self.ligand + '.pdb')) # minimizes using GAFF
        os.system(prepare_ligand_path + '{}'.format(self.ligand + '.pdb')) # adds charges, sets rotatable bonds
        try:
            shutil.move(self.ligand+'.sdf', './ligand_sdfs/')
            shutil.move(self.ligand+'.pdbqt', './ligand_pdbqts/')
            os.remove(self.ligand + 'prep.pdb')
            os.remove(self.ligand + '.pdb')
        except Exception as e:
            print(e)
            os.remove(self.ligand + '.sdf')
            os.remove(self.ligand + '.pdb')
            os.remove(self.ligand + 'prep.pdb')
            os.remove(self.ligand + '.pdbqt')




