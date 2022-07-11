import os

from subprocess import check_output

audio_dir = "./audio"
audio_files = os.listdir(audio_dir)


def convert_wav(file):
    file_name = file.split(".")[0]

    # skips .DS_Store file
    if not file.endswith(".DS_Store"):
        # creates a .wav file
        check_output(f'ffmpeg -i ./audio/{file} ./audio_wav/{file_name}.wav', shell=True)
        # # creates a single channel .wav file
        # check_output(f'ffmpeg -i ./audio/{file} -ac 1 ./audio_wav/{file_name}.wav', shell=True)
        # creates a new file with a sample rate of 8000 khz
        check_output(f'sox ./audio_wav/{file_name}.wav -r 8000 ./transcoded_audio/{file_name}.8khz.wav', shell=True)


for i in range(0, len(audio_files)):
    convert_wav(audio_files[i])

print("Files transcribed!")
