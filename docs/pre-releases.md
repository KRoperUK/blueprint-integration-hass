# Pre-releases and HACS

## Tag shapes

| Event | Version in tree | Git tag |
| --- | --- | --- |
| PR CI green | `X.Y.Z-pr.<PR>.<shortsha>` | `vX.Y.Z-pr.<PR>.<run_id>` |
| Push to `main` | `X.Y.Z-rc.N` | `vX.Y.Z-rc.N` |
| Stable release-please | `X.Y.Z` | `vX.Y.Z` |

The release points at a **synthetic commit** whose parent is the tested SHA; only version files differ. **`main` is never rewritten** for RCs.

## Why not `dev-v…` tags on the PR head?

Tagging the raw PR commit leaves `manifest.json` at the last stable version. HACS then thinks you installed an old stable, and the HA update entity may offer a confusing “update”. Semver pre-releases sort **above** the last stable and **below** the final `X.Y.Z`.

## Install

1. Enable pre-releases / beta for the repository in HACS, **or**
2. Download `example.zip` from the GitHub pre-release assets.

Confirm the running integration version (diagnostics / manifest) matches the pre-release string.
