import heapq

def solution(jobs):
    current_time = 0
    jobs.sort() # 작업이 요청된 순서대로 정렬
    total_time = 0 # 작업이 끝날 때까지의 총 시간
    completed_jobs = 0
    job_queue = [] # 작업 대기열
    job_index = 0
    num_jobs = len(jobs) # 전체 작업 수
    
    while completed_jobs < num_jobs:
        # 현재 시간까지 요청된 모든 작업을 대기열에 추가
        for i in range(job_index, num_jobs):
            if jobs[i][0] <= current_time:
                heapq.heappush(job_queue, (jobs[i][1], jobs[i][0]))
                job_index += 1
            else:
                break
        
        # 대기열에 작업이 있으면 처리
        if job_queue:
            job_duration, job_start = heapq.heappop(job_queue)
            current_time += job_duration
            total_time += current_time - job_start
            completed_jobs += 1
        else:
            # 대기열에 작업이 없으면 다음 작업의 요청 시점으로 이동
            current_time = jobs[job_index][0]

    return total_time // num_jobs
