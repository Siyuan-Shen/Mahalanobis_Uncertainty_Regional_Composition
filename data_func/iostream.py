import numpy as np
import netCDF4 as nc
import os
from data_func.utils import AVD_version, Obs_version, TrainingData_indir, BLISCO_indir,Resampled_Training_BLISCO_data_outdir 

def load_RawObs_training_data(channel_lists, species, version, special_name, AVD_version, Obs_version, start_year, end_year, width, height):

    data_indir = TrainingData_indir + '{}/RawData-{}/{}/{}/Seperated_TrainingChannels/'.format(species, Obs_version, AVD_version, version)

    total_data = {}
    for channel in channel_lists:
        if channel == 'GeoBC' or channel == 'GeoOM' or channel == 'GeoDUST' or channel == 'GeoSS' or channel == 'GeoNIT' or channel == 'GeoNH4' or channel == 'GeoSO4':
            infile = data_indir + '{}-cnn_TrainingData_{}_{}x{}_{}01-{}12{}.npy'.format(species, channel, width, height, start_year, end_year, special_name)
        else:
            infile = data_indir + '{}-cnn_TrainingData_{}_{}x{}_{}01-{}12.npy'.format(species, channel, width, height, start_year, end_year)
        total_data[channel] = np.load(infile)[:,int((width-1)/2),int((height-1)/2)]

    return total_data

def load_month_based_BLISCO_data_recording(species, version, typeName, beginyear, endyear,
                                           nchannel, special_name, width, height,
                                           buffer_radius_list, BLCO_kfold, BLCO_seeds_number):

    indir = BLISCO_indir + '{}/{}/Results/results-SelfIsolated_BLCO_DataRecording/'.format(species, version)
    BLISCO_obs_data_recording = {}
    BLISCO_final_data_recording = {}
    BLISCO_test_sites_index_recording = {}
    BLISCO_train_sites_index_recording = {}
    BLISCO_training_obs_data_recording = {}
    for buffer_radius in buffer_radius_list:
        BLISCO_obs_data_recording[buffer_radius] = {}
        BLISCO_final_data_recording[buffer_radius] = {}
        BLISCO_test_sites_index_recording[buffer_radius] = {}
        BLISCO_train_sites_index_recording[buffer_radius] = {}
        BLISCO_training_obs_data_recording[buffer_radius] = {}
        obs_data_infile =  indir + '{}-{}-Obs-BLCODataRecording_{}km_{}-folds_{}-ClusterSeeds_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species,buffer_radius, BLCO_kfold,BLCO_seeds_number, beginyear, endyear,width, height, nchannel,special_name)
        final_data_infile = indir + '{}-{}-Final-BLCODataRecording_{}km_{}-folds_{}-ClusterSeeds_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species,buffer_radius, BLCO_kfold,BLCO_seeds_number, beginyear, endyear,width, height, nchannel,special_name)
        test_sites_index_recording_infile =  indir + '{}-{}-test_sites_index_recording-BLCODataRecording_{}km_{}-folds_{}-ClusterSeeds_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, buffer_radius,BLCO_kfold,BLCO_seeds_number, beginyear, endyear,width, height, nchannel,special_name)
        train_sites_index_recording_infile = indir + '{}-{}-train_sites_index_recording-BLCODataRecording_{}km_{}-folds_{}-ClusterSeeds_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, buffer_radius,BLCO_kfold,BLCO_seeds_number, beginyear, endyear,width, height, nchannel,special_name)
        training_obs_data_infile = indir + '{}-{}-training_obs_data-BLCODataRecording_{}km_{}-folds_{}-ClusterSeeds_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, buffer_radius,BLCO_kfold,BLCO_seeds_number, beginyear, endyear,width, height, nchannel,special_name)
        obs_data = np.load(obs_data_infile,allow_pickle=True).item()
        final_data = np.load(final_data_infile,allow_pickle=True).item()
        test_sites_index_recording = np.load(test_sites_index_recording_infile, allow_pickle=True).item()
        train_sites_index_recording = np.load(train_sites_index_recording_infile, allow_pickle=True).item()
        training_obs_data = np.load(training_obs_data_infile, allow_pickle=True).item()
        BLISCO_obs_data_recording[buffer_radius] = obs_data
        BLISCO_final_data_recording[buffer_radius] = final_data
        BLISCO_test_sites_index_recording[buffer_radius] = test_sites_index_recording
        BLISCO_train_sites_index_recording[buffer_radius] = train_sites_index_recording
        BLISCO_training_obs_data_recording[buffer_radius] = training_obs_data
    return BLISCO_obs_data_recording, BLISCO_final_data_recording, BLISCO_test_sites_index_recording, BLISCO_train_sites_index_recording, BLISCO_training_obs_data_recording


