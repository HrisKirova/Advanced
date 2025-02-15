job_cycles = [int(x) for x in input().split(', ')]
index_of_job = int(input())
target_job = job_cycles[index_of_job]
sum_cycles = 0
while target_job in job_cycles:
    for current_job in job_cycles:
        min_job = min(job_cycles)
        if current_job > min_job:
            continue
        if current_job == min_job and current_job != target_job:
            sum_cycles += current_job
            job_cycles.remove(current_job)
        elif current_job == target_job:
            sum_cycles += current_job
            job_cycles.remove(current_job)
            break
        break



print(sum_cycles)