# Appendix: Formula Reference

## 1. Symbolic Filters

**Last Digit Filter**  
Exclude all integers ending in 0, 4, 6, 8 unless verified exceptions:
```
if str(n)[-1] in ['0', '4', '6', '8']: exclude
```

**Modulus Rule**  
Exclude multiples of 2 or 5:
```
if n % 2 == 0 or n % 5 == 0: exclude
```

## 2. Miller-Rabin Probabilistic Test

Used to validate if a number is likely prime:
```
Repeat k times:
  Choose random a
  Check pow(a, d, n) for specific residue conditions
```

Output: True = probably prime; False = definitely composite

## 3. Pipeline Flow

```
input → symbolic filter → GPU primality test → ML plugin (optional)
```

Each layer excludes or confirms candidate status.