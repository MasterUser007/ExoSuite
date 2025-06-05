# B. Multi-GPU Parallelism

The system automatically detects and allocates available GPUs using CUDA-aware libraries and batch partitioning. Multi-GPU support includes:
• Dynamic workload allocation across GPU devices
• Batched sieving and parallel candidate filtering
• Load-balancing based on memory usage and queue occupancy

This allows the system to scale linearly with available hardware, ideal for cryptographic discovery or academic simulation projects.

