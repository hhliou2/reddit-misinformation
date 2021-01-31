import os
import sys
import json
from src.data import data_download
from src.features import calculate_stats
from src.features import user_polarity
from src.models import construct_matrices


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
        
        after_year = data_params['after_year']
        after_day = data_params['after_day']
        after_month = data_params['after_month']

        science = data_params['science']
        myth = data_params['myth']
        politics = data_params['politics']
        
        data_download.write_data(science, science_path, before_year, before_day, before_month, after_year, after_day, after_month)
        data_download.write_data(myth, myth_path, before_year, before_day, before_month, after_year, after_day, after_month)
        data_download.write_data(politics, politics_path, before_year, before_day, before_month, after_year, after_day, after_month)
    
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
        
        
    if 'user_polarity' in targets:
        # Import configs
        with open('config/user_polarity_params.json') as f:
            path_params = json.load(f)
        
        # Load configs

        science_path = path_params['science_path']
        myth_path = path_params['myth_path']
        politics_path = path_params['politics_path']
        output_path = path_params['output_path']
        output_file = path_params['output_file']
        user_polarity.calc_user_polarity(science_path, myth_path, politics_path, output_path, output_file)
    
    if 'matrices' in targets:
        #Import configs
        with open('config/matrix_params.json') as f:
            matrix_params = json.load(f)
        
        # Load configs
        science_path = matrix_params['science_path']
        myth_path = matrix_params['myth_path']
        politics_path = matrix_params['politics_path']
        
        polarity_path = matrix_params['polarity_path']
        
        users_by_sub = construct_matrices.users_by_subreddit(science_path, politics_path, myth_path)
        shared_u = construct_matrices.shared_users(users_by_sub)
        print(construct_matrices.count_matrix(shared_u))
        print(construct_matrices.polarity_matrix(shared_u, polarity_path))
        
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
