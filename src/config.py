import os
from dotenv import load_dotenv
from paths import PARENT_DIR


HOPWORKS_PROJECT_NAME = 'taxi_demand_raj'

load_dotenv(PARENT_DIR/'.env')
try:
    HOPWORKS_API_KEY =  os.environ['HOPWORKS_API_KEY']
except:
    raise Exception('Create an .env file on the project root with the HOPSWORKS_API_KEY')

FEATURE_GROUP_NAME =  'time_series_hourly_feature_group'
FEATURE_GROUP_VERSION = 1
