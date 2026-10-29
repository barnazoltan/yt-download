##YouTube-to-MP3 Batch Downloader

A lightweight, containerized web application built with Flask and `yt-dlp` that allows users to batch download YouTube videos as MP3 files from a simple text file containing URLs.

## Features

- **Batch Processing**: Upload a `.txt` file with multiple YouTube links (one per line).
- **Automatic Conversion**: Extracts and converts video streams to high-quality MP3 files using `ffmpeg`.
- **ZIP Archive Delivery**: Automatically packs all converted MP3s into a single ZIP archive for easy download.
- **Dockerized**: Fully containerized for portable and isolated deployment.

## Tech Stack

- **Backend**: Python, Flask, `yt-dlp`
- **Media Processing**: `ffmpeg`
- **Containerization**: Docker

## Getting Started (Run with Docker)

Make sure you have [Docker](https://www.docker.com/) installed on your machine.

1. Clone the repository:
   ```bash
   git clone [https://github.com/barnaZoltan/yt-download.git](https://github.com/barnaZoltan/yt-download.git)
   cd yt-download
2. Build the Image
   ```bash
   docker build -t yt-download-app .
3. Run the container
  ```bash
   docker run -p 5000:5000 yt-download-app
4. Open with
   http://localhost:5000
