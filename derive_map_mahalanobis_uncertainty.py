from map_uncertainty_func.Assemble_func import Get_absolute_uncertainty_map,Convert_mahalanobis_distance_map_to_uncertainty,Calculate_Mahalanobis_distance,Get_nearby_sites_indices_map, Get_local_reference_for_channels
from data_func.utils import Get_typeName, AVD_version, Obs_version
from visualization_pkg.Assemble_func import plot_mahalanobis_distance_map, plot_rRMSE_uncertainty_map,plot_absolute_uncertainty_map,plot_map_estimation_data
import argparse
import numpy as np


parser=argparse.ArgumentParser()

parser.add_argument('--SPECIES_list',  nargs='+',type = str)
parser.add_argument('--desire_year_list',  nargs='+',type = int)
SPECIES_list = parser.parse_args().SPECIES_list
desire_year_list = parser.parse_args().desire_year_list

### Main functions Switches

Get_the_nearby_sites_indices_map_Switch = False # Run once to get the nearby sites indices map, then set it to False. Only set it True if you change to a new Observation version or nearby sites number.
Get_local_reference_map_Switch = False # Run once to get the local reference map, then set it to False. Only set it True if you change to a new Observation version, include new variables, or nearby sites number.

Get_mahalanobis_distance_map_Switch = False # Run once to get the Mahalanobis distance map, then set it to False. Only set it True if you change to a new Observation version, include new variables, or nearby sites number.
Plot_mahalanobis_distance_map_switch = False # After getting the Mahalanobis distance map, set it to True to plot the figures.

Get_uncertainty_rRMSE_map_Switch = False # Before getting the map, run the file mahalanobis_distance_uncertainty_test.ipynb to get the relationship between Mahalanobis distance and rRMSE.
Plot_rRMSE_uncertainty_map_Switch = False # After getting the rRMSE uncertainty map, set it to True to plot the figures.

Get_absolute_uncertainty_map_Switch = False # Multiple the rRMSE uncertainty map with the estimation map to get the absolute uncertainty map.
Plot_absolute_uncertainty_map_Switch = True # After getting the absolute uncertainty map, set it to True to plot the figures.

Plot_Map_estimation_Switch = True # Plot the map estimation data.

plot_months = [0,6,12]  # The months to plot the rRMSE uncertainty map.

if 'PM25' in SPECIES_list:
    species = 'PM25'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 34
    special_name = '_BenchMark'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = [
                    'AOD', 'GeoPM25','ETA', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias',
                    'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT',
                    'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi',
                    'DST_offline_emi',
                    'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                    'Urban_Builtup_Lands',
                    'minor_roads',
                    'Month_of_Year',
                    'Lat', 'Lon', 'elevation',
                    'Population'
                    ]
    local_nearby_sites_number = 30
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
                
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    
    
    if Plot_rRMSE_uncertainty_map_Switch:
        vmin_list = [0.25 , 0.25, 0.15, 0.25]
        vmax_list = [0.65 , 1.2 , 0.90,  1.0]
        for YYYY in desire_year_list:
            for MM in plot_months:
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=special_name,
                                            map_estimation_version=version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [5, 5, 10, 5, 5]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_version=version,YYYY=YYYY,MM=MM,map_estimation_special_name=special_name)
                
                
local_nearby_sites_number = 20
if 'NO3' in SPECIES_list:
    species = 'NO3'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 43
    special_name = '_BenchMark_AllYEAR_TwoModels_withThreeStarsVariables-1-3-4'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = ['AOD','ETA', 'GeoPM25','EtaAOD_Bias', 'EtaMixing', 'EtaSGAOD_Bias', 
                    'GeoNIT','GeoBC','GeoNH4','GeoSO4','GeoOM','GeoDUST','GeoSS',
                    'NA_CNN_PM25',
                    'GC_NIT',  'GC_SO4', 'GC_SOA', 'GC_PM25', 'GC_BC', 'GC_NH4', 'GC_DST','GC_SSLT','GC_OM',
                    'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'SO2_anthro_emi',
                    'DST_offline_emi','SSLT_offline_emi',
                    'RH', 'T2M', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    'Urban_Builtup_Lands','Croplands',
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',
                    'Population' ] 
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.5, 0.6, 0.5, 0.25]
                vmax_list = [0.8, 1.5, 1.2, 0.4]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=special_name,
                                            map_estimation_version=version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [2, 2, 2, 2, 2]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_version=version,YYYY=YYYY,MM=MM,map_estimation_special_name=special_name)
                
if 'SO4' in SPECIES_list:
    species = 'SO4'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 39
    special_name = '_BenchMark_AllYEAR_TwoModels'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = ['AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoSO4','GeoNH4','GeoNIT','GeoBC','GeoOM','GeoDUST','GeoSS',
                    'NA_CNN_PM25',
                    'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_DST','GC_PM25', 'GC_BC','GC_OM','GC_SSLT',#'GC_NIT', #'GC_OC',
                    'NH3_anthro_emi','NO_anthro_emi','SO2_anthro_emi',
                     'SSLT_offline_emi',
                    'T2M', 'RH', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    'Urban_Builtup_Lands',
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',
                   #'Population'
                    ] 
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.3, 0.2, 0.3, 0.2]
                vmax_list = [0.8, 0.6, 0.8, 0.6]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=special_name,
                                            map_estimation_version=version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [2, 2, 2, 2, 2]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_version=version,YYYY=YYYY,MM=MM,map_estimation_special_name=special_name)
