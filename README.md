# PYB Fitness Web App

This repository contains the static HTML pages for the PYB Fitness application.

## Running the tests

The project uses `pytest` together with `beautifulsoup4` for HTML validation tests.
Install the test dependencies and run `pytest` from the repository root:

```bash
pip install pytest beautifulsoup4
pytest
```

The provided test checks that all navigation links in each HTML page point to
files that actually exist in the repository.
