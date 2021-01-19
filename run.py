import os
import sys
import json
from src.data import data_download
from src.features import calculate_stats


# main operation
def main(targets):
    if 'data' in targets:
        # Import configs
        with open('config/data_params.json') as f:
            data_params = json.load(f)
        
        # Load configs
        api_keys = data_params['api_keys']

        science_path = data_params['science_path']
        myth_path = data_params['myth_path']
        politics_path = data_params['politics_path']
        
        before_year = data_params['before_year']
        before_day = data_params['before_day']
        before_month = data_params['before_month']

        science = data_params['science']
        myth = data_params['myth']
        politics = data_params['politics']
        
        data_download.write_dehydrated_data(science, science_path, before_year, before_day, before_month)
        data_download.write_dehydrated_data(myth, myth_path, before_year, before_day, before_month)
        data_download.write_dehydrated_data(politics, politics_path, before_year, before_day, before_month)
    
    if 'stats' in targets:
        with open('config/stat_params.json') as f:
            stat_params = json.load(f)
        
        # Load configs
        science_path = stat_params['science_path']
        myth_path = stat_params['myth_path']
        politics_path = stat_params['politics_path']
        
        sample_size = stat_params['sample_size']
        
        calculate_stats.sample(sample_size, science_path)
        calculate_stats.sample(sample_size, myth_path)
        calculate_stats.sample(sample_size, politics_path)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
