# ml_plugins/plugin_registry.py

class PluginRegistry:
    def __init__(self):
        self.plugins = []

    def register(self, plugin_instance):
        self.plugins.append({
            "name": plugin_instance.name,
            "version": getattr(plugin_instance, "version", "1.0"),
            "author": getattr(plugin_instance, "author", "unknown"),
            "description": getattr(plugin_instance, "description", ""),
            "instance": plugin_instance
        })

    def get_enabled_plugins(self, config):
        return [
            p["instance"]
            for p in self.plugins
            if config.get(p["name"], True)  # default to enabled
        ]