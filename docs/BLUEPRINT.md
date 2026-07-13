# Blueprint checklist (integration)

Copy this into the product repo’s internal notes, then tick as you implement.

## Must-have for HACS / HA

- [ ] `custom_components/<domain>/manifest.json` — correct `domain`, `version`, `iot_class`, `requirements`, `loggers`
- [ ] `strings.json` + at least `translations/en.json`
- [ ] Config flow with reauth when tokens/credentials die
- [ ] `DataUpdateCoordinator` (or equivalent) with backoff / grace for flaky APIs
- [ ] Diagnostics (`async_get_config_entry_diagnostics`) with redaction
- [ ] Unique IDs stable across reloads
- [ ] Options flow uses `OptionsFlowWithReload` (do not reload on every token write)
- [ ] Entity categories: diagnostics for health/internals; config for settings

## Quality scale (aim Gold → Platinum)

- [ ] Exception translations for user-visible write failures
- [ ] Repairs for actionable cloud/config failures (whitelist, rate limit, …)
- [ ] Parallel update limits on write platforms
- [ ] Assumed state only where API has no read-back
- [ ] Brands icons (`brand` assets / icons.json as needed)

## Cloud + optional local

- [ ] Single config entry for hybrid (cloud options host for local transport)
- [ ] Discovery attach to existing cloud entry (avoid duplicate devices)
- [ ] Reverse attach when local-first user later adds cloud
- [ ] Tag `source=` on realtime points (`cloud` / `modbus` / `derived`)
- [ ] Never let local transport take the plant offline if cloud still works

## CI / release

- [ ] Path-filtered CI (docs-only PRs skip heavy jobs)
- [ ] Semver pre-releases with synthetic version commit + HACS zip
- [ ] release-please for stable; pin versions in both `manifest.json` and `const.VERSION`
- [ ] Cleanup PR pre-releases on close

## Client library boundary

- [ ] Protocol/API in a separate PyPI package
- [ ] Integration pins an exact library version in `manifest.json` `requirements`
- [ ] No secrets in logs; debug logs must not dump tokens
