import os
import sys
import json
from src.data import data_download
from src.features import user_polarity
from src.models import construct_matrices
from src.visualization import plot_graphs


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
        
        matrix_path = matrix_params['matrix_path']
        count_matrix_name = matrix_params['count_matrix_name']
        polarity_matrix_name = matrix_params['polarity_matrix_name']
        
        science_order = matrix_params['science_order']
        myth_order = matrix_params['myth_order']
        politics_order = matrix_params['politics_order']
        
        users_by_sub = construct_matrices.users_by_subreddit(science_path, politics_path, myth_path)
        shared_u = construct_matrices.shared_users(users_by_sub)
        construct_matrices.count_matrix(shared_u, matrix_path, science_order, myth_order, politics_order, count_matrix_name)
        construct_matrices.polarity_matrix(shared_u, polarity_path, matrix_path, science_order, myth_order, politics_order, polarity_matrix_name)
    
    if 'visualize' in targets:
        #Import configs
        with open('config/visualize_params.json') as f:
            visualize_params = json.load(f)
        
        polarity_path = visualize_params['polarity_path']
        count_matrix_path = visualize_params['count_matrix_path']
        polarity_matrix_path = visualize_params['polarity_matrix_path']
        
        polarity_hist_path = visualize_params['polarity_hist_path']
        count_chart_path = visualize_params['count_chart_path']
        polarity_chart_path = visualize_params['polarity_chart_path']
        
        plot_graphs.polarity_histogram(polarity_path, polarity_hist_path)
        plot_graphs.count_chart(count_matrix_path, count_chart_path)
        plot_graphs.polarity_chart(polarity_matrix_path, polarity_chart_path)
        
    if 'test' in targets: 
        #Import configs
        with open('test/test_params.json') as f:
            path_params = json.load(f)
        # Load configs
        science_path = path_params['science_path']
        myth_path = path_params['myth_path']
        politics_path = path_params['politics_path']
        output_path = path_params['output_path']
        output_file = path_params['output_file']
        polarity_path = path_params['polarity_path']
        matrix_path = path_params['matrix_path']
        count_matrix_name = path_params['count_matrix_name']
        polarity_matrix_name = path_params['polarity_matrix_name']
        polarity_hist_path = path_params['polarity_hist_path']
        count_chart_path = path_params['count_chart_path']
        polarity_chart_path = path_params['polarity_chart_path']
        
        user_polarity.calc_user_polarity(science_path, myth_path, politics_path, output_path, output_file)
    
        users_by_sub = construct_matrices.users_by_subreddit(science_path, politics_path, myth_path)
        shared_u = construct_matrices.shared_users(users_by_sub)
        construct_matrices.count_matrix(shared_u, matrix_path, count_matrix_name)
        construct_matrices.polarity_matrix(shared_u, polarity_path, matrix_path, polarity_matrix_name)
        
        plot_graphs.polarity_histogram(polarity_path, polarity_hist_path)
        plot_graphs.count_chart(matrix_path + '/' + count_matrix_name, count_chart_path)
        plot_graphs.polarity_chart(matrix_path + '/' + polarity_matrix_name, polarity_chart_path)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