def save_training_and_BLISCO_data(resampled_RawObs_testing_site_input_data,resampled_RawObs_training_site_input_data,
                                  BLISCO_obs_data_recording, BLISCO_final_data_recording,
                                  species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height):
    """
    Save training and BLISCO data to a .npy file.

    Parameters:
    data (numpy.ndarray): The training data to be saved.
    outfile (str): The path to the output .npy file.
    """
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)

    # Save the data
    resampled_training_data_outfile = outdir + '{}-{}-Resampled_RawObs_Training_and_BLISCOData_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, startyear, endyear, width, height, nchannel, special_name)
    np.save(resampled_training_data_outfile, {
        'resampled_RawObs_testing_site_input_data': resampled_RawObs_testing_site_input_data,
        'resampled_RawObs_training_site_input_data': resampled_RawObs_training_site_input_data,
        'BLISCO_obs_data_recording': BLISCO_obs_data_recording,
        'BLISCO_final_data_recording': BLISCO_final_data_recording
    })
    
def load_training_and_BLISCO_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height):
    """
    Load training and BLISCO data from a .npy file.

    Parameters:
    infile (str): The path to the input .npy file.

    Returns:
    dict: The loaded training and BLISCO data.
    """
    infile = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version) + '{}-{}-Resampled_RawObs_Training_and_BLISCOData_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, startyear, endyear, width, height, nchannel, special_name)
    data = np.load(infile, allow_pickle=True).item()
    return data

def save_BLISCO_data(BLISCO_obs_data_recording, BLISCO_final_data_recording,
                                  species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height):
    """
    Save BLISCO data to a .npy file.
    Parameters:
    data (numpy.ndarray): The BLISCO data to be saved.
    outfile (str): The path to the output .npy file.
    """
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    # Save the data
    BLISCO_data_outfile = outdir + '{}-{}-BLISCOData_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, startyear,
                                                                                            endyear, width, height, nchannel, special_name)
    np.save(BLISCO_data_outfile, {
        'BLISCO_obs_data_recording': BLISCO_obs_data_recording,
        'BLISCO_final_data_recording': BLISCO_final_data_recording
    })  
    return

def load_BLISCO_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height):
    """
    Load BLISCO data from a .npy file.
    Parameters:
    infile (str): The path to the input .npy file.
    Returns:
    dict: The loaded BLISCO data.
    """
    infile = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version) + '{}-{}-BLISCOData_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, startyear,
                                                                                            endyear, width, height, nchannel, special_name)
    data = np.load(infile, allow_pickle=True).item()
    return data

