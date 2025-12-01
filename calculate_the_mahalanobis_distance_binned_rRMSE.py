import numpy as np
import os
from data_func.Assemble_func import Assemble_Mahalanobis_distance_data,derive_local_reference_for_channels
from data_func.utils import Get_typeName
import argparse


parser=argparse.ArgumentParser()

parser.add_argument('--SPECIES_list',  nargs='+',type = str)
SPECIES_list = parser.parse_args().SPECIES_list

Derive_local_reference_Switch = True # Once get the local reference for all the variables. No need to derive again.
Derive_Mahalanobis_distance_Switch = True

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
                    'AOD', 'GeoPM25','ETA',# 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias',
                    'GC_NH4', #'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT',
                    #'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi',
                   # 'DST_offline_emi',
                    'RH', #'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                    #'Urban_Builtup_Lands',
                    'minor_roads',
                    #'Month_of_Year',
                    'Lat', 'Lon',# 'elevation',
                   # 'Population'
                    ]
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    local_nearby_sites_number = 30
    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [#'AOD','ETA', 'GeoPM25','EtaAOD_Bias', 'EtaMixing', 'EtaSGAOD_Bias', 
                    'GeoNIT','GeoBC','GeoNH4','GeoSO4',#'GeoOM','GeoDUST','GeoSS',
                    #'NA_CNN_PM25',
                    'GC_NIT',  'GC_SO4', 'GC_SOA',# 'GC_PM25', 'GC_BC', 'GC_NH4', 'GC_DST','GC_SSLT','GC_OM',
                    'NH3_anthro_emi',#'NO_anthro_emi', 'OC_anthro_emi', 'SO2_anthro_emi',
                   # 'DST_offline_emi','SSLT_offline_emi',
                   # 'RH', 'T2M', 'U10M', 'V10M','PBLH', 'PRECTOT',
                   # 'Urban_Builtup_Lands','Croplands',
                    #'Month_of_Year',
                    'Lat', 'Lon',#'elevation',
                    #'Population'
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [#'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoSO4',#'GeoNH4','GeoNIT','GeoBC','GeoOM','GeoDUST','GeoSS',
                    'NA_CNN_PM25',
                    'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_DST',#'GC_PM25', 'GC_BC','GC_OM','GC_SSLT',#'GC_NIT', #'GC_OC',
                    #'NH3_anthro_emi','NO_anthro_emi','SO2_anthro_emi',
                     #'SSLT_offline_emi',
                    'T2M', #'RH', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    #'Urban_Builtup_Lands',
                    #'Month_of_Year',
                    'Lat', 'Lon',#'elevation',
                   
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [ #'AOD','EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias','GeoPM25','ETA',
                    'GeoNH4','GeoSO4',#'GeoBC','GeoOM','GeoDUST','GeoNIT',
                    'NA_CNN_PM25',
                     'GC_SO4', 'GC_SOA',  'GC_BC',#'GC_PM25', 'GC_NH4', 'GC_DST','GC_SSLT','GC_OM',
                     #'SSLT_offline_emi',
                    'T2M',# 'U10M', 'V10M','PBLH', 'PRECTOT',
                    #'Urban_Builtup_Lands','Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands',
                    'Month_of_Year',
                    'Lat', 'Lon',#'elevation',
                    #'Population'
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [#'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoBC','GeoSO4',#'GeoNH4','GeoNIT','GeoOM','GeoSS',
                    'NA_CNN_PM25',
                    'GC_SOA', 'GC_SO4',  'GC_BC',# 'GC_PM25', 'GC_NH4',  'GC_DST','GC_SSLT','GC_NIT',# #'GC_OC','GC_OM','
                    'BC_anthro_emi','OC_anthro_emi',
                    #'T2M', 'U10M', 'V10M','PBLH', 'RH', 'PRECTOT',
                    'Urban_Builtup_Lands',
                    #'log_motorway','log_primary',
                    #'major_roads',
                    #'Month_of_Year',
                    'Lat', 'Lon',#'elevation'
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    
    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [ #'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA',
                    'GeoOM','GeoSO4',#'GeoNIT','GeoSS',
                    'NA_CNN_PM25',
                    'GC_SOA', #'GC_OM', 'GC_PM25',  'GC_BC', 'GC_NIT', 
                    'SO2_anthro_emi','NO_anthro_emi', 'OC_anthro_emi',#'NH3_anthro_emi','NMVOC_anthro_emi', 
                    #'DST_offline_emi',
                    #'RH', 'T2M', 'U10M', 'V10M','PBLH', 'PRECTOT',
                    'Urban_Builtup_Lands',
                    #'Month_of_Year',
                    'Lat', 'Lon',#'elevation',
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)


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
    channel_lists = [#'AOD',  'EtaSGAOD_Bias',
                'GeoBC','GeoDUST',#'GeoNH4','GeoNIT','GeoSO4','GeoSS',
                'NA_CNN_PM25',
                'GC_SOA','GC_DST',# 'GC_NH4', 'GC_NIT','GC_SO4','GC_PM25',    'GC_BC', 'GC_SSLT','GC_OM',# #'GC_OC',
                'OC_anthro_emi', #'SO2_anthro_emi',
                #'SSLT_offline_emi',
                'RH', #'T2M', 'PBLH','USTAR', 'PRECTOT',
               # 'Urban_Builtup_Lands',
               # 'unclassified',
                'Month_of_Year',
                'Lat', 'Lon',#'elevation',
                #'Population'
                ] 

    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)

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
    channel_lists = [ #'AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                    'GeoSS','GeoSO4',#'GeoBC','GeoNH4','GeoNIT','GeoOM','GeoDUST',
                    #'NA_CNN_PM25',
                    'GC_SO4',#'GC_PM25', 'GC_NH4',   'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM','GC_NIT', #'GC_OC',
                    'SO2_anthro_emi','OC_anthro_emi', 'BC_anthro_emi',#'NH3_anthro_emi','NO_anthro_emi', 'NMVOC_anthro_emi',####'N2O_anthro_emi',,# 
                    #'DST_offline_emi',
                    'T2M','PBLH', #'RH', 'U10M', 'V10M','PRECTOT',
                    #'Month_of_Year',
                    'Lat', 'Lon',#'elevation',
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']

    if Derive_local_reference_Switch:
        derive_local_reference_for_channels(channel_lists, species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        buffer_radius_list, BLCO_kfold, desire_year_list, 'mean',
                                        local_nearby_sites_number)
    if Derive_Mahalanobis_distance_Switch:  
        Assemble_Mahalanobis_distance_data(species, version, typeName, startyear, endyear,
                                        nchannel, special_name, width, height,
                                        training_data_version, training_data_special_name,
                                        buffer_radius_list, BLCO_kfold,
                                        channel_lists, desire_year_list,
                                        local_nearby_sites_number)