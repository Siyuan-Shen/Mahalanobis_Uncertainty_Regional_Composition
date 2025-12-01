
from map_uncertainty_func.iostream import load_absolute_uncertainty_map,load_estimation_map_data,load_mahalanobis_distance_map,load_rRMSE_map
import numpy as np
from visualization_pkg.iostream import get_absolute_uncertainty_filepath,get_map_estimation_filepath,get_mahalanobis_distance_filepath, get_rRMSE_uncertainty_filepath,get_rRMSE_uncertainty_filepath
from visualization_pkg.map_plot_func import Plot_Map_estimation_Map_Figures,Plot_absolute_Uncertainty_Map_Figures,Plot_Mahalanobis_distance_Map_Figures, Plot_rRMSE_Uncertainty_Map_Figures

from visualization_pkg.utils import extent


def plot_map_estimation_data(species,map_estimation_version,YYYY,MM,map_estimation_special_name):
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12','Annual']
    print(f"Plotting map estimation data for species: {species}, version: {map_estimation_version}, date: {YYYY}-{MONTH[MM]}")
    plot_map = np.zeros((6000,13000),dtype=np.float64)
    if MM != 12:
        map_data, lat, lon = load_estimation_map_data(YYYY=YYYY, MM=MONTH[MM], SPECIES=species, version=map_estimation_version, special_name=map_estimation_special_name)
        plot_map[5:5995,5:12995] = map_data
    else:
        for m in range(12):
            monthly_map, lat, lon = load_estimation_map_data(YYYY=YYYY, MM=MONTH[m], SPECIES=species, version=map_estimation_version, special_name=map_estimation_special_name)
            plot_map[5:5995,5:12995] += monthly_map
        plot_map = plot_map / 12.0
    map_estiamtion_filepath = get_map_estimation_filepath(species=species,version=map_estimation_version,YYYY=YYYY,MM=MONTH[MM],special_name=map_estimation_special_name)
    SATLAT = np.linspace(10.005,69.995,6000)
    SATLON = np.linspace(-169.995,-40.005,13000)
    vmax_dic = {
        'PM25': 20,
        'SO4' : 4,
        'NO3' : 4,
        'NH4' : 2,
        'OM'  : 8,
        'BC'  : 1,
        'DUST': 2,
        'SS'  : 1
    }
    Plot_Map_estimation_Map_Figures(species=species,map_estimation_map=plot_map,extent=extent,
                                        Mahalanobis_LAT=SATLAT, Mahalanobis_LON=SATLON,
                                        YYYY=YYYY,MM=MONTH[MM],
                                        outfile=map_estiamtion_filepath,
                                        vmin=0,vmax=vmax_dic[species])
    return
    
def plot_absolute_uncertainty_map(species,version,special_name,YYYY,MM,obs_version,nearby_sites_number,vmin,vmax):
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12','Annual']
    print(f"Plotting absolute uncertainty map for species: {species}, version: {version}, date: {YYYY}-{MONTH[MM]}, obs_version: {obs_version}, nearby_sites_number: {nearby_sites_number}")
    absolute_uncertainty_filepath = get_absolute_uncertainty_filepath(species=species,version=version,special_name=special_name,YYYY=YYYY,MM=MONTH[MM],
                                                                   obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    absolute_uncertainty_map = load_absolute_uncertainty_map(species=species,version=version,special_name=special_name,YYYY=YYYY,MM=MONTH[MM],
                                                           obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    SATLAT = np.linspace(10.005,69.995,6000)
    SATLON = np.linspace(-169.995,-40.005,13000)
    Plot_absolute_Uncertainty_Map_Figures(species=species,absolute_uncertainty_map=absolute_uncertainty_map,extent=extent,
                                       Mahalanobis_LAT=SATLAT, Mahalanobis_LON=SATLON,
                                       YYYY=YYYY,MM=MONTH[MM],
                                       outfile=absolute_uncertainty_filepath,
                                       vmin=vmin,vmax=vmax)
    return
def plot_rRMSE_uncertainty_map(species,version,YYYY,MM,obs_version,nearby_sites_number,vmin,vmax):
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12','Annual']
    print(f"Plotting rRMSE uncertainty map for species: {species}, version: {version}, date: {YYYY}-{MONTH[MM]}, obs_version: {obs_version}, nearby_sites_number: {nearby_sites_number}")
    rRMSE_uncertainty_map = load_rRMSE_map(species=species,version=version,YYYY=YYYY,MM=MONTH[MM],
                                           obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    
    rRMSE_uncertainty_filepath = get_rRMSE_uncertainty_filepath(species=species,version=version,YYYY=YYYY,MM=MONTH[MM],
                                                               obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    SATLAT = np.linspace(10.005,69.995,6000)
    SATLON = np.linspace(-169.995,-40.005,13000)

    Plot_rRMSE_Uncertainty_Map_Figures(species=species,rRMSE_uncertainty_map=rRMSE_uncertainty_map,extent=extent,
                                       Mahalanobis_LAT=SATLAT, Mahalanobis_LON=SATLON,
                                       YYYY=YYYY,MM=MONTH[MM],
                                       outfile=rRMSE_uncertainty_filepath,
                                       vmin=vmin,vmax=vmax)

    return 



def plot_mahalanobis_distance_map(species,version,YYYY,MM,obs_version,nearby_sites_number):
    MONTH = ['01','02','03','04','05','06','07','08','09','10','11','12','Annual']
    print(f"Plotting Mahalanobis distance map for species: {species}, version: {version}, date: {YYYY}-{MONTH[MM]}, obs_version: {obs_version}, nearby_sites_number: {nearby_sites_number}")
    mahalanobis_distance_map = load_mahalanobis_distance_map(species=species,version=version,YYYY=YYYY,MM=MONTH[MM],
                                                             obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    
    mahalanobis_distance_filepath = get_mahalanobis_distance_filepath(species=species,version=version,YYYY=YYYY,MM=MONTH[MM],
                                                                     obs_version=obs_version,nearby_sites_number=nearby_sites_number)
    SATLAT = np.linspace(10.005,69.995,6000)
    SATLON = np.linspace(-169.995,-40.005,13000)

    Plot_Mahalanobis_distance_Map_Figures(species=species,mahalanobis_distance_map=mahalanobis_distance_map,extent=extent,
                                         Mahalanobis_LAT=SATLAT, Mahalanobis_LON=SATLON,
                                         YYYY=YYYY,MM=MONTH[MM],
                                         outfile=mahalanobis_distance_filepath)

    return 