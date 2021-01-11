import os
import sys
import json
from src.data import data_download


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

        science = data_params['science']
        myth = data_params['myth']
        politics = data_params['politics']
        
        data_download.write_data(science, science_path, api_keys)
        data_download.write_data(myth, myth_path, api_keys)
        data_download.write_data(politics, politics_path, api_keys)
        
if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
