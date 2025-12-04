# Continuous Integration Setup

## Overview
This project includes automated testing via a bash script that can be integrated into any CI/CD pipeline.

## Running Tests Locally
```bash
./run_tests.sh
```

## What the Script Does

1. **Activates virtual environment** - Ensures tests run in isolated environment
2. **Checks dependencies** - Verifies all required packages are installed
3. **Runs test suite** - Executes all tests in `tests/test_app_simple.py`
4. **Returns exit codes**:
   - `0` = All tests passed 
   - `1` = Tests failed or error occurred 

## Exit Codes

The script follows standard Unix conventions:
- Exit code `0`: Success - all tests passed
- Exit code `1`: Failure - tests failed or dependencies missing

## CI/CD Integration

This script can be integrated into any CI/CD platform:

### GitHub Actions
See `.github/workflows/test.yml` for automated testing on every push.

### Jenkins
```groovy
stage('Test') {
    steps {
        sh './run_tests.sh'
    }
}
```

### GitLab CI
```yaml
test:
  script:
    - ./run_tests.sh
```

### CircleCI
```yaml
jobs:
  test:
    steps:
      - run: ./run_tests.sh
```

## Test Coverage

The test suite verifies:
- ✅ Dash app exists and has valid layout
- ✅ Data loaded correctly (5,880 rows from 3 CSV files)
- ✅ All UI components present (header, chart, region filter)
- ✅ Interactive callbacks registered

## Manual Testing

To run tests without the CI script:
```bash
source venv/bin/activate
python tests/test_app_simple.py
```
