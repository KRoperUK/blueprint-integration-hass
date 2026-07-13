# blueprint-integration-hass

Template for a **Home Assistant custom integration** published via **HACS**, with the same CI and release discipline used on:

- [dimplex-controller-hass](https://github.com/KRoperUK/dimplex-controller-hass)
- [sungrow-hass](https://github.com/KRoperUK/sungrow-hass)

## What this blueprint includes

| Area | Pattern |
| --- | --- |
| **Layout** | `custom_components/<domain>/` + `tests/` + `docs/` |
| **HACS** | `hacs.json` with `zip_release` + `filename` |
| **Manifest** | Key order `domain`, `name`, then alphabetical; quality-scale ready |
| **CI** | Path-filtered lint / mypy / pytest / HACS / hassfest |
| **Pre-releases** | Semver tags `vX.Y.Z-pr.P.R` (PRs) and `vX.Y.Z-rc.N` (main) on **synthetic version commits** so HACS sorts above last stable |
| **Assets** | `scripts/package-hacs-zip.sh` → `{{DOMAIN}}.zip` on each pre-release |
| **Stable releases** | release-please + conventional commits |
| **Hygiene** | cleanup of PR pre-releases on close; weekly stale-dev sweep |
| **Quality** | ruff, mypy strict on the integration package, pytest-homeassistant-custom-component, coverage floor |
| **Docs** | installation, pre-releases, architecture checklist |

## Create a new integration from this blueprint

1. **Use as GitHub template** (or clone and re-init git).
2. Global rename placeholders (case-sensitive):

   | Placeholder | Example |
   | --- | --- |
   | `example` | domain folder / package name |
   | `Example` | human title |
   | `EXAMPLE` | env / constant prefix |
   | `KRoperUK/blueprint-integration-hass` | your `owner/repo` |
   | `example.zip` | HACS asset name |

   ```bash
   # rough bulk rename — review the diff
   rg -l 'example|Example|EXAMPLE' | xargs sed -i '' \
     -e 's/blueprint-integration-hass/my-device-hass/g' \
     -e 's/example/my_device/g' \
     -e 's/Example/My Device/g'
   mv custom_components/example custom_components/my_device
   ```

3. Set GitHub secrets / settings:
   - Branch protection: require CI checks (`lint`, `test`, `hacs_validate`, …)
   - HACS: add custom repository of type *Integration*
   - Optional: PyPI-linked client library as a `requirements` pin in `manifest.json`

4. Delete `docs/BLUEPRINT.md` notes you no longer need; keep `docs/installation.md` patterns.

5. First push to `main` → release-please opens a release PR when you use conventional commits (`feat:`, `fix:`).

## Pre-release install (dogfood)

After CI is green on a same-repo PR:

1. Open the PR’s **pre-release** on GitHub Releases (tag `vX.Y.Z-pr.<n>.…`).
2. Download **`example.zip`** (or enable HACS pre-releases and pick that version).
3. Confirm `custom_components/<domain>/manifest.json` `"version"` matches the pre-release (not the last stable).

See [docs/pre-releases.md](docs/pre-releases.md).

## Relationship to the Python client

Prefer a separate package (see [blueprint-library-py](https://github.com/KRoperUK/blueprint-library-py)) for cloud/API/protocol logic. The integration should stay a thin HA layer: config flow, coordinators, entities, repairs, diagnostics.

## License

MIT — copy freely into new product repos.
