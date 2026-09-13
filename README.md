# host-status-checker

A tiny, dependency-light CLI that checks whether a list of file-host domains is reachable, and prints status + latency. Handy for spotting a host that's down before you waste time on it.

## Usage
```bash
python3 check_hosts.py            # uses the built-in list
python3 check_hosts.py hosts.txt  # one domain per line
```

Example output:
```
rapidgator.net        UP    212 ms
k2s.cc                UP    198 ms
nitroflare.com        DOWN  timeout
```

## How it works
For each domain it does an HTTPS `HEAD` (falls back to `GET`) with a short timeout and reports the status code + round-trip time. No third-party deps — standard library only.

## License
MIT
