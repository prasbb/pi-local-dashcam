# Roadmap

## Phase 0 — Architecture

- [x] Select one-controller architecture.
- [x] Reject Bluetooth as the primary video transport.
- [x] Define local-first privacy model.
- [x] Define initial Raspberry Pi hardware direction.
- [x] Create initial repository documentation.

## Phase 1 — Bench prototype

- [ ] Select two UVC cameras.
- [ ] Confirm camera-side H.264/H.265 output.
- [ ] Install Raspberry Pi OS Lite.
- [ ] Attach NVMe storage.
- [ ] Record two simultaneous streams.
- [ ] Implement segmented recording.
- [ ] Add camera-health monitoring.
- [ ] Measure thermals and power consumption.

## Phase 2 — Loop recording and events

- [ ] Add SQLite metadata index.
- [ ] Add free-space management.
- [ ] Add protected-event handling.
- [ ] Add physical event button.
- [ ] Add IMU-triggered events.
- [ ] Add pre-event and post-event windows.

## Phase 3 — Vehicle power integration

- [ ] Select automotive-rated converter.
- [ ] Add ACC detection.
- [ ] Add low-voltage cutoff.
- [ ] Add supercapacitor or UPS shutdown reserve.
- [ ] Validate repeated power cycles.
- [ ] Implement parking modes.

## Phase 4 — Local interface

- [ ] Add FastAPI service.
- [ ] Add private Wi-Fi access point.
- [ ] Add authenticated local web interface.
- [ ] Add live preview.
- [ ] Add clip browsing and download.
- [ ] Add Bluetooth-assisted onboarding.

## Phase 5 — Reliability

- [ ] Eight-hour and multi-day soak tests.
- [ ] Camera disconnect recovery.
- [ ] Storage failure handling.
- [ ] Thermal-management policy.
- [ ] Read-only root filesystem.
- [ ] Structured diagnostics export.