def save_mahalanobis_distance_data(EachMonth_EachYear_Martix_Mahalanobis_distance_recording, EachMonth_AllYear_Martix_Mahalanobis_distance_recording, AllMonth_AllYear_Martix_Mahalanobis_distance_recording,
                                   species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height, nearby_sites_number):
    """
    Save Mahalanobis distance recording data to a .npy file.

    Parameters:
    mahalanobis_distance_recording (dict): The Mahalanobis distance recording data to be saved.
    outfile (str): The path to the output .npy file.
    """
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}-{}-{}_sites_nearby-MahalanobisDistance_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, nearby_sites_number, startyear, endyear, width, height, nchannel, special_name)
    np.save(outfile, {
        'EachMonth_EachYear_Martix_Mahalanobis_distance_recording': EachMonth_EachYear_Martix_Mahalanobis_distance_recording,
        'EachMonth_AllYear_Martix_Mahalanobis_distance_recording': EachMonth_AllYear_Martix_Mahalanobis_distance_recording,
        'AllMonth_AllYear_Martix_Mahalanobis_distance_recording': AllMonth_AllYear_Martix_Mahalanobis_distance_recording
    })

    return

def load_mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height, nearby_sites_number):
    """
    Load Mahalanobis distance recording data from a .npy file.

    Parameters:
    infile (str): The path to the input .npy file.

    Returns:
    dict: The loaded Mahalanobis distance recording data.
    """
    infile = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version) + '{}-{}-{}_sites_nearby-MahalanobisDistance_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, nearby_sites_number, startyear, endyear, width, height, nchannel, special_name)
    data = np.load(infile, allow_pickle=True).item()
    return data

def save_nearby_sites_index_reference_data(nearby_sites_index_dict, nearby_sites_channel_reference_dict,
                                           species, version, typeName, startyear, endyear,
                                           nchannel, special_name, width, height, nearby_sites_number):
    """
    Save nearby sites index and channel reference data to a .npy file.
    Parameters:
    data (numpy.ndarray): The nearby sites index and channel reference data to be saved.
    outfile (str): The path to the output .npy file.
    """
    outdir = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version)
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    outfile = outdir + '{}-{}-{}_sites_nearby-NearbySitesIndexAndChannelReference_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, nearby_sites_number, startyear, endyear, width, height, nchannel, special_name)
    np.save(outfile, {
        'nearby_sites_index_dict': nearby_sites_index_dict,
        'nearby_sites_channel_reference_dict': nearby_sites_channel_reference_dict
    })
    return

def load_nearby_sites_index_reference_data(species, version, typeName, startyear, endyear,
                                             nchannel, special_name, width, height, nearby_sites_number):
     """
     Load nearby sites index and channel reference data from a .npy file.
     Parameters:
     infile (str): The path to the input .npy file.
     Returns:
     dict: The loaded nearby sites index and channel reference data.
     """
     infile = Resampled_Training_BLISCO_data_outdir + '{}/{}/'.format(species, version) + '{}-{}-{}_sites_nearby-NearbySitesIndexAndChannelReference_{}-{}_{}x{}_{}Channel{}.npy'.format(typeName, species, nearby_sites_number, startyear, endyear, width, height, nchannel, special_name)
     data = np.load(infile, allow_pickle=True).item()
     return data
 
def load_RawObservation(speices):
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/monthly_observation/RawData-{}/'.format(Obs_version)
    infile = indir + '{}_monthly_observations-Threshold5.nc'.format(speices)
    dataset = nc.Dataset(infile)
    obsdata = dataset.variables[speices][:]
    obs_lat = dataset.variables['latitude'][:]
    obs_lon = dataset.variables['longitude'][:]
    return obsdata, obs_lat, obs_lon

def load_NA_GeoLatLon():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA.npy'
    lon_infile = indir + 'tSATLON_NA.npy'
    NA_GeoLAT = np.load(lat_infile)
    NA_GeoLON = np.load(lon_infile)
    return NA_GeoLAT, NA_GeoLON

def load_NA_GeoLatLon_Map():
    indir = '/my-projects/Projects/PM25_Speices_DL_2023/data/input_variables_map/'
    lat_infile = indir + 'tSATLAT_NA_MAP.npy'
    lon_infile = indir + 'tSATLON_NA_MAP.npy'
    NA_GeoLAT_MAP = np.load(lat_infile)
    NA_GeoLON_MAP = np.load(lon_infile)
    return NA_GeoLAT_MAP, NA_GeoLON_MAP
