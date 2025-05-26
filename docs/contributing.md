# to ExoSuite

We welcome contributions to ExoSuite! Please follow the guidelines below to help maintain consistency and code quality.

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a new branch (`feature/my-feature`)
4. Commit your changes with clear messages
5. Push to your fork and submit a pull request

## Contribution Checklist

- Follow the structure and naming conventions of the ExoProject template
- Add tests for any new logic in `tests/`
- Validate your code with:
  ```bash
  pytest
  pre-commit run --all-files
  ```

## Test Strategy

- Unit tests should cover critical paths
- Black-box tests go in `tests/test_exosuite.py`
- Use `examples/` for CLI and API demonstrations

## Security & Code Quality

- Use `pre-commit` to scan for secrets and enforce formatting
- Adhere to PEP8 via `flake8` or `black`

## Documentation

- Update `README.md` or `DEVELOPER_GUIDE.md` for new components
- Include diagrams or examples as needed in `docs/`

---

We maintain strict parity across all ExoSuite engines: changes to one must propagate to all.