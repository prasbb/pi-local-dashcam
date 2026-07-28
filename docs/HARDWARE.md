# Hardware and Provisional BOM

## Prototype target

The initial prototype is a dual-camera, fully local recorder using one Raspberry Pi 5 and one NVMe SSD.

## Recommended bill of materials

| Item | Quantity | Target specification | Estimated subtotal |
|---|---:|---|---:|
| Raspberry Pi 5 | 1 | 4 GB recommended | $70–$100 |
| Active cooler | 1 | Pi 5-compatible | $5–$15 |
| Front UVC camera | 1 | 1080p/1440p, H.264, WDR | $45–$80 |
| Rear UVC camera | 1 | 1080p/1440p, H.264, WDR | $45–$80 |
| Active USB extension | 1 | 3–5 m, powered if required | $15–$35 |
| M.2 HAT | 1 | Pi 5-compatible | $12–$25 |
| High-endurance NVMe SSD | 1 | 1 TB | $60–$100 |
| Pi enclosure | 1 | Ventilated, SSD-compatible | $15–$35 |
| Automotive buck converter | 1 | 12 V to regulated 5 V, 5 A class | $25–$50 |
| Shutdown backup | 1 | Supercapacitor or short-duration UPS | $25–$60 |
| Low-voltage cutoff | 1 | Configurable vehicle-battery protection | $15–$35 |
| GNSS receiver | 1 | USB or UART | $15–$35 |
| IMU module | 1 | I2C accelerometer/gyroscope | $5–$20 |
| Wiring, fuse, mounts | 1 set | Automotive-appropriate | $25–$50 |

**Provisional total:** approximately **$400–$500**.

The estimate does not include custom PCBs, compliance testing, professional installation, automotive certification, or product-grade enclosures.

## Camera requirements

Prioritize:

- Linux UVC compatibility,
- hardware H.264/H.265 output,
- 30 fps or better,
- wide dynamic range,
- low-light performance,
- 120–160 degree field of view,
- stable fixed-focus behavior,
- exposure control,
- operating-temperature documentation,
- locking or strain-relieved connectors.

Avoid cameras that only provide uncompressed high-resolution output. Two raw streams can create unnecessary USB and CPU load.

## Raspberry Pi memory

- **2 GB:** adequate for a minimal capture-only proof of concept.
- **4 GB:** recommended for the main prototype.
- **8 GB:** useful only when adding heavier computer-vision processing or a large local interface.

## Storage sizing

Approximate continuous-recording storage:

| Combined bitrate | Data per day | Approximate usable retention on 1 TB |
|---:|---:|---:|
| 10 Mbps | 108 GB | 8 days |
| 16 Mbps | 173 GB | 5 days |
| 24 Mbps | 259 GB | 3 days |

Actual capacity depends on filesystem overhead, reserved free space, audio, metadata, bitrate variability, and protected events.

## Thermal considerations

The central module should:

- use active cooling,
- avoid direct sunlight when possible,
- include temperature monitoring,
- reduce bitrate or stop recording before unsafe thermal conditions,
- avoid placing the SSD directly against a heat source,
- use a ventilated prototype enclosure.

A Raspberry Pi prototype is not automatically suitable for all parked-vehicle temperature conditions.

## Microphone options

1. Use microphones built into the cameras.
2. Add one centrally mounted USB microphone.
3. Add a dedicated I2S microphone in a later custom enclosure.

Bluetooth microphones are not recommended for primary recording because reconnect behavior and audio/video timing can be unreliable.

## Future hardware revision

A product-oriented version may replace:

- USB with GMSL2, FPD-Link, or automotive Ethernet,
- removable USB connectors with locking automotive connectors,
- the Pi carrier arrangement with a custom PCB,
- consumer power accessories with an integrated automotive power controller,
- a consumer SSD with temperature-rated managed storage.
