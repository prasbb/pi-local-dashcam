# Prototype Test Plan

## 1. Bench tests

### Camera discovery

- Confirm both cameras enumerate consistently after cold boot.
- Confirm stable device mapping.
- Record supported formats and frame rates.
- Test camera disconnect and reconnection.

### Simultaneous recording

- Record both cameras for at least two hours.
- Verify no dropped or corrupted segments.
- Verify aligned segment timestamps.
- Measure Raspberry Pi CPU, memory, USB bandwidth, and temperature.

### Storage

- Fill the data partition to the cleanup threshold.
- Verify only the oldest unprotected segments are deleted.
- Verify protected clips remain.
- Remove and reconnect the SSD during a controlled test.
- Test recovery after an intentionally interrupted recording.

### Event protection

- Trigger a manual event.
- Trigger an IMU event.
- Confirm front and rear clips are protected.
- Confirm pre-event and post-event windows are included.

## 2. Power tests

- Start from ignition-off state.
- Apply ignition and confirm automatic boot and recording.
- Remove ignition and confirm clean shutdown.
- Repeat at least 50 cycles.
- Test sudden primary-power loss.
- Confirm the backup supply has enough duration to finalize files.
- Test low-voltage cutoff behavior.

## 3. Thermal tests

- Record continuously in a warm controlled environment.
- Monitor Pi and SSD temperature.
- Verify thermal throttling does not corrupt footage.
- Verify the system records a thermal warning.
- Verify controlled shutdown at the configured critical threshold.

## 4. Vehicle tests

- Day driving.
- Night driving.
- Direct sunlight.
- Headlight glare.
- Rain.
- Rough road.
- Highway vibration.
- Rear-window heating elements.
- Vehicle start/stop cycles.
- Parking mode battery consumption.

## 5. Local-network tests

- Pair a phone over Bluetooth.
- Join the private Wi-Fi network.
- Preview each camera.
- Download a clip.
- Change a safe setting.
- Attempt access with an invalid password.
- Confirm recording continues when Wi-Fi is disabled.

## 6. Acceptance criteria for prototype milestone

- Two simultaneous 1080p30 compressed streams.
- Eight-hour continuous recording without capture failure.
- Clean recovery after camera reconnection.
- Clean shutdown after ignition loss.
- No deletion of protected events.
- Local clip browsing without internet.
- Rear camera operates reliably across the selected cable length.
