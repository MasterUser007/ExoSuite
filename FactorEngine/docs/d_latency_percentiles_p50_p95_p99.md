# D. Latency Percentiles (p50, p95, p99)

Latency is recorded at each pipeline stage using percentile statistics:
• p50: Median time per candidate.
• p95: Upper-tail latency representing 95th percentile.
• p99: Edge-case latency (1% slowest).
These metrics help isolate inconsistent behavior, spike events, or I/O bottlenecks during intensive candidate testing.

