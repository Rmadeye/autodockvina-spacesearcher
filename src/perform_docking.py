import os, shutil
from biopandas.pdb import PandasPdb


class VinaDocker:

    def __init__(self, protein_pdbqt: str, ligand_pdbqt: str):
        self.protein = protein_pdbqt
        self.ligand = ligand_pdbqt

    def prepare_docking_grid_and_dock(self):
        df = PandasPdb().read_pdb(self.protein).df['ATOM']
        minx = df['x_coord'].min()
        maxx = df['x_coord'].max()
        cent_x = round((maxx + minx) / 2,2)
        size_x = round(abs(maxx - minx) + 3,2)
        miny = df['y_coord'].min()
        maxy = df['y_coord'].max()
        cent_y = round((maxy + miny) / 2,2)
        size_y = round(abs(maxy - miny) + 3,2)
        minz = df['z_coord'].min()
        maxz = df['z_coord'].max()
        cent_z = round((maxz + minz) / 2,2)
        size_z = round(abs(maxz - minz) + 3,2)
        print("Center point of docking grid for {} is as follows: "
              "x: {}, y: {}, z: {}".format(self.protein, size_x, size_y, size_z))
        print("Sizes of docking grid are as follows:"
              "x: {}, y: {}, z: {}".format(cent_x,cent_y,cent_z))
        os.system('vina --receptor {} --ligand {} --center_x {} --center_y {} --center_z {} --size_x {} --size_y {} --size_z {}'.format(self.protein,
                                                               self.ligand,
                                                               cent_x,
                                                               cent_y,
                                                               cent_z,
                                                               size_x,
                                                               size_y,
                                                               size_z))

    # def dock(self):

