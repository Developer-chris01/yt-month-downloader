import requests
from pathlib import Path
from typing import List
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console

console = Console()
API_BASE = "https://www.googleapis.com/youtube/v3"

def get_channel_id(api_key: str, handle: str) -> str:
    handle_name = handle.lstrip("@")
    url = f"{API_BASE}/channels"
    params = {
        "part": "id,snippet",
        "forHandle": handle_name,
        "key": api_key
    }
    resp = requests.get(url, params=params)
    resp.raise_for_status()
    data = resp.json()
    if not data.get("items"):
        raise ValueError(f"Channel not found for handle: {handle}")
    return data["items"][0]["id"]

def get_channel_title(api_key: str, channel_id: str) -> str:
    url = f"{API_BASE}/channels"
    params = {"part": "snippet", "id": channel_id, "key": api_key}
    resp = requests.get(url, params=params).json()
    title = resp["items"][0]["snippet"]["title"]
    return "".join(c if c.isalnum() else "_" for c in title)

def get_video_urls(api_key: str, channel_id: str, year: int, month: int) -> List[str]:
    after = f"{year}-{month:02d}-01T00:00:00Z"
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    before = f"{next_year}-{next_month:02d}-01T00:00:00Z"

    urls = []
    page_token = ""
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "type": "video",
        "order": "date",
        "maxResults": 50,
        "publishedAfter": after,
        "publishedBefore": before,
        "key": api_key
    }

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True
    ) as progress:
        task = progress.add_task("Fetching videos...", total=None)
        while True:
            if page_token:
                params["pageToken"] = page_token
            resp = requests.get(f"{API_BASE}/search", params=params)
            resp.raise_for_status()
            data = resp.json()
            batch = [
                f"https://www.youtube.com/watch?v={item['id']['videoId']}"
                for item in data.get("items", [])
            ]
            urls.extend(batch)
            page_token = data.get("nextPageToken")
            if not page_token:
                break
        progress.update(task, completed=True)

    return urls