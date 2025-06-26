# 1001 Albums Generator – LaMetric Display App

This is a LaMetric Time app that shows your daily album from [1001albumsgenerator.com](https://1001albumsgenerator.com), along with your personal progress through the "1001 Albums You Must Hear Before You Die" list.

## How it works

The app connects to the 1001 Albums Generator API and displays:

- The current album title  
- The artist name  
- Your current progress (e.g., "Album 37 of 1001" or "FINISHED")

## Requirements

- A LaMetric Time device  
- An account at [1001albumsgenerator.com](https://1001albumsgenerator.com)  
- Your personal project slug

## Setup

1. Install the app on your LaMetric device  
2. Enter your project slug in the app settings (e.g., `6830174f8f99d23180874bfb`)  
3. The app will show your current album and progress

## Polling frequency

The app is designed to check for updates every **1 hours**, as the 1001 Albums Generator typically updates once per day.

## Privacy

This app only reads data from the public API using your personal slug. No data is stored or shared.

Privacy Policy: [https://github.com/jimscheel/lametric-album/blob/main/privacy.md](https://github.com/jimscheel/lametric-album/blob/main/privacy.md)

## Credits

Created by Jimmy Fjeldbonde  
Powered by the 1001 Albums Generator API
