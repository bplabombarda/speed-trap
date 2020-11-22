import os
from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

INFLUX_BUCKET = os.environ.get("INFLUX_BUCKET")
INFLUX_ORG = os.environ.get("INFLUX_ORG")
INFLUX_TOKEN = os.environ.get("INFLUX_TOKEN")
INFLUX_URL = os.environ.get("INFLUX_URL")

client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN)

write_client = client.write_api(write_options=SYNCHRONOUS)


def write(data):
    data_point = Point("bytes_ps")

    for field in data:
        data_point.field(field, data[field])

    data_point.tag("host", "pi0")
    data_point.time(datetime.utcnow(), WritePrecision.NS)

    try:
        write_client.write(INFLUX_BUCKET, INFLUX_ORG, data_point)
    except Exception as err:
        print(err)