if 'NH4' in SPECIES_list:
    species = 'NH4'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 38
    special_name = '_BenchMark_AllYEAR_TwoModels_withThreeStarsVariables'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = [ 'AOD','EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias','GeoPM25','ETA',
                    'GeoNH4','GeoSO4','GeoBC','GeoOM','GeoDUST','GeoNIT',
                    'NA_CNN_PM25',
                     'GC_SO4', 'GC_SOA',  'GC_BC','GC_PM25', 'GC_NH4', 'GC_DST','GC_SSLT','GC_OM',
                     'SSLT_offline_emi',
                    'T2M', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    'Urban_Builtup_Lands','Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands',
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',
                    'Population'
                    ] 
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)
    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.3, 0.2, 0.3, 0.3]
                vmax_list = [0.8, 1.2, 0.8, 0.8]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=special_name,
                                            map_estimation_version=version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [2, 2, 2, 2, 2]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_version=version,YYYY=YYYY,MM=MM,map_estimation_special_name=special_name)
                
if 'BC' in SPECIES_list:
    species = 'BC'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=False, normalize_bias=False, normalize_species=True, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 39
    special_name = '_BenchMark_AllYEAR_TwoModels'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = ['AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoBC','GeoSO4','GeoNH4','GeoNIT','GeoOM','GeoSS',
                    'NA_CNN_PM25',
                    'GC_SOA', 'GC_SO4',  'GC_BC', 'GC_PM25', 'GC_NH4',  'GC_DST','GC_SSLT','GC_NIT',# #'GC_OC','GC_OM','
                    'BC_anthro_emi','OC_anthro_emi',
                    'T2M', 'U10M', 'V10M','PBLH', 'RH', 'PRECTOT',
                    'Urban_Builtup_Lands',
                    'log_motorway','log_primary',
                    'major_roads',
                     'Month_of_Year',
                    'Lat', 'Lon','elevation'
                    ] 
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.5, 0.4, 0.5, 0.4]
                vmax_list = [0.8, 0.9, 1.0, 0.8]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=special_name,
                                            map_estimation_version=version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [1, 1, 1, 1, 1]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_version=version,YYYY=YYYY,MM=MM,map_estimation_special_name=special_name)
if 'OM' in SPECIES_list:
    species = 'OM'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 33
    special_name = '_BenchMark_withThreeStarVariables-Threshold5_EveryTenYearsModels'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = [ 'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA',
                    'GeoOM','GeoSO4','GeoNIT','GeoSS',
                    'NA_CNN_PM25',
                    'GC_SOA', 'GC_OM', 'GC_PM25',  'GC_BC', 'GC_NIT', 
                    'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi','NMVOC_anthro_emi', 'SO2_anthro_emi',
                    'DST_offline_emi',
                    'RH', 'T2M', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    'Urban_Builtup_Lands',
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',
                    ] 
    map_estimation_version = 'v1.8.1'
    map_estimation_special_name = '_BenchMark_withThreeStarVariables'
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)

    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                                species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.4, 0.3, 0.3, 0.4]
                vmax_list = [0.8, 0.8, 1.2, 0.6]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=map_estimation_special_name,
                                            map_estimation_version=map_estimation_version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [2, 2, 4, 2, 4]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,YYYY=YYYY,MM=MM,
                                         map_estimation_version=map_estimation_version,
                                         map_estimation_special_name=map_estimation_special_name)
if 'DUST' in SPECIES_list:
    species = 'DUST'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 32
    special_name = '_BenchMark_AllYEAR_TwoModels_Epoch51_withThreeStarVariables-Threshold5'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = ['AOD',  'EtaSGAOD_Bias',
                'GeoBC','GeoDUST','GeoNH4','GeoNIT','GeoSO4','GeoSS',
                'NA_CNN_PM25',
                'GC_PM25', 'GC_SOA','GC_DST', 'GC_NH4', 'GC_NIT','GC_SO4',   'GC_BC', 'GC_SSLT','GC_OM',# #'GC_OC',
                'OC_anthro_emi',  'SO2_anthro_emi',
                'SSLT_offline_emi',
                'RH', 'T2M', 'PBLH','USTAR', 'PRECTOT',
                'Urban_Builtup_Lands',
                'unclassified',
                'Month_of_Year',
                'Lat', 'Lon','elevation',
                #'Population'
                ] 
    map_estimation_version = 'v1.8.1'
    map_estimation_special_name = '_BenchMark_AllYEAR_TwoModels_Epoch51_withThreeStarVariables'

    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)

    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
        Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.8, 0.5, 0.6, 0.5]
                vmax_list = [1.2, 0.9, 1.0, 0.9]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=map_estimation_special_name,
                                            map_estimation_version=map_estimation_version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [1, 1, 2, 1, 1]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_special_name=map_estimation_special_name,map_estimation_version=map_estimation_version,YYYY=YYYY,MM=MM)
