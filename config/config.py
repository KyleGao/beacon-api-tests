"""Configurations for the tests."""

# Path to the OpenAPI spec
SPEC = 'beacon.yaml'

# Lists of hosts to test
HOSTS = {
    'local': 'http://localhost:5050',
    # sv beacon must end with '/'
    'sv': 'https://swefreq-dev.nbis.se/api/beacon-elixir/',
    'es': 'https://ega-archive.org/beacon-api',
    'fi': 'https://beaconpy-elixirbeacon.rahtiapp.fi',
    'fi_local': 'http://localhost:5051',
}

# Directory containing JSON schemas
SCHEMAS = 'schemas'

#  Floats are rounded in comparisions, set the precision (number of digits) here
PRECISION = 6

# Define what keys that should be used to sort lists of dictionaries
SORT_BY = {'datasets': ['id'], 'datasetAlleleResponses': ['datasetId', 'frequency']}
