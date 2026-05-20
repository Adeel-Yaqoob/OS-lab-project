import threading
import time

from analytics import MetricsCalculator
from adaptive_engine import AdaptiveEngine
from schedulers import Scheduler


class SimulationEngine:

    def __init__(self, app):

        self.app = app

        self.processes = []

        self.ready_queue = []

        self.completed = []

        self.current_time = 0

        self.running = False

        self.paused = False

        self.algorithm = "FCFS"

        self.scheduler = Scheduler()

        self.quantum = 3

        self.busy_time = 0

        self.analysis_engine = AdaptiveEngine()

        self.current_process = None

    def add_process(self, process):
        self.processes.append(process)

    def reset(self):

        self.processes.clear()

        self.ready_queue.clear()

        self.completed.clear()

        self.current_time = 0

        self.busy_time = 0

        self.running = False

        self.app.clear_tables()

    def start(self):

        self.running = True

        threading.Thread(target=self.run).start()

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def switch_algorithm(self, algo):
        self.algorithm = algo

    def run(self):

        rr_counter = 0

        while self.running:

            if self.paused:
                time.sleep(0.1)
                continue

            for p in self.processes:
                if (
                    p.arrival_time <= self.current_time
                    and p.remaining_time > 0
                    and p not in self.ready_queue
                    and p not in self.completed
                ):
                    self.ready_queue.append(p)

            if self.algorithm == "FCFS":
                process = self.scheduler.fcfs(self.ready_queue)

            elif self.algorithm == "SJF":
                process = self.scheduler.sjf(self.ready_queue)

            elif self.algorithm == "Priority":
                process = self.scheduler.priority_preemptive(
                    self.ready_queue
                )

            elif self.algorithm == "RR":
                process = self.scheduler.round_robin(
                    self.ready_queue
                )

            else:
                process = self.scheduler.fcfs(self.ready_queue)

            if process:

                self.current_process = process

                if process.start_time == -1:
                    process.start_time = self.current_time
                    process.response_time = (
                        self.current_time - process.arrival_time
                    )

                process.state = "Running"

                process.remaining_time -= 1

                self.busy_time += 1

                self.app.gantt.draw(
                    process.pid,
                    self.current_time
                )

                if self.algorithm == "RR":
                    rr_counter += 1

                if process.remaining_time == 0:

                    process.completion_time = self.current_time + 1

                    process.turnaround_time = (
                        process.completion_time -
                        process.arrival_time
                    )

                    process.waiting_time = (
                        process.turnaround_time -
                        process.burst_time
                    )

                    process.state = "Completed"

                    self.completed.append(process)

                    if process in self.ready_queue:
                        self.ready_queue.remove(process)

                    rr_counter = 0

                elif self.algorithm == "RR":

                    if rr_counter >= self.quantum:

                        self.ready_queue.remove(process)

                        self.ready_queue.append(process)

                        rr_counter = 0

            for p in self.ready_queue:
                if p != process:
                    p.waiting_time += 1

            metrics = MetricsCalculator.calculate(
                self.processes,
                self.current_time + 1,
                self.busy_time
            )

            self.app.update_metrics(metrics)

            self.app.update_ready_queue(self.ready_queue)

            self.app.update_completed(self.completed)

            analysis = self.analysis_engine.analyze(
                self.ready_queue,
                self.algorithm
            )

            self.app.update_analysis(analysis)

            self.current_time += 1

            time.sleep(1)