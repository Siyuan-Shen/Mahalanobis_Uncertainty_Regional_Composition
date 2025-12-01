import numpy as np
import netCDF4 as nc
import os
import mat73 as mat
from data_func.utils import Resampled_Training_BLISCO_data_outdir
from map_uncertainty_func.utils import Estimation_outdir


def save_absoulute_uncertainty_map(absolute_uncertainty_map,species,version,special_name,YYYY,MM,obs_version,nearby_sites_number):
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Absolute_Uncertainty_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'RawObs-{}_pixels_nearby_{}_sites_absolute_uncertainty_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    print(f'Saving absolute uncertainty map to {outfile}')
    np.save(outfile, absolute_uncertainty_map)
    return

def load_absolute_uncertainty_map(species,version,special_name,YYYY,MM,obs_version,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Absolute_Uncertainty_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    infile = indir + 'RawObs-{}_pixels_nearby_{}_sites_absolute_uncertainty_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    absolute_uncertainty_map = np.load(infile)
    return absolute_uncertainty_map

def load_estimation_map_data(YYYY:str, MM:str,SPECIES:str, version:str, special_name):
    indir = Estimation_outdir + '{}/{}/Map_Estimation/{}/'.format(SPECIES,version,YYYY)
    infile = indir + '{}_{}_{}{}{}.nc'.format(SPECIES,version,YYYY,MM,special_name)
    MapData = nc.Dataset(infile)
    lat = MapData.variables['lat'][:]
    lon = MapData.variables['lon'][:]
    SPECIES_Map = MapData.variables[SPECIES][:]
    SPECIES_Map = np.array(SPECIES_Map)
    return SPECIES_Map, lat, lon

def save_rRMSE_map(rRMSE_uncertainty_map,species,version,YYYY,MM,obs_version,nearby_sites_number):
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/rRMSE_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'RawObs-{}_pixels_nearby_{}_sites_rRMSE_uncertainty_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    np.save(outfile, rRMSE_uncertainty_map)
    return
def load_rRMSE_map(species,version,YYYY,MM,obs_version,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/rRMSE_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    infile = indir + 'RawObs-{}_pixels_nearby_{}_sites_rRMSE_uncertainty_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    rRMSE_uncertainty_map = np.load(infile)
    return rRMSE_uncertainty_map

def load_bins_LOWESS_values(species,version,special_name,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Mahalanobis_distance_LOWESS_values/'.format(species,version)
    infile = indir + '{}_nearby_sites-{}{}_Mahalanobis_distance_LOWESS_values.npy'.format( species,nearby_sites_number,special_name)
    bins_LOWESS_values = np.load(infile,allow_pickle=True).item()
    Mahalanobis_distance_bin_centers = bins_LOWESS_values['Mahalanobis_distance_bin_centers']
    WINTER_LOWESS_values = bins_LOWESS_values['WINTER_LOWESS_values']
    SPRING_LOWESS_values = bins_LOWESS_values['SPRING_LOWESS_values']
    SUMMER_LOWESS_values = bins_LOWESS_values['SUMMER_LOWESS_values']
    AUTUMN_LOWESS_values = bins_LOWESS_values['AUTUMN_LOWESS_values']
    ALL_LOWESS_values = bins_LOWESS_values['ALL_LOWESS_values']
    
    return Mahalanobis_distance_bin_centers,WINTER_LOWESS_values,SPRING_LOWESS_values,SUMMER_LOWESS_values,AUTUMN_LOWESS_values,ALL_LOWESS_values

def save_mahalanobis_distance_map(mahalanobis_distance_map,species,version,YYYY,MM,obs_version,nearby_sites_number):
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Mahalanobis_distance_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'RawObs-{}_pixels_nearby_{}_sites_mahalanobis_distance_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    np.save(outfile, mahalanobis_distance_map)
    return
def load_mahalanobis_distance_map(species,version,YYYY,MM,obs_version,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Mahalanobis_distance_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    infile = indir + 'RawObs-{}_pixels_nearby_{}_sites_mahalanobis_distance_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    mahalanobis_distance_map = np.load(infile)
    return mahalanobis_distance_map

def save_pixel_nearby_sites_index_map(nearby_sites_training_data_indices,species,version,YYYY,MM,obs_version,nearby_sites_number):
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Nearby_sites_indices/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'RawObs-{}_pixels_nearby_{}_sites_index_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    np.save(outfile, nearby_sites_training_data_indices)
    return

def load_pixels_nearest_sites_indices_map(species,version,YYYY,MM,obs_version,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Nearby_sites_indices/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    infile = indir + 'RawObs-{}_pixels_nearby_{}_sites_index_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    nearby_sites_training_data_indices = np.load(infile)
    return nearby_sites_training_data_indices

def save_local_reference_map(local_reference_for_channels_map,species,version,YYYY,MM,obs_version,nearby_sites_number):
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Local_reference_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile = outdir + 'RawObs-{}_pixels_nearby_{}_sites_local_reference_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    np.save(outfile, local_reference_for_channels_map)
    return

def load_local_reference_map(species,version,YYYY,MM,obs_version,nearby_sites_number):
    indir = Resampled_Training_BLISCO_data_outdir + '{}/{}/Local_reference_Map/sitesnumber-{}/{}/'.format(species,version,nearby_sites_number,YYYY)
    infile = indir + 'RawObs-{}_pixels_nearby_{}_sites_local_reference_map_{}{}.npy'.format(obs_version,nearby_sites_number,YYYY,MM)
    local_reference_for_channels_map = np.load(infile,allow_pickle=True).item()
    return local_reference_for_channels_map

def load_mapdata(infile):
    mapdata = np.load(infile)
    if len(np.where(np.isnan(mapdata)==True)):
        mapdata[np.where(np.isnan(mapdata)==True)] = np.mean(mapdata[np.where(np.isnan(mapdata)==False)])
    return mapdata

def get_landtype(YYYY,extent)->np.array:
    #landtype_infile = '/my-projects/Projects/MLCNN_PM25_2021/data/inputdata/Other_Variables_MAP_INPUT/{}/MCD12C1_LandCoverMap_{}.npy'.format(YYYY,YYYY)
    #landtype = np.load(landtype_infile)
    Mask_indir = '/my-projects/mask/NA_Masks/Cropped_NA_Masks/'
    '''
    Contiguous_US_data = nc.Dataset(Mask_indir+'Cropped_REGIONMASK-Contiguous United States.nc')
    Canada_data        = nc.Dataset(Mask_indir+'Cropped_REGIONMASK-Canada.nc')
    Alaska_data        = nc.Dataset(Mask_indir+'Cropped_REGIONMASK-Alaska.nc')
    Contiguous_US_mask = np.array(Contiguous_US_data['regionmask'][:])
    Canada_mask        = np.array(Canada_data['regionmask'][:])
    Alaska_mask        = np.array(Alaska_data['regionmask'][:])
    landtype = Contiguous_US_mask + Canada_mask + Alaska_mask
    lat_index,lon_index = get_extent_index(extent=extent)
    '''
    landtype_infile = '/my-projects/mask/Land_Ocean_Mask/NewLandMask-0.01.mat'
    LandMask = mat.loadmat(landtype_infile)
    MASKp1 = LandMask['MASKp1']
    MASKp2 = LandMask['MASKp2']
    MASKp3 = LandMask['MASKp3']
    MASKp4 = LandMask['MASKp4']
    MASKp5 = LandMask['MASKp5']
    MASKp6 = LandMask['MASKp6']
    MASKp7 = LandMask['MASKp7']
    MASKp_land = MASKp1 +MASKp2 + MASKp3 + MASKp4 + MASKp5 + MASKp6 + MASKp7 
    landtype = np.zeros((13000,36000),dtype=np.float32)
    landtype = MASKp_land
    lat_index,lon_index = get_GL_extent_index(extent=extent)
    
    output = np.zeros((len(lat_index),len(lon_index)), dtype=int)

    for ix in range(len(lat_index)):
        output[ix,:] = landtype[lat_index[ix],lon_index]
    return output
def get_GL_extent_index(extent)->np.array:
    '''
    :param extent:
        The range of the input. [Bottom_Lat, Up_Lat, Left_Lon, Right_Lon]
    :return:
        lat_index, lon_index
    '''
    SATLAT = np.load('/my-projects2/Projects/MLCNN_PM25_2021/data/tSATLAT.npy')
    SATLON = np.load('/my-projects2/Projects/MLCNN_PM25_2021/data/tSATLON.npy')
    lat_index = np.where((SATLAT >= extent[0])&(SATLAT<=extent[1]))
    lon_index = np.where((SATLON >= extent[2])&(SATLON<=extent[3]))
    lat_index = np.squeeze(np.array(lat_index))
    lon_index = np.squeeze(np.array(lon_index))
    return lat_index,lon_index
