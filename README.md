# Transcoder

This application transcodes audio files to an 8khz `.wav` file. Note: you will need to have the [SoX](https://formulae.brew.sh/formula/sox) and [FFmpeg](https://formulae.brew.sh/formula/ffmpeg) packages installed on your machine to use this app.

Add the file or files you would like to transcode to the `/audio` directory and then run the `script.py` file. The original files will remain unchanged but a `.wav` version of each file will be created in the `/audio_wav` directory and an 8khz version of each file will be created in the `/trancoded_audio` directory.

