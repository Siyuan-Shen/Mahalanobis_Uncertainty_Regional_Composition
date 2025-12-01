import numpy as np
import math

AVD_version = 'gPM25-20240604'
Obs_version = '20241015'
compute1= False
local_laptop = True

GCC_version                         = 'MERRASPEC-GCV11.GLandNested-20240607-RH35-199801-202312-wSA'

if compute1:
    # Training data directories
    TrainingData_indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/TrainingDatasets/'
    BLISCO_indir = '/my-projects/Projects/PM25_Speices_DL_2023/code/Training_Evaluation_Estimation/'
    Resampled_Training_BLISCO_data_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/code/Manuscript_Figures/Mahalanobis_distance_uncertainty_calculation_plot/data/'
    Figure_outdir = '/my-projects/Projects/PM25_Speices_DL_2023/code/Manuscript_Figures/Mahalanobis_distance_uncertainty_calculation_plot/figures/'
# Local laptop directories  
if local_laptop:
    TrainingData_indir = '/Volumes/rvmartin/Active/s.siyuan/Projects/PM25_Speices_DL_2023/data/TrainingDatasets/'
    BLISCO_indir = '/Volumes/rvmartin/Active/s.siyuan/Projects/PM25_Speices_DL_2023/code/Training_Evaluation_Estimation/'
    Resampled_Training_BLISCO_data_outdir = '/Volumes/rvmartin/Active/s.siyuan/Projects/PM25_Speices_DL_2023/code/Manuscript_Figures/Mahalanobis_distance_uncertainty_calculation_plot/data/'
    Figure_outdir = '/Volumes/rvmartin/Active/s.siyuan/Projects/PM25_Speices_DL_2023/code/Manuscript_Figures/Mahalanobis_distance_uncertainty_calculation_plot/figures/'

sites_number_dict = {
    'PM25': 3062,
    'SO4' : 695,
    'NO3' : 695,
    'NH4' : 695,
    'OM'  : 695,
    'BC'  : 695,
    'DUST': 639,
    'SS'  : 695
}


def neighbors_haversine_indices(train_lat, train_lon, test_lat, test_lon, k):
    try:
        from sklearn.neighbors import NearestNeighbors
        train_rad = np.c_[np.radians(train_lat), np.radians(train_lon)]
        test_rad  = np.c_[np.radians(test_lat),  np.radians(test_lon)]
        k = int(min(k, len(train_rad)))
        if k <= 0:
            return np.empty((len(test_rad), 0), dtype=np.int64)
        nn = NearestNeighbors(n_neighbors=k, algorithm='ball_tree', metric='haversine')
        nn.fit(train_rad)
        _, idx = nn.kneighbors(test_rad, n_neighbors=k, return_distance=True)
        return idx.astype(np.int64, copy=False)
    except Exception:
        # Fallback uses the pure NumPy implementation defined above
        return batch_topk_indices(test_lat, test_lon, train_lat, train_lon, k)



def Get_typeName(bias, normalize_bias, normalize_species, absolute_species, log_species, species):
    if bias == True:
        typeName = '{}-bias'.format(species)
    elif normalize_bias:
        typeName = 'Normalized-{}-bias'.format(species)
    elif normalize_species == True:
        typeName = 'Normaized-{}'.format(species)
    elif absolute_species == True:
        typeName = 'Absolute-{}'.format(species)
    elif log_species == True:
        typeName = 'Log-{}'.format(species)
    return  typeName