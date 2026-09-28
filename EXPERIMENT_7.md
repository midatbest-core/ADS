# Experiment 7: CI/CD Pipeline with Open Source Tools

## Aim
CI/CD Pipeline with Open Source Tools.

## Objective
Automate testing, version checks, and deployment using GitHub Actions.

## Tools Used
- GitHub Actions
- Git
- DVC
- Python
- Flake8
- Pytest

## CI Pipeline

The GitHub Actions workflow is stored at:

`.github/workflows/ci.yml`

The workflow runs automatically when changes are pushed to the `main` branch or when a pull request targets `main`.

### Test Job
- Sets up Python 3.11
- Installs project dependencies
- Installs DVC
- Checks DVC tracking status
- Runs Pytest when a `tests` directory is available

### Lint Job
- Sets up Python 3.11
- Installs Flake8
- Performs Python code quality checks

### Build Job
- Sets up Python 3.11
- Installs project dependencies
- Compiles Python files using `compileall` to detect syntax errors

## DVC

The revenue-enhanced dataset is tracked using DVC.

The actual dataset is stored in the configured DVC storage, while the `.dvc` metadata file is version-controlled through Git.

## Conclusion

A CI/CD workflow was created using GitHub Actions with separate test, lint, and build jobs. DVC tracking was also incorporated into the pipeline to support dataset version control. The workflow is configured to execute automatically on changes to the main branch and pull requests.
