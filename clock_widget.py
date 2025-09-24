#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime
import time

class ClockWidget:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simple Clock Widget")
        self.root.geometry("300x150")
        self.root.configure(bg='black')
        
        # Make window stay on top
        self.root.attributes('-topmost', True)
        
        # Create clock label
        self.clock_label = tk.Label(
            self.root,
            font=('Arial', 24, 'bold'),
            fg='white',
            bg='black',
            pady=20
        )
        self.clock_label.pack(expand=True)
        
        # Create date label
        self.date_label = tk.Label(
            self.root,
            font=('Arial', 12),
            fg='lightgray',
            bg='black'
        )
        self.date_label.pack()
        
        # Start the clock
        self.update_clock()
        
    def update_clock(self):
        """Update the clock display every second"""
        current_time = datetime.now()
        time_str = current_time.strftime("%H:%M:%S")
        date_str = current_time.strftime("%A, %B %d, %Y")
        
        self.clock_label.config(text=time_str)
        self.date_label.config(text=date_str)
        
        # Schedule next update
        self.root.after(1000, self.update_clock)
    
    def run(self):
        """Start the clock widget"""
        self.root.mainloop()

def main():
    clock = ClockWidget()
    clock.run()

if __name__ == "__main__":
    main()