# E. Efficiency & Scalability

Symbolic filtering eliminates over 90% of candidate numbers in the early pipeline. By doing so, it drastically reduces the load on the GPU sieve and Miller-Rabin test stages, which are significantly more computationally expensive. This early pruning is especially important when operating on large digit sets, where the number of raw candidates can scale into the billions.

