from dataclasses import dataclass, field


@dataclass
class Process:
    pid: str
    arrival_time: int
    burst_time: int
    priority: int

    remaining_time: int = field(init=False)
    completion_time: int = 0
    turnaround_time: int = 0
    waiting_time: int = 0
    response_time: int = -1
    start_time: int = -1

    state: str = "Ready"

    queue_level: int = 0

    def __post_init__(self):
        self.remaining_time = self.burst_time