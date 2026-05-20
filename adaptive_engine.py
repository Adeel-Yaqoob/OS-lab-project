class AdaptiveEngine:

    def analyze(self, processes, algorithm):

        if not processes:
            return "System Idle."

        avg_burst = sum(p.remaining_time for p in processes) / len(processes)

        high_wait = any(p.waiting_time > 10 for p in processes)

        short_jobs = len(
            [p for p in processes if p.remaining_time <= 4]
        )

        long_jobs = len(
            [p for p in processes if p.remaining_time > 10]
        )

        analysis = []

        if short_jobs > long_jobs:
            analysis.append(
                "Detected short interactive workload. "
                "SRTF or RR is recommended for responsiveness."
            )

        if long_jobs > short_jobs:
            analysis.append(
                "Detected CPU-bound workload. FCFS or Priority scheduling recommended."
            )

        if high_wait:
            analysis.append(
                "Potential starvation detected. "
                "Aging or MLFQ strongly recommended."
            )

        if algorithm == "FCFS" and short_jobs > 2:
            analysis.append(
                "FCFS may increase turnaround time for short tasks."
            )

        if algorithm == "RR":
            analysis.append(
                "Round Robin improves fairness and responsiveness."
            )

        return "\n".join(analysis)