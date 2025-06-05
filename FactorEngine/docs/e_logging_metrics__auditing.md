# E. Logging, Metrics & Auditing

All Miller–Rabin and ECPP test results are logged in a centralized test ledger. The system tracks execution time per candidate, round outcomes, total passes/fails, and cumulative false positive rates. This telemetry supports future ML training, audit reproducibility, and performance tuning. Optional JSON or Prometheus exports enable external dashboards and compliance monitoring.

