# superset_config.py
from flask_appbuilder.security.manager import AUTH_DB

# Database configurations
SQLALCHEMY_DATABASE_URI = 'postgresql://cagri:35413541@postgres:5432/druid'

# Druid configurations
DRUID_IS_ACTIVE = True
DRUID_HOST = 'broker:8082'
DRUID_ENDPOINT = '/druid/v2/sql'
DRUID_USER = ''
DRUID_PASSWORD = ''

# Add Druid to the databases
ADDITIONAL_DATABASES = {
    'druid': {
        'allow_csv_upload': False,
        'allow_ctas': False,
        'allow_cvas': False,
        'database_name': 'druid',
        'extra': {
            'engine_params': {
                'connect_args': {
                    'host': 'broker',
                    'port': 8082,
                    'path': '/druid/v2/sql',
                    'scheme': 'http'
                }
            }
        },
        'sqlalchemy_uri': 'druid://broker:8082/druid/v2/sql'
    }
}

# Security configurations
AUTH_TYPE = AUTH_DB
SECRET_KEY = '35413541'

# Feature flags
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
}