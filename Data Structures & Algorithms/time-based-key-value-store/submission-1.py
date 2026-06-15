class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if self.timeMap[key]:
            value_p = None
            for time, value in sorted(self.timeMap[key]):
                if time == timestamp:
                    return value
                if time < timestamp:
                    value_p = value
            return value_p if value_p else ""
        else:
            return ""