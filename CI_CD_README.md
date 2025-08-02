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
  4. **Upload Job**: Uploads all artifacts to GitHub Release (not PyPI)
- **Features**:
  - Comprehensive test coverage with Codecov integration
  - Cross-platform wheel building with `cibuildwheel`
  - Tests package installation during wheel building
  - Fail-fast: stops on first test failure
  - Automatic GitHub Release publishing with formatted release notes

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
- **📦 Release**: On GitHub releases, wheels are automatically uploaded to the release assets

### GitHub Release Publishing

When you create a GitHub release, the pipeline will:

1. **Download** all built artifacts (wheels and source distribution)
2. **Upload** them as release assets to the GitHub release
3. **Generate** formatted release notes with:
   - List of included distribution files
   - Installation instructions
   - Platform compatibility information
   - Quality assurance notes

### Manual Installation from Releases

Users can install your package by:
1. Going to the [Releases page](https://github.com/ScienceAIHub/gym-super-mario-bros/releases)
2. Downloading the appropriate wheel for their platform/Python version
3. Installing with: `pip install <downloaded-wheel-file>`

### GitHub Release Setup

To publish packages with this pipeline:

1. **Create a GitHub Release**:
   - Go to repository → Releases → Create a new release
   - Choose a tag version (e.g., `v7.4.1`)
   - Add release title and description
   - Publish the release

2. **Automatic Upload**: The pipeline will automatically:
   - Build and test all wheels
   - Upload them as release assets
   - Generate professional release notes

### Manual Builds

You can trigger builds manually using the "workflow_dispatch" trigger in the Actions tab.

### Development Notes

- The `pyproject.toml` file configures modern Python packaging standards
- `setup.py` is maintained for compatibility but `pyproject.toml` takes precedence
- Wheels are tested by importing the package after installation
- Build artifacts are retained for 30 days for debugging purposes
