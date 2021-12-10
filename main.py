# This is a sample Python script.
import subprocess


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def exercise1():
    v = ["BBB_160x120p.mp4", "BBB_360x240p.mp4", "BBB_480p.mp4", "BBB_720p.mp4"]
    for video in v:
        video_name = video.removesuffix('.mp4')

        # Conversion to VP8
        command_vp8 = ["ffmpeg", "-i", video, "-c:v", "libvpx", "-b:v", "1M", "-c:a", "libvorbis",
                       "vp8" + video_name + ".webm"]
        subprocess.call(command_vp8)

        # Conversion to VP9
        command_vp9 = ["ffmpeg", "-i", video, "-c:v", "libvpx-vp9", "-b:v", "2M", "vp9" + video_name + ".webm"]
        subprocess.call(command_vp9)

        # Conversion to h265

        command_h265 = ['ffmpeg', "-i", video, "-c:v", "libx265", "-crf", "26", "-preset", "fast", "-c:a", "aac",
                        "-b:a", "128k", "h265" + video_name + ".mp4"]
        subprocess.call(command_h265)

        # Conversion to AV1

        command_av1 = ["ffmpeg", "-i", video, "-c:v", "libaom-av1", "-cpu-used", "3", "-crf", "40", "-preset",
                       "medium", "-c:a", "copy", "av1" + video_name + ".mkv"]
        subprocess.call(command_av1)


def exercise2():
    v1 = "vp8BBB_360x240p.webm"
    v2 = "vp9BBB_360x240p.webm"

    # Video comparison

    command = ["ffmpeg", "-i", v1, "-i", v2, "-filter_complex",
               "hstack=inputs=2", "comparison.webm"]
    subprocess.call(command)


def exercise3():
    v = "BBB_cut.mp4"
    ip = "udp://127.0.0.1:1111"

    # Live streaming

    command = ["ffmpeg", "-re", "-i", v, "-v", "0", "-c:v", "copy", "-f", "mpegts", ip]
    subprocess.call(command)


def exercise4():
    v = "BBB_cut.mp4"
    ip = input("Choose an ip for broadcasting the BBB video.\nExample, udp://127.0.0.1:1343 \n")

    # Live streaming

    command = ["ffmpeg", "-re", "-i", v, "-v", "0", "-c:v", "copy", "-f", "mpegts", ip]
    subprocess.call(command)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = int(input("Please, select the exercise you want"
                    "\n\n\t 1 -VP8, VP9, h265 and AV1 conversion"
                    "\n\n\t 2 -VP8 vs VP9 comparison"
                    "\n\n\t 3 -Live streaming"
                    "\n\n\t 4 -Choosing IP to live streaming  \n\n\t"))

    if opt == 1:
        exercise1()
    elif opt == 2:
        exercise2()
    elif opt == 3:
        exercise3()
    elif opt == 4:
        exercise4()

    else:
        print("Please, choose a correct number")

# See PyCharm help at https://www.jetbrains.com/help/pyºcharm/
