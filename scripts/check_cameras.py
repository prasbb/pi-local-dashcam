#!/usr/bin/env python3
"""List Linux video devices and basic V4L2 information."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


def main() -> int:
    devices = sorted(Path("/dev").glob("video*"))

    if not devices:
        print("No /dev/video* devices found.")
        return 1

    print("Detected video devices:")
    for device in devices:
        print(f"  - {device}")

    v4l2_ctl = shutil.which("v4l2-ctl")
    if v4l2_ctl is None:
        print("\nInstall v4l-utils for detailed device information:")
        print("  sudo apt install v4l-utils")
        return 0

    print("\nV4L2 device summary:")
    result = subprocess.run(
        [v4l2_ctl, "--list-devices"],
        check=False,
        text=True,
        capture_output=True,
    )

    if result.stdout:
        print(result.stdout.strip())
    if result.stderr:
        print(result.stderr.strip())

    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
