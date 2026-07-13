# Agent notes (integration blueprint)

- Prefer thin HA integration + separate PyPI client library.
- Never log tokens / app secrets; use redacted diagnostics.
- Use `OptionsFlowWithReload` so token refreshes do not reload the integration.
- Tag realtime points with `source` when multiple transports exist.
- Conventional commits drive release-please.
- Dev installs must use semver pre-release tags (see `docs/pre-releases.md`), not raw branch tips with stale `manifest.json` versions.
