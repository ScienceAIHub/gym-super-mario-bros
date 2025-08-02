# CI/CD Pipeline Documentation

## Automated Testing and Wheel Building

This repository includes GitHub Actions workflows that automatically run tests and build wheel packages for multiple platforms and Python versions.

### Pipeline Overview

The CI/CD pipeline follows a **test-first approach**:

1. **🧪 Test Phase**: Run comprehensive tests on all supported platforms and Python versions
2. **🔨 Build Phase**: Build wheels only if all tests pass
3. **📦 Publish Phase**: Publish to PyPI on releases (if tests and builds succeed)

### Build Matrix

The pipeline runs tests and builds wheels for:
- **Operating Systems**: Ubuntu (Linux) and Windows
- **Python Versions**: 3.11 and 3.12
- **Architectures**: x86_64 (Linux), AMD64 (Windows)

### Workflows

#### `ci.yml` - Complete CI/CD Pipeline
- **Trigger**: Every push to `master` branch, pull requests, and releases
- **Pipeline Steps**:
  1. **Test Job**: Runs pytest with coverage on all OS/Python combinations
  2. **Build Wheels Job**: Uses `cibuildwheel` for robust wheel building  
  3. **Build Source Job**: Creates source distribution tarball
  4. **Publish Job**: Publishes all artifacts to PyPI on releases
- **Features**:
  - Comprehensive test coverage with Codecov integration
  - Cross-platform wheel building with `cibuildwheel`
  - Tests package installation during wheel building
  - Fail-fast: stops on first test failure
  - Automatic PyPI publishing on GitHub releases

### Test Coverage

The pipeline includes comprehensive testing:
- **Unit Tests**: All existing tests in `gym_super_mario_bros/tests/`
- **Import Tests**: Verifies package can be imported successfully
- **Coverage Reporting**: Generates coverage reports (uploaded to Codecov in advanced pipeline)
- **Cross-platform Testing**: Tests run on both Linux and Windows

### Artifacts

Built wheels are uploaded as GitHub Actions artifacts and can be downloaded from the Actions tab. Artifacts include:
- `cibw-wheels-ubuntu-20.04` - Linux wheels for Python 3.11 and 3.12
- `cibw-wheels-windows-2019` - Windows wheels for Python 3.11 and 3.12
- `cibw-sdist` - Source distribution (tarball)

### Pipeline Behavior

- **🟢 All Tests Pass**: Pipeline proceeds to build wheels and artifacts
- **🔴 Any Test Fails**: Pipeline stops immediately, no wheels are built
- **⚠️ Build Fails**: Tests passed but wheel building failed (likely dependency issue)
- **📦 Release**: On GitHub releases, wheels are automatically published to PyPI

### PyPI Publishing

For automatic PyPI publishing on releases:

1. **Set up PyPI trusted publishing** (recommended):
   - Go to repository Settings → Environments
   - Create environment named `pypi`
   - Configure the PyPI trusted publisher for this repository

2. **Alternative: Use API token**:
   - Create a PyPI API token
   - Add it as repository secret `PYPI_API_TOKEN`
   - Uncomment the token-based authentication in the workflow

### Manual Builds

You can trigger builds manually using the "workflow_dispatch" trigger in the Actions tab.

### Development Notes

- The `pyproject.toml` file configures modern Python packaging standards
- `setup.py` is maintained for compatibility but `pyproject.toml` takes precedence
- Wheels are tested by importing the package after installation
- Build artifacts are retained for 30 days for debugging purposes
