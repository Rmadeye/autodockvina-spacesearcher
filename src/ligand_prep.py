import os, shutil
from time import sleep
#set preparation pathways
prepare_ligand_path = '~/MGLTools-1.5.6/bin/pythonsh ~/MGLTools-1.5.6/MGLToolsPckgs/AutoDockTools/Utilities24/prepare_ligand4.py -A bonds_hydrogens -U nphs_lps -l'

class LigandPreparer:

    def __init__(self, smile: str, dir: str):
        self.ligand = smile
        self.tmpdir = dir

    def prepare_ligand(self):
        with open(self.tmpdir+'/'+self.ligand+'.smi', 'w') as smile_input_file:
            smile_input_file.write(self.ligand)

        os.system('obabel "{}" -O "{}" --gen3d'.format(
            self.tmpdir + '/' + self.ligand + '.smi', self.tmpdir + '/' + self.ligand + 'prep.pdb'))
        # generates 3d coords
        os.system(
            'obminimize -ff GAFF "{}" > "{}"'.format(
                self.tmpdir + '/' + self.ligand + 'prep.pdb', self.tmpdir + '/' + self.ligand + '.pdb'
                                                 )
        )
        #minimizes using GAFF
        os.system(prepare_ligand_path + '"{}"'.format(self.tmpdir + '/' + self.ligand + '.pdb'
                                                    )) # adds charges, sets rotatable bonds
        shutil.move(self.ligand + '.pdbqt', self.tmpdir)
