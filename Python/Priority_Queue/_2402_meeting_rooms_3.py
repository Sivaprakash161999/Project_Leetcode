import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = [i for i in range(n)]
        used_rooms = [] # [end_time, room_idx]
        
        meetings.sort() # sort the meeting based on start time
        heapq.heapify(available_rooms)
        heapq.heapify(used_rooms) # sort the rooms based on free_from

        counter = [0] * (n) # keep track of number of meetings per room
        max_count, res = 0, 0 # track room idx with max count of meetings

        for meet_start, meet_end in meetings:

            # free up all the used rooms, which has a 
            # end time <= start time of the current meeting
            # and add them to the available rooms.
            while used_rooms and used_rooms[0][0] <= meet_start:
                room_idx = heapq.heappop(used_rooms)[1]
                heapq.heappush(available_rooms, room_idx)

            # if rooms available, pick the lowest available room
            if available_rooms:
                cur_room = heapq.heappop(available_rooms)
                # put that room in used_rooms with meet_end as end_time
                heapq.heappush(used_rooms, [meet_end, cur_room])
            # if rooms not available,
            # pick a room with least end time from the used room,
            # add the cur meeting duration to the end time of the picked room
            # and again add it to the used_rooms
            else:
                cur_end, cur_room = heapq.heappop(used_rooms)
                meet_duration = meet_end - meet_start
                new_end = cur_end + meet_duration
                heapq.heappush(used_rooms, [new_end, cur_room])

            # update the no. of meeting for the cur_room and 
            # update the result as well
            counter[cur_room] += 1
            if counter[cur_room] > max_count:
                max_count = counter[cur_room]
                res = cur_room
            elif counter[cur_room] == max_count:
                res = min(res, cur_room)
        
        return res



