# File paths
INPUT_FILE_PATH = "datasets/"
OUTPUT_FILE_PATH = "output/"

# Data Loading conditions
COLS_TO_DROP_DURING_LOAD = ['Current Price', 'Market Capitalization']
FILE_TO_EXCLUDE = 'datasets/other_metrics_final.csv'

# Preprocessing parameters
MISSING_THRESHOLD = 0.1
VARIANCE_THRESHOLD = 0.01
CORRELATION_THRESHOLD = 0.1

# Preprocessing strategies
MISSING_VALUE_STRATEGY = 'mean'  # Options: 'mean', 'median', 'most_frequent'

# Target
TARGET = 'Current Price'

# Non Essential Features to drop
COLS_TO_DROP = ['BSE Code', 'NSE Code', 'Name', 'join_key']