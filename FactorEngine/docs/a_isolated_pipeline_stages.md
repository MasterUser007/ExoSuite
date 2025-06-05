# A. Isolated Pipeline Stages

Each pipeline stage—truncation testing, symbolic filtering, GPU sieving, remainder analysis, and primality testing—is implemented as an independent module. This modular encapsulation allows each component to be upgraded, replaced, or re-optimized without requiring changes to the surrounding infrastructure. It also allows rapid prototyping of new filtering techniques and side-by-side validation against production logic.

