#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from .core import get_channel_id, get_channel_title, get_video_urls
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
import subprocess

console = Console()

def main():
    console.print("\n[bold cyan]YouTube Month Downloader v1.0.0[/]\n", justify="center")

    handle = Prompt.ask("Enter channel handle", default="@Sehnend.")
    year = IntPrompt.ask("Enter year", default=2025)
    month = IntPrompt.ask("Enter month (1-12)", choices=[str(i) for i in range(1,13)], default=10)

    api_key = os.getenv("YT_API_KEY")
    if not api_key:
        api_key = Prompt.ask("Enter YouTube API Key", password=True)
        if not api_key:
            console.print("[red]API key required![/]")
            sys.exit(1)

    try:
        with console.status("Resolving channel..."):
            channel_id = get_channel_id(api_key, handle)
            channel_title = get_channel_title(api_key, channel_id)
        console.print(f"[green]Channel:[/] {channel_title}")

        with console.status("Searching videos..."):
            urls = get_video_urls(api_key, channel_id, year, month)

        if not urls:
            console.print(f"[yellow]No videos found in {year}-{month:02d}[/]")
            return

        folder = Path(f"{channel_title}_{year}-{month:02d}")
        folder.mkdir(exist_ok=True)
        console.print(f"[green]Found {len(urls)} video(s) →[/] [bold]{folder}[/]")

        url_file = folder / ".urls.txt"
        url_file.write_text("\n".join(urls))

        console.print("Starting download...")
        cmd = [
            "yt-dlp",
            "-a", str(url_file),
            "--output", str(folder / "%(title)s [%(id)s].%(ext)s"),
            "--no-overwrites",
            "--continue",
            "--ignore-errors",
            "--format", "bestvideo[height<=1080]+bestaudio/best",
            "--merge-output-format", "mp4"
        ]
        result = subprocess.run(cmd, cwd=folder.parent)
        url_file.unlink(missing_ok=True)

        if result.returncode == 0:
            console.print(f"\n[bold green]All done! Saved in:[/] [cyan]{folder}[/]")
        else:
            console.print("[red]Some downloads failed.[/]")

    except Exception as e:
        console.print(f"[red]Error:[/] {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()