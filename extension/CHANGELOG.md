# Change Log

All notable changes to the AlibreScript extension will be documented in this file.

## [0.0.3] - 2025-10-22

### Added
- Standard .github folder with community files:
  - Bug report template
  - Feature request template
  - Pull request template
  - Contributing guidelines
  - Security policy

### Changed
- Updated README with early development notice
- Removed emojis and icons from extension README for cleaner presentation
- Clarified prerequisites: Python 3.6+ required for extension, IronPython 2.7.10 is used inside Alibre Design
- Updated requirements to properly list Python extension, Pylance, and Python Debugger as required
- Removed Alibre Design from prerequisites (only needed for script execution, not for development)
- Simplified CONTRIBUTING.md to reflect informal contribution process
- Updated feature list: replaced "Syntax Highlighting" with "Examples" for accuracy

## [0.0.2] - 2025-10-22

### Fixed
- `CurrentPart()` and `CurrentAssembly()` now return `Part` and `Assembly` types instead of `Optional[Part]` and `Optional[Assembly]`, eliminating the need for None checking when coding
