"""
Record Label Composer
Build 002 - Workbench

version.py
Provides version information for the application.
"""

from constants import (
    APP_NAME,
    VERSION,
    BUILD,
    BUILD_NAME,
    APP_TAGLINE,
)


def application_title() -> str:
    """Return the title displayed in the main window."""
    return f"{APP_NAME} - Build {BUILD} ({BUILD_NAME})"


def version_string() -> str:
    """Return a human-friendly version string."""
    return f"Version {VERSION} | Build {BUILD} - {BUILD_NAME}"


def about_text() -> str:
    """Return text for the About dialog."""
    return (
        f"{APP_NAME}\n"
        f"{version_string()}\n\n"
        f"{APP_TAGLINE}"
    )


if __name__ == "__main__":
    print(application_title())
    print(version_string())