if 'SS' in SPECIES_list:
    species = 'SS'
    version = 'v1.8.1'
    typeName = Get_typeName(bias=True, normalize_bias=False, normalize_species=False, absolute_species=False, log_species=False, species=species)
    startyear = 2000
    endyear = 2023
    nchannel = 42
    special_name = '_BenchMark_twoModels-Threshold5'
    width = 11
    height = 11
    training_data_version = 'NA_PM25-v1.8.0'
    training_data_special_name = '_BenchMark'
    buffer_radius_list = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
    BLCO_kfold = 10
    BLCO_seeds_number = 10
    channel_lists = [ 'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoSS','GeoBC','GeoNH4','GeoNIT','GeoSO4','GeoOM','GeoDUST',
                    'NA_CNN_PM25',
                    'GC_SO4','GC_PM25', 'GC_NH4',   'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM','GC_NIT', #'GC_OC',
                    'SO2_anthro_emi','NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi','NMVOC_anthro_emi',####'N2O_anthro_emi',,# 
                    'DST_offline_emi',
                    'RH', 'T2M', 'U10M', 'V10M','PBLH','PRECTOT',
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',
                    ] 
    map_estimation_version = 'v1.8.1'
    map_estimation_special_name = '_BenchMark_AllYear_twoModels_exclude_SS_Emi'
    if Get_the_nearby_sites_indices_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_nearby_sites_indices_map(species=species,version=version,nearby_sites_number=local_nearby_sites_number,
                                             YYYY=YYYY,MM=MM)
    if Get_local_reference_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_local_reference_for_channels(channel_lists=channel_lists,
                                                species=species,version=version,NA_CNN_version=training_data_version,
                                                NorthAmerica_PM25_special_name=training_data_special_name,
                                                AVD_version=AVD_version,Obs_version=Obs_version,
                                                start_year=startyear,end_year=endyear,
                                                Width=width,Height=height,
                                                nearby_sites_number=local_nearby_sites_number,
                                                YYYY=YYYY,MM=MM)

    if Get_mahalanobis_distance_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Calculate_Mahalanobis_distance(channel_lists=channel_lists,
                                              species=species,version=version,NA_CNN_version=training_data_version,
                                              NorthAmerica_PM25_special_name=training_data_special_name,
                                              AVD_version=AVD_version,Obs_version=Obs_version,
                                              start_year=startyear,end_year=endyear,
                                              Width=width,Height=height,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY=YYYY,MM=MM)
    if Plot_mahalanobis_distance_map_switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_mahalanobis_distance_map(species=species,version=version,
                                              YYYY=YYYY,MM=MM,
                                              obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number)
    if Get_uncertainty_rRMSE_map_Switch:
       Convert_mahalanobis_distance_map_to_uncertainty(
                                              species=species,version=version,special_name=special_name,
                                              Obs_version=Obs_version,
                                              nearby_sites_number=local_nearby_sites_number,
                                              YYYY_list=desire_year_list,MM_list=plot_months)
    if Plot_rRMSE_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0.8, 1.0, 1.2, 0.6]
                vmax_list = [1.6, 2.0, 2.0, 1.8]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                else:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                plot_rRMSE_uncertainty_map(species=species,version=version,
                                           YYYY=YYYY,MM=MM,
                                           obs_version=Obs_version,
                                           nearby_sites_number=local_nearby_sites_number,
                                           vmin=vmin,vmax=vmax)
    if Get_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                Get_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                            obs_version=Obs_version,
                                            nearby_sites_number=local_nearby_sites_number,
                                            YYYY=YYYY,MM=MM,map_estimation_special_name=map_estimation_special_name,
                                            map_estimation_version=map_estimation_version)
    if Plot_absolute_uncertainty_map_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                vmin_list = [0, 0, 0, 0, 0]
                vmax_list = [1, 1, 1, 1, 1]
                if MM in [0,1,11]:
                    vmin = vmin_list[0]
                    vmax = vmax_list[0]
                elif MM in [2,3,4]:
                    vmin = vmin_list[1]
                    vmax = vmax_list[1]
                elif MM in [5,6,7]:
                    vmin = vmin_list[2]
                    vmax = vmax_list[2]
                elif MM in [8,9,10]:
                    vmin = vmin_list[3]
                    vmax = vmax_list[3]
                else:
                    vmin = vmin_list[4]
                    vmax = vmax_list[4]
                plot_absolute_uncertainty_map(species=species,version=version,special_name=special_name,
                                             YYYY=YYYY,MM=MM,
                                             obs_version=Obs_version,
                                             nearby_sites_number=local_nearby_sites_number,
                                             vmin=vmin,vmax=vmax)
    if Plot_Map_estimation_Switch:
        for YYYY in desire_year_list:
            for MM in plot_months:
                plot_map_estimation_data(species=species,map_estimation_special_name=map_estimation_special_name,map_estimation_version=map_estimation_version,YYYY=YYYY,MM=MM)