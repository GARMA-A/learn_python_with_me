# ninput from the lecture problem (lec.4 slide 24)
import random as rd

iteration = 6

IAT = [rd.randint(1, 5) for _ in range(iteration)]  # Inter-Arrival Times
ST = [rd.randint(3, 7) for _ in range(iteration)]  # Service Times

arrival_time = []
service_start = []
service_end = []
waiting_time = []
queue_length = []

# For the first customer
arrival_time.append(IAT[0])
service_start.append(arrival_time[0])
service_end.append(service_start[0] + ST[0])
waiting_time.append(0)
queue_length.append(0)

# For the rest of the customers
for i in range(1, iteration):
    arrival_time.append(arrival_time[i - 1] + IAT[i])

    if arrival_time[i] >= service_end[i - 1]:
        service_start.append(arrival_time[i])
        waiting_time.append(0)
    else:
        service_start.append(service_end[i - 1])
        waiting_time.append(service_end[i - 1] - arrival_time[i])

    service_end.append(service_start[i] + ST[i])

    count = 0
    for j in range(i):
        if arrival_time[i] < service_end[j]:
            count += 1
    queue_length.append(count)

# Print table header
print(
    "{:<10}{:<5}{:<5}{:<12}{:<15}{:<15}{:<15}{:<10}".format(
        "Customer", "IAT", "ST", "Arrival", "Start", "End", "Waiting", "QueueLen"
    )
)

# Print each row of customer data
for i in range(iteration):
    print(
        "{:<10}{:<5}{:<5}{:<12}{:<15}{:<15}{:<15}{:<10}".format(
            i + 1,
            IAT[i],
            ST[i],
            arrival_time[i],
            service_start[i],
            service_end[i],
            waiting_time[i],
            queue_length[i],
        )
    )

# Summary statistics
total_waiting = sum(waiting_time)
average_waiting = total_waiting / len(waiting_time)
max_queue = max(queue_length)

print("\nAverage waiting time = {:.2f}".format(average_waiting))
print("Maximum queue length = {}".format(max_queue))
