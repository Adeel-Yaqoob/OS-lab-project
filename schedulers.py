from collections import deque


class Scheduler:

    def fcfs(self, ready):
        return ready[0] if ready else None

    def sjf(self, ready):
        if not ready:
            return None

        return min(ready, key=lambda x: x.remaining_time)

    def priority_non_preemptive(self, ready):
        if not ready:
            return None

        return min(ready, key=lambda x: x.priority)

    def priority_preemptive(self, ready):
        if not ready:
            return None

        return min(ready, key=lambda x: x.priority)

    def round_robin(self, ready):
        return ready[0] if ready else None

    def mlfq(self, queues):
        for q in queues:
            if q:
                return q[0]
        return None