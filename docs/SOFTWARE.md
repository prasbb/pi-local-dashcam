# Software Design

## Operating system

Initial target:

- Raspberry Pi OS Lite, 64-bit
- Read-only or protected root filesystem considered after prototype validation
- Application data stored on NVMe
- `systemd` used for service supervision

## Proposed components

### Capture service

Responsibilities:

- discover the assigned video device,
- validate resolution and codec,
- start FFmpeg or GStreamer,
- write short timestamped segments,
- expose health status,
- recover after camera reconnection.

### Event manager

Event sources:

- IMU acceleration threshold,
- manual button,
- local API request,
- optional computer-vision event.

On an event, the manager protects:

- a configurable period before the event,
- the current segment,
- a configurable period after the event,
- matching front and rear segments,
- associated audio and metadata.

### Storage manager

Responsibilities:

- monitor free space,
- maintain a reserved free-space threshold,
- delete the oldest unprotected files,
- never delete protected events during ordinary cleanup,
- detect orphaned metadata or files,
- periodically verify storage health.

### Device-health service

Monitors:

- camera presence,
- camera frame flow,
- SSD state,
- filesystem space,
- Pi temperature,
- supply voltage warnings,
- GPS state,
- IMU state,
- service restart count.

### Local API

Suggested stack: FastAPI.

Initial endpoints:

```text
GET  /api/v1/status
GET  /api/v1/cameras
GET  /api/v1/clips
GET  /api/v1/clips/{clip_id}
POST /api/v1/events
POST /api/v1/settings
POST /api/v1/shutdown
```

No endpoint should require cloud access.

## Recording command concept

An early FFmpeg experiment may resemble:

```bash
ffmpeg \
  -f v4l2 \
  -input_format h264 \
  -video_size 1920x1080 \
  -framerate 30 \
  -i /dev/video0 \
  -c:v copy \
  -f segment \
  -segment_time 60 \
  -reset_timestamps 1 \
  "/data/dashcam/continuous/front/%Y-%m-%dT%H-%M-%S_front.mp4"
```

The exact command depends on the selected camera, supported formats, and timestamp requirements.

## Configuration

The initial configuration lives in `config/default.yaml`.

Configuration categories:

- camera device mapping,
- resolution and frame rate,
- segment duration,
- recording directories,
- storage thresholds,
- event windows,
- IMU thresholds,
- access-point settings,
- power-loss shutdown delay,
- logging levels.

## Metadata schema

Suggested `clips` table:

| Column | Purpose |
|---|---|
| `id` | Unique clip identifier |
| `camera` | `front`, `rear`, or other |
| `start_time_utc` | Segment start |
| `end_time_utc` | Segment end |
| `path` | Local file path |
| `protected` | Loop-deletion protection |
| `event_id` | Associated incident |
| `size_bytes` | File size |
| `codec` | Video codec |
| `sha256` | Optional integrity hash |

Suggested `events` table:

| Column | Purpose |
|---|---|
| `id` | Unique event identifier |
| `event_time_utc` | Trigger time |
| `event_type` | Impact, manual, API, or other |
| `severity` | Optional normalized score |
| `latitude` / `longitude` | GNSS location when available |
| `speed` | GNSS speed when available |
| `notes` | Local annotation |

## Security baseline

- Bind the management interface only to the private local network.
- Require authentication for clip access and settings.
- Disable password-based SSH after initial setup.
- Do not expose router ports.
- Store Wi-Fi credentials with restricted permissions.
- Sign update packages in later milestones.
- Consider full-disk or clip-level encryption after performance testing.

## Coding standards

- Python 3.12 or later where available.
- Type hints for public functions.
- Structured logging.
- Unit tests for storage and event logic.
- Integration tests with recorded sample streams.
- No silent exception handling.
- Hardware failures represented explicitly in health status.
