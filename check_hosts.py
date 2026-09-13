#!/usr/bin/env python3
"""Check reachability + latency of file-host domains. Stdlib only."""
import sys, time, http.client, socket

DEFAULT = [
    "rapidgator.net", "k2s.cc", "nitroflare.com", "fboom.me",
    "filesmonster.com", "fileaxa.com", "filejoker.net", "upstore.net",
    "mega.nz", "1fichier.com", "turbobit.net",
]

def check(host, timeout=6.0):
    t0 = time.time()
    try:
        conn = http.client.HTTPSConnection(host, timeout=timeout)
        try:
            conn.request("HEAD", "/")
            r = conn.getresponse()
            code = r.status
        except Exception:
            conn.request("GET", "/")
            code = conn.getresponse().status
        finally:
            conn.close()
        ms = int((time.time() - t0) * 1000)
        up = 200 <= code < 500  # 4xx still means the host is answering
        return up, f"{ms} ms" if up else f"HTTP {code}"
    except (socket.timeout, TimeoutError):
        return False, "timeout"
    except Exception as e:
        return False, type(e).__name__

def main(argv):
    hosts = DEFAULT
    if len(argv) > 1:
        with open(argv[1]) as f:
            hosts = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    width = max(len(h) for h in hosts) + 2
    for h in hosts:
        up, info = check(h)
        print(f"{h:<{width}} {'UP  ' if up else 'DOWN'}  {info}")

if __name__ == "__main__":
    main(sys.argv)
