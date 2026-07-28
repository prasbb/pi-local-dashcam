# Privacy and Security

## Privacy model

The dashcam is designed to operate without:

- a cloud account,
- remote telemetry,
- third-party video hosting,
- mobile data,
- mandatory internet access.

All footage and metadata remain on the vehicle's local storage unless the owner explicitly exports them.

## Threat model

The initial design should consider:

- theft of the central module or SSD,
- unauthorized local Wi-Fi access,
- weak default passwords,
- exposed management services,
- malicious firmware or update files,
- accidental clip deletion,
- physical access to USB ports,
- metadata leakage from exported files.

## Initial controls

- Generate a unique device password during setup.
- Use WPA2 or WPA3 for the private access point.
- Require authentication for live view, clip access, deletion, and settings.
- Disable unused services.
- Bind the API to the local interface only.
- Disable remote cloud dependencies.
- Record administrative actions in a local audit log.
- Protect event clips against ordinary loop deletion.
- Provide a clear method to erase all local data before resale or disposal.

## Encryption roadmap

Possible stages:

1. Unencrypted prototype filesystem for development.
2. Encrypted protected-event directory.
3. Full data-partition encryption with a locally managed key.
4. Optional phone-assisted unlock.
5. Hardware-backed keys in a product revision.

Encryption should not prevent automatic recording after vehicle startup unless that behavior is explicitly selected.

## Audio privacy

Audio recording laws and expectations vary by jurisdiction. The software should make microphone recording:

- disabled by default or clearly disclosed,
- easy to disable,
- visibly represented in the local interface,
- configurable independently from video.

## Data retention

Recommended policy controls:

- maximum ordinary-recording age,
- reserved storage for protected clips,
- automatic overwrite of ordinary clips,
- manual deletion of protected clips,
- full-device erase,
- export with optional metadata removal.

## No hidden access

The project should not include:

- undisclosed remote-access services,
- default vendor cloud accounts,
- silent telemetry,
- hidden administrative credentials.
