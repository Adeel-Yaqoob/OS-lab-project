import customtkinter as ctk
from tkinter import ttk

from models import Process
from simulation_engine import SimulationEngine
from gantt import GanttChart


ctk.set_appearance_mode("dark")


class CPUSchedulerGUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Real-Time CPU Scheduling Simulator")

        self.geometry("1500x900")

        self.engine = SimulationEngine(self)

        self.create_widgets()

    def create_widgets(self):

        control_frame = ctk.CTkFrame(self)
        control_frame.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(control_frame, text="PID").grid(
            row=0, column=0, padx=5
        )

        self.pid_entry = ctk.CTkEntry(control_frame)
        self.pid_entry.grid(row=0, column=1)

        ctk.CTkLabel(control_frame, text="Burst").grid(
            row=0, column=2
        )

        self.burst_entry = ctk.CTkEntry(control_frame)
        self.burst_entry.grid(row=0, column=3)

        ctk.CTkLabel(control_frame, text="Priority").grid(
            row=0, column=4
        )

        self.priority_entry = ctk.CTkEntry(control_frame)
        self.priority_entry.grid(row=0, column=5)

        add_btn = ctk.CTkButton(
            control_frame,
            text="Add Process",
            command=self.add_process
        )

        add_btn.grid(row=0, column=6, padx=10)

        self.algorithm_box = ctk.CTkComboBox(
            control_frame,
            values=[
                "FCFS",
                "SJF",
                "Priority",
                "RR"
            ],
            command=self.change_algorithm
        )

        self.algorithm_box.grid(row=0, column=7)

        self.algorithm_box.set("FCFS")

        ctk.CTkLabel(control_frame, text="Quantum").grid(
            row=0, column=8
        )

        self.quantum_entry = ctk.CTkEntry(
            control_frame,
            width=60
        )

        self.quantum_entry.insert(0, "3")

        self.quantum_entry.grid(row=0, column=9)

        start_btn = ctk.CTkButton(
            control_frame,
            text="Start",
            command=self.start_simulation
        )

        start_btn.grid(row=0, column=10, padx=5)

        pause_btn = ctk.CTkButton(
            control_frame,
            text="Pause",
            command=self.engine.pause
        )

        pause_btn.grid(row=0, column=11)

        resume_btn = ctk.CTkButton(
            control_frame,
            text="Resume",
            command=self.engine.resume
        )

        resume_btn.grid(row=0, column=12)

        reset_btn = ctk.CTkButton(
            control_frame,
            text="Reset",
            command=self.engine.reset
        )

        reset_btn.grid(row=0, column=13)

        # READY QUEUE TABLE

        self.ready_table = ttk.Treeview(
            self,
            columns=("PID", "Remaining", "Priority"),
            show="headings",
            height=8
        )

        for col in ("PID", "Remaining", "Priority"):
            self.ready_table.heading(col, text=col)

        self.ready_table.pack(fill="x", padx=10, pady=10)

        # COMPLETED TABLE

        self.completed_table = ttk.Treeview(
            self,
            columns=(
                "PID",
                "Waiting",
                "Turnaround",
                "Response"
            ),
            show="headings",
            height=8
        )

        for col in (
            "PID",
            "Waiting",
            "Turnaround",
            "Response"
        ):
            self.completed_table.heading(col, text=col)

        self.completed_table.pack(fill="x", padx=10)

        # METRICS

        metrics_frame = ctk.CTkFrame(self)
        metrics_frame.pack(fill="x", padx=10, pady=10)

        self.metrics_label = ctk.CTkLabel(
            metrics_frame,
            text="Metrics"
        )

        self.metrics_label.pack()

        # GANTT CHART

        gantt_frame = ctk.CTkFrame(self)
        gantt_frame.pack(fill="both", expand=True)

        self.canvas = ctk.CTkCanvas(
            gantt_frame,
            bg="white",
            height=150
        )

        self.canvas.pack(fill="x")

        self.gantt = GanttChart(self.canvas)

        # ANALYSIS TERMINAL

        analysis_frame = ctk.CTkFrame(self)
        analysis_frame.pack(fill="both", expand=True)

        self.analysis_box = ctk.CTkTextbox(
            analysis_frame,
            height=150
        )

        self.analysis_box.pack(fill="both", padx=10, pady=10)

    def add_process(self):

        pid = self.pid_entry.get()

        burst = int(self.burst_entry.get())

        priority = int(self.priority_entry.get())

        p = Process(
            pid=pid,
            arrival_time=self.engine.current_time,
            burst_time=burst,
            priority=priority
        )

        self.engine.add_process(p)

    def start_simulation(self):

        self.engine.quantum = int(
            self.quantum_entry.get()
        )

        self.engine.start()

    def change_algorithm(self, value):

        self.engine.switch_algorithm(value)

    def update_ready_queue(self, queue):

        for row in self.ready_table.get_children():
            self.ready_table.delete(row)

        for p in queue:
            self.ready_table.insert(
                "",
                "end",
                values=(
                    p.pid,
                    p.remaining_time,
                    p.priority
                )
            )

    def update_completed(self, completed):

        for row in self.completed_table.get_children():
            self.completed_table.delete(row)

        for p in completed:
            self.completed_table.insert(
                "",
                "end",
                values=(
                    p.pid,
                    p.waiting_time,
                    p.turnaround_time,
                    p.response_time
                )
            )

    def update_metrics(self, metrics):

        text = (
            f"Average Waiting Time: "
            f"{metrics['avg_waiting']} | "
            f"Average Turnaround Time: "
            f"{metrics['avg_turnaround']} | "
            f"Average Response Time: "
            f"{metrics['avg_response']} | "
            f"CPU Utilization: "
            f"{metrics['cpu_util']}% | "
            f"Throughput: "
            f"{metrics['throughput']}"
        )

        self.metrics_label.configure(text=text)

    def update_analysis(self, text):

        self.analysis_box.delete("1.0", "end")

        self.analysis_box.insert("end", text)

    def clear_tables(self):

        for row in self.ready_table.get_children():
            self.ready_table.delete(row)

        for row in self.completed_table.get_children():
            self.completed_table.delete(row)

        self.canvas.delete("all")


if __name__ == "__main__":

    app = CPUSchedulerGUI()

    app.mainloop()