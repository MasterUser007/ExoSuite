# ml_plugins/plugin_metrics.py

from prometheus_client import Counter, Histogram, start_http_server

plugin_usage_counter = Counter(
    "plugin_usage_total", "Total number of plugin invocations", ["plugin_name"]
)
plugin_score_histogram = Histogram(
    "plugin_score_distribution", "Score distribution per plugin", ["plugin_name"]
)


def start_metrics_server(port=9000):
    start_http_server(port)


def log_metrics(plugin_name, score):
    plugin_usage_counter.labels(plugin_name=plugin_name).inc()
    plugin_score_histogram.labels(plugin_name=plugin_name).observe(score)
