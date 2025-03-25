from copy import deepcopy
import os
import yaml


class ConfigImporter:
    def get_config(self):
        """
        Create a config dictionary based on the config file.

        :return: dict, configuration
        """
        # Load config files
        config = self.load_config_file("../config/config.yaml")

        return config

    def load_config_file(self, filename):
        """
        Load a config file.

        :param filename: str, name of the YAML config file
        :return: dict, containing config settings
        """
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, filename)

        with open(config_path, "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)

        return config
