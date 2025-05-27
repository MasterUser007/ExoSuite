# ExoSuite Blueprint

## Executive Summary
**Purpose:**  
ExoSuite is an orchestrating layer that brings together four core engines—PrimeEngineAI, FactorEngine, QuantumHash, CacheManager—into a cohesive, high‑performance prime‑discovery and cryptographic toolset.

**Value Proposition:**  
- Unified API surface for prime discovery, factorization, hashing, and symbolic caching  
- Pareto‑optimal compute efficiency via tiered filtering and GPU acceleration  
- Continuous learning across engines through shared symbol cache  

## Objectives & Goals
1. **Interoperability:** Seamless data handoff between engines with minimal serialization overhead.  
2. **Scalability:** Support local, multi‑CPU, and multi‑GPU deployments (on‑prem or cloud).  
3. **Reliability:** 99.9% uptime via CI/CD–driven testing and automated deployments.  
4. **Extensibility:** Plugin model for adding new engines (e.g., entropy sampler) without core changes.  

## Scope
- **In‑Scope:**  
  - Integration of existing engines  
  - Unified REST/gRPC endpoints  
  - Centralized symbol cache management  
  - CI pipelines (lint, tests, docs) and GitHub Pages  
- **Out‑of‑Scope (v1):**  
  - Web‑based GUI frontend  
  - Third‑party cloud orchestration scripts (Kubernetes, Terraform)  

## High‑Level Architecture

![ExoSuite Architecture](exosuite_architecture.png)

### Components
- **API Gateway:** Routes requests to individual engines or workflows.  
- **PrimeEngineAI Module:** High‑speed prime finder with symbolic prefiltering.  
- **FactorEngine Module:** Deterministic factorization pipeline.  
- **QuantumHash Module:** GPU‑accelerated cryptographic hash generation.  
- **CacheManager:** Tiered L0/L1/L2 symbol cache with persistence.  

### Integration Patterns
- **Synchronous Calls:** Single‑engine operations via direct endpoint (e.g., /prime, /factor).  
- **Orchestrated Workflows:** Chained multi‑engine routines (e.g., find prime → compute hash → cache symbol).  
- **Event‑Driven Hooks:** Plugins can subscribe to cache miss/hit events for custom analytics.  

## Module & Pipeline Specifications

### PrimeEngineAI
- **Responsibilities:** Discover primes in range.  
- **Interfaces:**  
  - POST /prime → { start: int, end: int } → [primes]  
  - Hook events: onPrimeFound, onPrefilterApplied.

### FactorEngine
- **Responsibilities:** Factor integers into primes.  
- **Interfaces:**  
  - POST /factor → { n: int } → { factors: [int] }  
  - Exposes streaming results for large inputs.

*(Repeat similarly for QuantumHash & CacheManager)*

## Data Flow & Persistence
1. Request received at API Gateway  
2. Route to appropriate engine  
3. Engine queries CacheManager for symbols  
4. Compute or retrieve result  
5. Write back to cache and return response  

All cache state is persisted to disk under ~/.exosuite/cache/ with TTL and LRU eviction.

## CI/CD & Documentation
- **Lint/Test:** GitHub Actions (.github/workflows/ci.yml) across Python 3.8–3.11.  
- **Docs:** MkDocs site built to docs/site/ and deployed via pages.yml.  
- **Pre‑commit:** Black, MyPy, trailing‑whitespace fixer.

## Roadmap & Milestones
| Phase         | Deliverables                           | ETA        |
| ------------- | -------------------------------------- | ---------- |
| Initialization| Polyrepo setup + CI + Docs for v0.1    | Jun 5, 2025 |
| Integration   | ExoSuite monorepo + submodules         | Jun 20, 2025|
| Performance   | GPU batching + RL‑driven caching       | Jul 15, 2025|
| Beta Release  | Private beta with internal users       | Aug 1, 2025 |

## Glossary
- **Symbol:** A canonical representation of a prime or factor used for caching.  
- **Prefilter:** A lightweight test to eliminate non‑primes before heavy computation.  

---
