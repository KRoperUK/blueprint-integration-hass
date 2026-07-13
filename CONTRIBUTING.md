# Contributing

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` → minor bump
- `fix:` → patch bump
- `feat!:` / `fix!:` / `BREAKING CHANGE:` → major
- `chore:`, `docs:`, `ci:`, `test:` → no release by default

## Dev pre-releases

Same-repo PRs that touch `custom_components/**` (or tests/CI) mint a **prerelease** after CI is green. See [docs/pre-releases.md](docs/pre-releases.md).

## Local checks

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements_test.txt
ruff check custom_components tests
ruff format --check custom_components tests
mypy
pytest
bash scripts/test-dev-version-scripts.sh
```
