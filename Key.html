import DistanceSensor

SAMPLE_RATE = 1.0  # sensor sampling rate in Hz


dist_sensors = [  # using maximum rated distance for HC-SR04
    DistanceSensor(echo=13, trigger=19, max_distance=4),
    DistanceSensor(echo=17, trigger=27, max_distance=4),
    DistanceSensor(echo=20, trigger=21, max_distance=4),
    DistanceSensor(echo=23, trigger=24, max_distance=4)
]


def show_dist_sensors():
    """Shows configuration of all distance sensors."""
    print("Distance sensors configured:")
    for index, sensor in enumerate(dist_sensors):
        print("%d: echo = %s, trigger = %s, max_distance = %.1f, threshold_distance = %.1f"
              % (index, sensor.echo, sensor.trigger, sensor.max_distance,
                 sensor.threshold_distance))
    print()

def read_dist_sensors():
    """Read all distance sensors."""
    for index, sensor in enumerate(dist_sensors):
        print("Distance sensor %d read %.1f cm."
              % (index, sensor.distance * 100))

show_dist_sensors()
previous_time = time()  # time in seconds
print("Press CTRL-C to exit.\n")
while True:
    current_time = time()  # time in seconds
    if current_time - previous_time >= 1.0/SAMPLE_RATE:
        read_dist_sensors()
        previous_time = current_time
