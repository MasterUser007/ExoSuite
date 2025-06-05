# A. Symbolic Cache for Composite Elimination (Dynamic Symbolic Filtering)

Novelty: HIGH

This approach encodes composite elimination patterns into symbolic representations, allowing storage of generalized traits of composites as symbolic rules rather than specific numbers. It enables dynamic creation of new symbolic patterns during discovery, fusing caching, symbolic abstraction, and pattern mining. It moves from number-by-number elimination toward pattern-based knowledge compression, combining symbolic AI concepts with number theory.

B. Filtering as a Data Compression Problem
Novelty: HIGH

This concept reframes prime search as an information compression problem, viewing filtering as reducing the information needed to represent the valid candidate set. Inspired by data compression, it removes redundancy (invalid candidates), leaving a compressed valid dataset. This aligns with machine learning/information theory rather than classical number theory framing.

C. Built-in Symbolic Cache Hierarchies (Parent-Child Symbol Patterns)
Novelty: HIGH

The symbolic cache supports hierarchical structures: child symbolic rules branch from parent elimination patterns. Hierarchical caching enables meta-pattern reuse and inheritance of elimination traits, introducing a graph- or tree-based abstraction over composite elimination rules, which departs from flat lookup tables.

D. Progressive Modulus Expansion for Dynamic Filtering
Novelty: HIGH (in application)

The design supports incrementally increasing the modulus (e.g., 210 → 2310 → 30030) dynamically to tighten exclusion as compute/memory allows. This enables scaling filter tightness in stages without redesign. Traditional sieves pick modulus at compile/init-time; here, it acts as a scalable design variable.

E. Layered Filtering Pipeline Ordered by Elimination Power
Novelty: HIGH

Filtering operations are prioritized from largest eliminator to smallest, minimizing function calls. Most algorithms use fixed sequences without measuring elimination impact as an ordering heuristic. This intentionally prioritizes elimination order as a quantifiable design factor for efficiency.

F. Modulo Residue Class Filtering as Primary Eliminator
Novelty: MEDIUM-HIGH

Instead of using modulo filtering inside sieves, this approach uses valid residue classes as a front-loaded standalone filter. Residue tables are precomputed for composite moduli like 210, 2310, etc., eliminating ~77%+ upfront before sieving or testing.

G. Combining Symbolic + Modulo + Digit Pattern into Unified Filter Chain
Novelty: MEDIUM-HIGH (as integration)

While components are known separately, combining symbolic cache, modulo residue filter, and last-2-digit elimination into a single pre-sieving exclusion system, ordered by elimination power is rare. This integration pre-reduces candidates before sieve operations.

H. Elimination via Precomputed Invalid Last Two-Digit Endings
Novelty: MEDIUM

Using a precomputed cache of last-2-digit endings known to be composite avoids full modulo calculations at runtime. This digit pattern elimination acts orthogonally to classic sieves by pre-filtering based on digit patterns.

9. Exclusion-First Design Philosophy (Removing Haystacks vs Finding Needle)
Novelty: MEDIUM-HIGH

The tool is designed around removing known false candidates before testing unknowns. The guiding philosophy is 'We remove the haystacks so you don’t have to find the needle, focusing optimization on minimizing search space rather than optimizing primality tests.

10. Structural Elimination of Evens via Iteration
Novelty: LOW-MEDIUM

By stepping increments of 2 starting at “n” (Where “n = the highest recorded prime with no gaps in numbers back to 0”), even numbers are eliminated structurally in iteration logic, not by runtime checking. This ensures no compute cycles wasted checking even numbers.

