# Changelog

All notable changes to Project UTEXAS DECWAR are recorded here.

## [1.3.0] - 2026-08-01
### Changed
- Improved the README and project documentation for clarity and future expansion.
- Included the previously missed `setup.for` file in the cleanup process.

## [1.2.0] - 2026-02-07
### Changed
- Migrated the repository to `github.com/decwarorg/utexas`.
- Cleaned up `warmac` and verified the release with a Docker build.

## [1.1.0] - 2025-12-01
### Added
- Added an `oddities/` directory for files referenced in commentary but not listed in `DECWAR.TAP`.
- Preserved uncertain files in a staging area for later review.

## [1.0.0] - 2025-11-09
### Added
- Initial public release of Project UTEXAS.

## 2025-11-30
### Changed
- Improved Docker Compose integration with bind-mounted `utexas23-reconstruction`.
- Enabled live source updates inside the container without rebuilding the tape image.

## 2025-08-14
### Added
- Updated robot behavior to start aggressively and transition tactics after surviving long enough.
- Documented Raspberry Pi setup issues and recovery steps in the main README.

## 2025-07-19
### Fixed
- Corrected a `tell` command defect caused by incorrect hit-link list allocation in `warmac`.
- Changed `knhit==knhshp*^d10` to `knhit==knhshp*^d18` to prevent message-list corruption.

## 2025-07-13
### Added
- Published the first public `workflow1` process for hardware and software setup.
- Added `boot-from-disk-fast.ini` to reach the TOPS-10 prompt without rebuilding from tape.
- Documented robot launch and log monitoring workflows.

### Notes
- Continued work on TOPS-10 locking and unlocking behavior using `enq`, `deq`, and `uuo`.
- Continued investigation into the `tell` command and message queue behavior.
- Continued troubleshooting Raspberry Pi PIDP-10 instability and reset procedures.

## 2025-05-11
### Added
- First public mention of Project UTEXAS in the DECWAR GitHub discussion: https://github.com/drforbin/decwar/discussions/27
