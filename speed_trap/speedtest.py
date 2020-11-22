import speedtest

servers = []
threads = None

s = speedtest.Speedtest()
s.get_servers(servers)


def run_speedtest():
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    return {
        "down": results_dict["download"],
        "ping": results_dict["ping"],
        "up": results_dict["upload"],
    }
