# Contributing

This project is in an early prototype stage. Contributions should prioritize reliability, privacy, and clear failure handling.

## Before opening a change

1. Describe the problem being solved.
2. State the hardware used for testing.
3. Explain any impact on recording reliability.
4. Explain any impact on local privacy or security.
5. Include repeatable test steps.

## Development principles

- Do not add mandatory cloud services.
- Do not use Bluetooth for primary video transport.
- Keep front and rear capture failures isolated.
- Avoid hidden telemetry.
- Preserve protected events.
- Prefer explicit error states over silent failure.
- Document vehicle-power and safety assumptions.

## Python style

- Use Python 3.12-compatible syntax.
- Add type hints to public functions.
- Use structured logging.
- Add tests for non-trivial logic.
- Keep hardware-specific code behind clear interfaces.

## Commit style

Examples:

```text
docs: document power-loss shutdown sequence
feat: add camera discovery command
fix: preserve protected clips during cleanup
test: add storage-threshold integration test
```
