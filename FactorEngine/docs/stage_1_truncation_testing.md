# Stage 1: Truncation Testing

In this initial filtering stage, PrimeEngineAI applies digit-based symbolic exclusion rules to rapidly remove non-prime candidates. These rules are based on known properties of composites—such as numbers ending in '0', '2', '4', '5', '6', or '8', which are immediately excluded. Additionally, patterns like repeating digits (e.g., '111', '000', '222') or mirrored ends may signal divisibility or non-prime structures. This symbolic truncation step eliminates a significant portion of low-quality candidates before deeper analysis.

