# ml_plugins/loader.py

import importlib.util
import pathlib
import json
from ml_plugins.base import BaseMLPlugin
from ml_plugins.plugin_registry import PluginRegistry


def load_plugins(plugin_folder="ml_plugins", config_file=".ml_config.json"):
    registry = PluginRegistry()
    config = {}

    # Load runtime config
    config_path = pathlib.Path(config_file)
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)

    plugin_path = pathlib.Path(plugin_folder)
    for plugin_file in plugin_path.glob("*.py"):
        if plugin_file.name in (
            "__init__.py",
            "base.py",
            "loader.py",
            "plugin_registry.py",
        ):
            continue
        spec = importlib.util.spec_from_file_location(plugin_file.stem, plugin_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        for attr in dir(module):
            obj = getattr(module, attr)
            if (
                isinstance(obj, type)
                and issubclass(obj, BaseMLPlugin)
                and obj is not BaseMLPlugin
            ):
                instance = obj()
                registry.register(instance)

    return registry.get_enabled_plugins(config)

