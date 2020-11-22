# speed-trap

Reports results from the [speedtest-cli](https://pypi.org/project/speedtest-cli/) to an InfluxDB bucket.

## Run

The below environment variables are required to run and can be found in the Influx dashboard:

```sh
INFLUX_BUCKET
INFLUX_ORG
INFLUX_TOKEN
INFLUX_URL
```

Then execute `run.py`:

``` sh
poetry run python run.py
```

or

``` sh
python run.py
```
