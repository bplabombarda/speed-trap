from speed_trap.influx import write
from speed_trap.speedtest import run_speedtest


write(run_speedtest())
