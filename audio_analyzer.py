import sys
import librosa
import serial

def read_mp3(file_name):
    duration = librosa.get_duration(filename = file_name)
    current_time = 0
    sample_size = 0.5
    max = 0
    while current_time + sample_size < duration:
        waveform, sample_rate = librosa.load(path = file_name,
                                             offset = current_time,
                                             duration = sample_size)
        tuning = librosa.core.estimate_tuning(y = waveform,
                                              sr = sample_rate)
        if tuning > max:
            max = tuning
        scaled_tuning = ((tuning + 1) * 255) % 255

        serial_line_writer = serial.Serial('/dev/ttyACM0', 9600);

        serial_line_writer.write('.'.join(map(str, map(int, color_wheel(scaled_tuning)))))

        current_time = current_time + sample_size


def color_wheel(wheel_pos):
    if wheel_pos < 85:
        return [wheel_pos * 3, 255 - wheel_pos * 3, 0]
    elif wheel_pos < 170:
        wheel_pos = wheel_pos - 85
        return [255 - wheel_pos * 3, 0, wheel_pos * 3]
    else:
        wheel_pos = wheel_pos - 170
        return [0, wheel_pos * 3, 255 - wheel_pos * 3]
