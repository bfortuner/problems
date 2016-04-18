"""
Suppose you work at Lyft and there is a system that keeps track of how many drivers are on the road at any given time. 
The system has a server in each region that stores timestamps of when the current number of drivers change. 
Create a function to combine N number of these regional server logs into a single log file. Here is the server log format:

timestamp / current # of drivers on the road

Server Log 1 (New York)
1:00 5 
2:10 10
3:15 7
4:00 5
5:00 10

Server Log 2 (San Francisco)
1:05 3
3:15 20
4:30 6 
5:26 7

Combined Log (United States):
1:00 5
1:05 8
2:10 13
3:15 27
4:00 25
4:30 11
5:00 16
5:26 17

Cases:
1) Time in both servers. Combined log = sum
2) Time Server 1 < Time Server 2, Last entry in combined + Delta of Current Server 1 Log Entry + Prior Server 1 Log Entry
2) Time Server 1 > Time Server 2, Last entry in combined + Delta of Current Server 2 Log Entry + Prior Server 2 Log Entry
"""

def get_combined_log(log1, log2):
    combined_log = [[0,0]]
    a = 0
    b = 0
    last_a = 0
    last_b = 0
    while a < len(log1) or b < len(log2):
        if a < len(log1) and (b >= len(log2) or log1[a][0] < log2[b][0]):
            a_delta = log1[a][1] - last_a
            new_entry = [log1[a][0], a_delta + combined_log[-1][1]]
            last_a = log1[a][1]
            a += 1
        elif b < len(log2) and (a >= len(log1) or log2[b][0] < log1[a][0]):
            b_delta = log2[b][1] - last_b
            new_entry = [log2[b][0], b_delta + combined_log[-1][1]]
            last_b = log2[b][1]
            b += 1
        elif a < len(log1) and b < len(log2):
            new_entry = [log2[b][0], log2[b][1] + log1[a][1]]
            last_a = log1[a][1]
            last_b = log2[b][1]
            a += 1
            b += 1
        combined_log.append(new_entry)
    
    return combined_log[1:]





#Tests

assert get_combined_log([
    [100,5],
    [210,10],
    [315,7],
    [400,5],
    [500,10]
],[
    [105,3],
    [315,20],
    [430,6],
    [526,7]
]) == [[100, 5], [105, 8], [210, 13], [315, 27], [400, 25], [430, 11], [500, 16], [526, 17]]
