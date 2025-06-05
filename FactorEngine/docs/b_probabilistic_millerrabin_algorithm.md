# B. Probabilistic Miller–Rabin Algorithm

The Miller–Rabin test is a probabilistic primality test that verifies whether a number is 'probably prime'. It works by performing randomized base checks that would detect compositeness if the candidate fails any round. Each successful round exponentially reduces the chance of a false positive. For example, 40 rounds yields a false positive rate below 2⁻⁸⁰. PrimeEngineAI supports user-defined configurations to set the number of test rounds for each candidate class.

