class MetricsCalculator:

    @staticmethod
    def calculate(processes, current_time, busy_time):

        completed = [p for p in processes if p.remaining_time == 0]

        if not completed:
            return {
                "avg_waiting": 0,
                "avg_turnaround": 0,
                "avg_response": 0,
                "cpu_util": 0,
                "throughput": 0
            }

        avg_waiting = sum(p.waiting_time for p in completed) / len(completed)

        avg_turnaround = sum(
            p.turnaround_time for p in completed
        ) / len(completed)

        avg_response = sum(
            p.response_time for p in completed
        ) / len(completed)

        cpu_util = (busy_time / current_time) * 100 if current_time > 0 else 0

        throughput = len(completed) / current_time if current_time > 0 else 0

        return {
            "avg_waiting": round(avg_waiting, 2),
            "avg_turnaround": round(avg_turnaround, 2),
            "avg_response": round(avg_response, 2),
            "cpu_util": round(cpu_util, 2),
            "throughput": round(throughput, 2)
        }