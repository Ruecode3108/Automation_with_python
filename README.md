# Automation_with_python
A collection of Python Automation Scripts
🤖 Automation Scripts
This folder contains a collection of Python scripts designed to automate various utility and media processing tasks. Each script is intended to simplify repetitive processes, improve efficiency, and reduce manual effort.📝 OverviewThe scripts in this repository cover the following key areas:Media Conversion: Converting images to PDF and videos to audio files.File Management: Organizing files and resizing images in bulk.Scheduling: Setting and managing daily reminders.Data Acquisition: Web scraping movie information.

🚀 Getting Started
To use these scripts, you'll need the proper setup, as they rely on specific Python libraries.PrerequisitesPython: Ensure you have Python 3.x installed on your system.Required Libraries: The scripts require various external libraries. It is best practice to install them all from a single file.InstallationInstall Dependencies: Run the following command in your terminal within this folder to install all necessary packages:Bashpip install -r requirements.txt

Script Name,Description,Key Dependencies (Likely),How to Run
image2pdf.py,"Takes one or more image files (e.g., .jpg, .png) and combines them into a single PDF document.","Pillow, reportlab or similar" 

reminder.py,"Sets up a recurring daily reminder, often using system notifications or sending an email/message.","schedule, smtplib (for email)" (Must run continuously or as a scheduled task)
organising files.py,"Automatically sorts files in a specified directory into categorized folders (e.g., separating images, documents, and videos).","os, shutil" 
image resizer.py,Resizes a batch of images in a folder to a specified dimension or percentage.,Pillow (PIL) 
converter.py,"Extracts the audio track from a video file and saves it as an audio format (e.g., .mp3 or .wav).",moviepy or pydub
movie scraper.py,"Scrapes movie data (e.g., titles, ratings, summaries) from a website like IMDb or Rotten Tomatoes.","requests, BeautifulSoup4"

