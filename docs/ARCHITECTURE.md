# System Architecture

## 1. Overview

The system uses a star topology centered on one Raspberry Pi 5. Every sensor, camera, storage device, and local user interface communicates with this controller.

```mermaid
flowchart TD
    subgraph Vehicle
        FC[Front camera]
        RC[Rear camera]
        CM[Cabin microphone]
        GNSS[GNSS receiver]
        IMU[IMU]
        ACC[Ignition / ACC signal]
        BATT[12 V vehicle supply]
    end

    FC -->|UVC / USB| PI[Raspberry Pi 5]
    RC -->|UVC / active USB| PI
    CM -->|USB Audio| PI
    GNSS -->|USB or UART| PI
    IMU -->|I2C| PI
    ACC --> PM[Power controller]
    BATT --> PM
    PM -->|Regulated 5 V| PI
    PI --> NVME[NVMe storage]
    PI <-->|Local Wi-Fi| CLIENT[Phone or laptop]
    PI <-->|Bluetooth control| CLIENT
```

## 2. Why one central controller

A single controller reduces:

- duplicated compute boards,
- duplicated storage,
- duplicated power regulation,
- software deployment complexity,
- synchronization problems,
- enclosure count,
- maintenance effort.

The cameras should contain only the sensor, lens, image processor, hardware encoder, and transport interface needed to deliver a compressed stream.

## 3. Camera transport

### Prototype: USB UVC cameras

The first prototype should use UVC-compatible USB cameras that can output H.264 or H.265. Camera-side compression reduces Raspberry Pi CPU load and USB bandwidth.

Requirements:

- 1080p30 minimum,
- hardware-compressed output,
- wide dynamic range,
- low-light capability,
- stable Linux UVC support,
- wide-angle lens,
- configurable exposure,
- timestamp consistency.

The rear camera should use an active USB extension or a powered USB transport appropriate for the cable length.

### Later alternatives

| Transport | Use case | Advantages | Limitations |
|---|---|---|---|
| USB UVC | Initial prototype | Low cost, easy Linux support | Cable length and connector robustness |
| Ethernet/PoE | Advanced prototype | One cable for data and power | Larger camera modules and switch hardware |
| Automotive Ethernet | Product direction | Vehicle-oriented networking | Higher integration effort |
| GMSL2 / FPD-Link | Automotive product | Long cable, low latency, robust synchronization | More expensive and specialized |
| Wi-Fi | Temporary experimentation | No long cable | Interference, latency, packet loss |
| Bluetooth | Controls only | Low-power pairing | Unsuitable for continuous video |

## 4. Recording pipeline

```mermaid
flowchart LR
    CAM1[Front encoded stream] --> CAPTURE[Capture service]
    CAM2[Rear encoded stream] --> CAPTURE
    MIC[Audio stream] --> CAPTURE
    CLOCK[GNSS / system clock] --> CAPTURE
    CAPTURE --> SEGMENTS[Short recording segments]
    SEGMENTS --> INDEX[SQLite metadata index]
    SEGMENTS --> LOOP[Loop-storage manager]
    IMU[Impact event] --> EVENT[Event manager]
    BUTTON[Manual event] --> EVENT
    EVENT --> LOCK[Protect related segments]
    LOOP --> DELETE[Delete oldest unprotected segments]
```

Recommended segment duration: one to five minutes. Short segments limit corruption when power is lost and simplify event protection.

## 5. Process boundaries

Suggested services:

- `dashcam-capture-front`
- `dashcam-capture-rear`
- `dashcam-audio`
- `dashcam-event-manager`
- `dashcam-storage-manager`
- `dashcam-device-health`
- `dashcam-local-api`
- `dashcam-power-monitor`

Each service should be restartable independently.

## 6. Failure behavior

| Failure | Expected behavior |
|---|---|
| Front camera disconnected | Rear recording continues; health event logged |
| Rear camera disconnected | Front recording continues; health event logged |
| SSD unavailable | Stop recording safely; raise local warning |
| Wi-Fi unavailable | Recording continues |
| Bluetooth unavailable | Recording continues |
| GPS unavailable | Use monotonic/system clock and flag metadata |
| Sudden ignition loss | Backup power completes current file and shuts down |
| Service crash | `systemd` restarts the affected service |
| Storage threshold reached | Delete oldest unprotected segments |

## 7. Time synchronization

All streams should use one controller clock. GNSS time may discipline the system clock when available. Front and rear filenames should share the same timestamp convention.

Example:

```text
2026-07-28T18-22-00Z_front.mp4
2026-07-28T18-22-00Z_rear.mp4
```

## 8. Local interfaces

Bluetooth should provide:

- initial pairing,
- basic device status,
- Wi-Fi credential exchange,
- event marking,
- low-bandwidth configuration.

Private Wi-Fi should provide:

- live preview,
- clip browsing,
- clip download,
- settings,
- diagnostics,
- local firmware update.

Core recording must remain independent of both interfaces.
