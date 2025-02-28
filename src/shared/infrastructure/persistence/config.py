import configparser
import os
from dotenv import load_dotenv
from src.shared.exceptions.config_exceptions import ConfigSectionNotFound
from src.shared.exceptions.config_exceptions import DatabaseURISchemeNotFound

load_dotenv()

DATABASE_URI_SCHEME = {
    "postgresql": ("postgresql://"
                   "{user}:{password}@"
                   "{host}:{port}/"
                   "{database}")
}

config = configparser.ConfigParser()
config_file_path = os.environ.get("DB_CONFIG_FILE")

if config_file_path:
    config.read(config_file_path)
else:
    raise FileNotFoundError("DB Config file not found")

def get_database_uri(db_config_section: str) -> str:
    if not config.has_section(db_config_section):
        raise ConfigSectionNotFound(f"Section {db_config_section} not found in config file")

    section = dict(config[db_config_section])
    protocol = section.pop("protocol")

    if not protocol in DATABASE_URI_SCHEME:
        raise DatabaseURISchemeNotFound(f"Database URI scheme {protocol} not found")

    uri = DATABASE_URI_SCHEME[protocol].format(**section)
    return uri
