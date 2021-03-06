# NAME
#        duree_(repas)_mean_parser.py
#
# DESCRIPTION
#
#       'duree_(repas)_mean_parser.py' is a script that returns one csv
#       containing the mean meal length in all regions
#       We first retrieve all individuals in a given region and then,
#       we extract from REPAS table the matching data
#
# HISTORY
#
# 2 january 2018 - Initial design and coding. (Valentina Zelaya, @vz-chameleon, TGarwood @TGarwood)

import pandas as pd
import numpy as np
import os.path


data_url_repas = os.path.join('..','raw','INCA2','Table_repas.csv')
df_repas=pd.read_csv(data_url_repas, sep = ';')

region_codes_url = os.path.join('..','csv','indiv_by_region','region_codes.csv')
df_regions=pd.read_csv(region_codes_url, sep= ';')

mean_duree_by_region = [None]*21
entries_number_region= [None]*21
indiv_number_for_region = [None]*21


for reg_code in range(1,22):
    data_url_indiv_region=os.path.join('..', 'csv','indiv_by_region', 'indiv_per_region_'+str(reg_code)+'.csv')
    df_indiv_reg=pd.read_csv(data_url_indiv_region, sep = ';')

    # Get all the individuals in the loaded region
    indiv_values_list = df_indiv_reg["nomen"].values
    indiv_list = np.unique(indiv_values_list)
    indiv_number_for_region[reg_code - 1] = len(indiv_list)

    c=df_repas.loc[(df_repas['nomen'].isin(indiv_list))]
    entries_number_region[reg_code - 1] = len(c['nomen'].values) # to chech

    mean_duree_by_region[reg_code - 1] = c.duree.mean()

df_regions['entries_num'] = entries_number_region
df_regions['indiv_num'] = indiv_number_for_region
df_regions['mean'] = mean_duree_by_region

file_path = os.path.join('..','csv','duree_repas_mean')
file_name = 'simple_duree_repas_mean'+'.csv'
if not os.path.exists(file_path):
    os.makedirs(file_path)
df_regions.to_csv(os.path.join(file_path,file_name), sep=';')

for sexe_ps in range(1, 3):
    for revenu_foyer in range(1, 16):
        for reg_code in range(1,22):
            data_url_menage_region = os.path.join('..', 'csv', 'menage_by_region',
                                                  'menage_by_region' + str(reg_code) + '.csv')
            df_menage_reg = pd.read_csv(data_url_menage_region, sep=';')
            df_menage_reg_filtered = df_menage_reg.loc[
                (df_menage_reg['revenu'] == revenu_foyer)]

            indiv_values_list = df_menage_reg_filtered["nomen"].values
            indiv_list = np.unique(indiv_values_list)

            data_url_indiv_region = os.path.join('..', 'csv', 'indiv_by_region',
                                                 'indiv_per_region_' + str(reg_code) + '.csv')
            df_indiv_reg = pd.read_csv(data_url_indiv_region, sep=';')
            df_indiv_reg_filtered = df_indiv_reg.loc[
                (df_indiv_reg['sexe_ps'] == sexe_ps) & (df_indiv_reg['nomen'].isin(indiv_list))]

            # Get all the individuals in the loaded region
            indiv_values_list = df_indiv_reg_filtered["nomen"].values
            indiv_list = np.unique(indiv_values_list)
            indiv_number_for_region[reg_code - 1] = len(indiv_list)

            c=df_repas.loc[(df_repas['nomen'].isin(indiv_list))]
            entries_number_region[reg_code - 1] = len(c['nomen'].values) # to chech

            mean_duree_by_region[reg_code - 1] = c.duree.mean()

        df_regions['entries_num'] = entries_number_region
        df_regions['indiv_num'] = indiv_number_for_region
        df_regions['mean'] = mean_duree_by_region

        file_path = os.path.join('..','csv','duree_repas_mean')
        file_name = 'simple_duree_repas_mean'+ '_of_sexe_' + str(
                sexe_ps) + '_of_revenu_foyer_' + str(revenu_foyer) +'.csv'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        df_regions.to_csv(os.path.join(file_path,file_name), sep=';')

for revenu_foyer in range(1, 16):
    for reg_code in range(1,22):
        data_url_menage_region = os.path.join('..', 'csv', 'menage_by_region',
                                              'menage_by_region' + str(reg_code) + '.csv')
        df_menage_reg = pd.read_csv(data_url_menage_region, sep=';')
        df_menage_reg_filtered = df_menage_reg.loc[
            (df_menage_reg['revenu'] == revenu_foyer)]

        indiv_values_list = df_menage_reg_filtered["nomen"].values
        indiv_list = np.unique(indiv_values_list)
        indiv_number_for_region[reg_code - 1] = len(indiv_list)

        c=df_repas.loc[(df_repas['nomen'].isin(indiv_list))]
        entries_number_region[reg_code - 1] = len(c['nomen'].values) # to chech

        mean_duree_by_region[reg_code - 1] = c.duree.mean()

    df_regions['entries_num'] = entries_number_region
    df_regions['indiv_num'] = indiv_number_for_region
    df_regions['mean'] = mean_duree_by_region

    file_path = os.path.join('..','csv','duree_repas_mean')
    file_name = 'simple_duree_repas_mean'+ '_of_revenu_foyer_' + str(revenu_foyer) +'.csv'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    df_regions.to_csv(os.path.join(file_path,file_name), sep=';')

for sexe_ps in range(1, 3):
    for reg_code in range(1,22):

        data_url_indiv_region = os.path.join('..', 'csv', 'indiv_by_region',
                                             'indiv_per_region_' + str(reg_code) + '.csv')
        df_indiv_reg = pd.read_csv(data_url_indiv_region, sep=';')
        df_indiv_reg_filtered = df_indiv_reg.loc[
            (df_indiv_reg['sexe_ps'] == sexe_ps)]

        # Get all the individuals in the loaded region
        indiv_values_list = df_indiv_reg_filtered["nomen"].values
        indiv_list = np.unique(indiv_values_list)
        indiv_number_for_region[reg_code - 1] = len(indiv_list)

        c=df_repas.loc[(df_repas['nomen'].isin(indiv_list))]
        entries_number_region[reg_code - 1] = len(c['nomen'].values) # to chech

        mean_duree_by_region[reg_code - 1] = c.duree.mean()

    df_regions['entries_num'] = entries_number_region
    df_regions['indiv_num'] = indiv_number_for_region
    df_regions['mean'] = mean_duree_by_region

    file_path = os.path.join('..','csv','duree_repas_mean')
    file_name = 'simple_duree_repas_mean'+ '_of_sexe_' + str(
            sexe_ps) +'.csv'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    df_regions.to_csv(os.path.join(file_path,file_name), sep=';')
