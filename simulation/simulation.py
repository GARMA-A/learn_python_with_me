"""
Single server queue simulation
"""

import random as rd
from collections import deque

# Number of iterations (customers)
iterations = 7

# Inter-arrival times (0 for first customer)
inter_arrival_time = [0] + [rd.randint(1, 5) for _ in range(iterations - 1)]
# Service times
service_time = [rd.randint(3, 7) for _ in range(iterations)]

# Arrival times as is the sum of inter-arrival times
arrival_time = [0] * iterations
total = 0
for i in range(1, iterations):
    total += inter_arrival_time[i]
    arrival_time[i] = total

# Initialize tracking lists
service_start_times = [0] * iterations
service_end_times = [0] * iterations
waiting_times = [0] * iterations
queue_lengths = [0] * iterations

queue = deque()

# First customer (index 0)
service_start_times[0] = arrival_time[0]
service_end_times[0] = service_start_times[0] + service_time[0]
waiting_times[0] = 0
queue.append(service_end_times[0])

# Output headers
print(
    "{:<10}{:<5}{:<5}{:<12}{:<15}{:<15}{:<15}{:<10}".format(
        "Customer", "IAT", "ST", "Arrival", "Start", "End", "Waiting", "QueueLen"
    )
)
# print first row
print(
    "{:<10}{:<5}{:<5}{:<12}{:<15}{:<15}{:<15}{:<10}".format(
        1,
        inter_arrival_time[0],
        service_time[0],
        arrival_time[0],
        service_start_times[0],
        service_end_times[0],
        waiting_times[0],
        0,
    )
)

# Loop for remaining customers
total_waiting_time = 0
max_queue_length = 0

for i in range(1, iterations):
    # Remove customers whose service ended before arrival
    while queue and arrival_time[i] > queue[0]:
        queue.popleft()

    # Service start depends on arrival vs. last end
    last_service_end = service_end_times[i - 1]
    if arrival_time[i] >= last_service_end:
        service_start = arrival_time[i]
    else:
        service_start = last_service_end

    service_end = service_start + service_time[i]
    waiting = service_start - arrival_time[i]

    # Track values
    service_start_times[i] = service_start
    service_end_times[i] = service_end
    waiting_times[i] = waiting
    queue.append(service_end)
    queue_lengths[i] = len(queue) - 1

    # Update stats
    total_waiting_time += waiting
    max_queue_length = max(max_queue_length, queue_lengths[i])

    # Print row
    print(
        "{:<10}{:<5}{:<5}{:<12}{:<15}{:<15}{:<15}{:<10}".format(
            i + 1,
            inter_arrival_time[i],
            service_time[i],
            arrival_time[i],
            service_start,
            service_end,
            waiting,
            queue_lengths[i],
        )
    )

# Final statistics
print("─" * 90)
print(
    f"Total waiting time: {total_waiting_time} | "
    f"Average waiting time: {round(total_waiting_time / iterations, 2)} | "
    f"Max queue length: {max_queue_length}"
)
