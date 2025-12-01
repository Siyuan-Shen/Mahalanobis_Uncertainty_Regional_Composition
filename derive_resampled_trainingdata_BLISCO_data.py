import numpy as np
import os
from data_func.Assemble_func import derive_corresponding_training_data_BLISCO_data
from data_func.utils import Get_typeName

SPECIES_list = ['PM25','NO3','SO4','NH4','BC','OM','DUST','SS']

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
    channel_lists = ['AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing',   'GeoPM25','EtaSGAOD_Bias','EtaSGTOPO_Bias','ETA',
                                                        'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT',
                                                        'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'BC_anthro_emi',
                                                        'DST_offline_emi',
                                                        'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                                                        'Urban_Builtup_Lands',
                                                        'minor_roads',
                                                        'Month_of_Year',
                                                            'Lat', 'Lon','elevation',
                                                            'Population']
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)

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
    channel_lists =  ['AOD', 'EtaAOD_Bias', 'EtaMixing', 'EtaSGAOD_Bias',  'GeoPM25','ETA',#'EtaSGTOPO_Bias','EtaCoastal',
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoOM','GeoDUST','GeoSS',
                                                       'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                       'GC_PM25','GC_NIT',  'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM',##'GC_OC',
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                       'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi', 'SO2_anthro_emi','NMVOC_anthro_emi',#'BC_anthro_emi','N2O_anthro_emi',,# 
                                                       'DST_offline_emi','SSLT_offline_emi',
                                                       'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                                                       'Urban_Builtup_Lands','Croplands',#'Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       #'primary',# 'secondary',#'unclassified',#'trunk',#'motorway', #
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    
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
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoOM','GeoDUST','GeoSS',
                                                       'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                       'GC_PM25', 'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_OM','GC_SSLT',#'GC_NIT', #'GC_OC',
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                       'NH3_anthro_emi','NO_anthro_emi','SO2_anthro_emi',# 'OC_anthro_emi', 'BC_anthro_emi',#,##'NMVOC_anthro_emi',#'N2O_anthro_emi',,# 
                                                       'SSLT_offline_emi',#'DST_offline_emi',#
                                                       'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                                                       'Urban_Builtup_Lands',#'Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       #'primary',# 'secondary',#'unclassified',#'trunk',#'motorway', #
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    

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
    channel_lists = ['AOD','EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias', 'EtaSGTOPO_Bias','GeoPM25','ETA',# 
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoOM','GeoDUST',#'GeoSS',
                                                       'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                       'GC_PM25', 'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM',# #'GC_OC','GC_NIT',
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                       'NH3_anthro_emi','SO2_anthro_emi',# 'NO_anthro_emi','OC_anthro_emi', 'BC_anthro_emi',##'NMVOC_anthro_emi',#'N2O_anthro_emi',,# 
                                                      'SSLT_offline_emi',# 'DST_offline_emi',
                                                        'T2M', 'U10M', 'V10M','PRECTOT','PBLH', #'RH',
                                                       'Urban_Builtup_Lands','Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       #'primary',# 'secondary',#'unclassified',#'trunk',#'motorway', #
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    


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
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoOM','GeoSS',#'GeoDUST',
                                                      'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                      'GC_PM25', 'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_NIT',# #'GC_OC','GC_OM','
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                        'OC_anthro_emi', 'BC_anthro_emi',#'NMVOC_anthro_emi','NH3_anthro_emi','NO_anthro_emi','SO2_anthro_emi',###'N2O_anthro_emi',,# 
                                                       #'SSLT_offline_emi',#'DST_offline_emi',#
                                                       'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 'RH', 
                                                       'Urban_Builtup_Lands',#'Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       'log_motorway','log_primary',
                                                       'major_roads',#'minor_roads',#'primary',# 'secondary',#'unclassified',#'trunk',#'motorway', #
                                                        #"trunk_dist", #"primary_dist", "secondary_dist","motorway_dist",
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        #'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    

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
    channel_lists = ['AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA',#'GeoPM25',#'EtaSGTOPO_Bias',
                    'GeoNIT','GeoSO4','GeoOM','GeoSS',#'GeoDUST','GeoBC','GeoNH4',
                    'NA_CNN_PM25',#'GL_CNN_PM25',#
                    'GC_PM25',  'GC_SOA',  'GC_BC', 'GC_OM','GC_NIT', #'GC_OC','GC_NH4', 'GC_SO4', 'GC_DST','GC_SSLT',
                    # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                    'NH3_anthro_emi','NO_anthro_emi', 'OC_anthro_emi','NMVOC_anthro_emi', 'SO2_anthro_emi',#'BC_anthro_emi',###'N2O_anthro_emi',,# 
                    'DST_offline_emi',#'SSLT_offline_emi',
                    'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                    'Urban_Builtup_Lands',#'Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                    #'motorway', # #'primary',# 'secondary',#'unclassified',#'trunk',#
                    'Month_of_Year',
                    'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                    #'Population'
                    ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    


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
    channel_lists =['AOD',  'EtaSGAOD_Bias',#'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoDUST','GeoSS',#'GeoOM',
                                                       'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                       'GC_PM25', 'GC_NH4', 'GC_NIT','GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM',# #'GC_OC',
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                       'SO2_anthro_emi', 'OC_anthro_emi', #'BC_anthro_emi','NH3_anthro_emi','NO_anthro_emi','NMVOC_anthro_emi',#'N2O_anthro_emi',,# 
                                                       'SSLT_offline_emi',#'DST_offline_emi',#
                                                       'RH', 'T2M', 'PRECTOT','PBLH','USTAR', #'U10M', 'V10M',
                                                       'Urban_Builtup_Lands',#'Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       'unclassified',#'primary','trunk',# 'secondary',###'motorway', #
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)
    


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
    channel_lists = ['AOD', 'EtaAOD_Bias', 'EtaCoastal', 'EtaMixing', 'EtaSGAOD_Bias',  'ETA','EtaSGTOPO_Bias','GeoPM25',
                                                       'GeoNH4','GeoNIT','GeoSO4','GeoBC','GeoOM','GeoDUST','GeoSS',
                                                       'NA_CNN_PM25',#'GL_CNN_PM25',#
                                                       'GC_PM25', 'GC_NH4', 'GC_SO4',  'GC_SOA',  'GC_BC', 'GC_DST','GC_SSLT','GC_OM','GC_NIT', #'GC_OC',
                                                       # 'GCHP_PM25', 'GCHP_NH4', 'GCHP_SO4', 'GCHP_SOA', 'GCHP_OC',  'GCHP_BC', 'GCHP_DST', 'GCHP_SSLT',#'GCHP_NIT', 'GCHP_OM',
                                                       'NH3_anthro_emi','NO_anthro_emi', 'SO2_anthro_emi','OC_anthro_emi', 'BC_anthro_emi','NMVOC_anthro_emi',####'N2O_anthro_emi',,# 
                                                       'DST_offline_emi',#'SSLT_offline_emi',
                                                       'RH', 'T2M', 'U10M', 'V10M','PRECTOT','PBLH', 
                                                       #'Urban_Builtup_Lands',#'Croplands','Crop_Nat_Vege_Mos','Permanent_Wetlands', 
                                                       #'primary',# 'secondary',#'unclassified',#'trunk',#'motorway', #
                                                       'Month_of_Year',
                                                        'Lat', 'Lon','elevation',#'S1','S2','S3',#'S1','S2','S3','  'Lon',
                                                        #'Population'
                                                       ] 
    desire_year_list = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009',
                        '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
                        '2020', '2021', '2022', '2023']
    derive_corresponding_training_data_BLISCO_data(typeName=typeName, species=species, version=version,
                                                    startyear=startyear, endyear=endyear, nchannel=nchannel,
                                                    special_name=special_name, width=width, height=height,
                                                    training_data_version=training_data_version,
                                                    training_data_special_name=training_data_special_name,
                                                    buffer_radius_list=buffer_radius_list, BLCO_kfold=BLCO_kfold,
                                                    BLCO_seeds_number=BLCO_seeds_number, channel_lists=channel_lists,
                                                    desire_year_list=desire_year_list)