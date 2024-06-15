from db import Region
import json


class RegionStats:
    def run(self):
        regions = [region for region in list(Region.aggregate_stats())]
        print(json.dumps({ "regions": regions }, indent=4))

if __name__ == "__main__":
    RegionStats().run()