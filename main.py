import sys
from urllib.request import Request, urlopen

if len(sys.argv) < 2:
    print("Usage: %s [Auth Token] [Artist Id]" % sys.argv[0])
    exit(0)

request = Request("https://spclient.wg.spotify.com/artist/v1/%s/desktop?format=json&catalogue=premium"
                  % sys.argv[2])
request.add_header("Authorization", "Bearer %s" % sys.argv[1])

print("\n" + urlopen(request).read().decode('utf-8'))
