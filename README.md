markdown# YouTube Month Downloader (`v1.0.0`)

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/yourname/yt-month-downloader/releases/tag/v1.0.0)
[![Python](https://img.shields.io/badge/python-3.8%2B-green)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

**Download every video from a YouTube channel in a specific month** — automatically saved into a clean folder:
Sehnend_2025-10/
├── My Deep Video [abc123].mp4
├── Philosophy Explained [xyz789].mp4
└── The Meaning of Life [def456].mp4
text---

## Features

- **Works with `@handle`** → `@Sehnend.` (no URL parsing bugs)
- **No extra API calls** — uses `forHandle` + `search.list`
- **Auto folder naming**: `ChannelName_YYYY-MM`
- **Skips already downloaded videos**
- **Max 1080p + audio**, merged to `.mp4`
- **Beautiful CLI** with `rich` (progress, prompts, colors)
- **Versioned, installable, GitHub-ready**

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/yourname/yt-month-downloader.git
cd yt-month-downloader

# 2. Install
pip install .

# 3. (Recommended) Install yt-dlp globally
pip install yt-dlp

Usage
Option 1: API Key in Environment (Recommended)
export YT_API_KEY="your_actual_api_key_here"
yt-month
Option 2: Enter Key at Prompt
yt-month
    You will be prompted:
    Enter channel handle: @Sehnend.
    Enter year: 2025
    Enter month (1-12): 10
Example Output
YouTube Month Downloader v1.0.0

Enter channel handle: @Sehnend.
Enter year: 2025
Enter month (1-12): 10
Channel: Sehnend
Found 3 video(s) → Sehnend_2025-10/
Starting download...
[download] Destination: Sehnend_2025-10/Deep Thoughts [abc123].mp4
...
All done! Saved in: Sehnend_2025-10/

Folder Structure After Download
yt-month-downloader/
├── Sehnend_2025-10/
│   ├── Deep Thoughts [abc123].mp4
│   ├── Philosophy [xyz789].mp4
│   └── .urls.txt (deleted)
├── yt_month_downloader/
│   ├── __init__.py
│   ├── __main__.py
│   └── core.py
├── pyproject.toml
├── README.md
└── .gitignore

Development
# Edit code
nano yt_month_downloader/core.py

# Test without installing
python -m yt_month_downloader

# Build wheel
python -m build

Versioning
Version,Description
v1.0.0,First stable release
v1.1.0,"(Planned) Config file, GUI, batch mode"

Requirements

Python 3.8+
YouTube Data API v3 key
yt-dlp (for downloading)


License
MIT License – Free to use, modify, and distribute.

Author
Your Chris
GitHub: @Developer-chris01
















```
