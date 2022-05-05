# Movie-Theater-Seating
Design an algorithm to complete the task of assigning seats

## Introduction
Implement an algorithm for assigning seats within a movie theater.
This algorithm should maximize both customer satisfaction and customer safety.

## Assumption
1. If the total available seats less than the group size, it will print insufficient seats in the output file.
2. The highest priority of customer satisfication need to ensure all group members sit in the same row.
3. If we can not find a row to assign all group members, we will divide the group by 2 until all people have been assigned a seat.
4. Customers who reserves the seat first are offered better seats(seats that are far from the screen and seats that are in the middle) than the customers who are reserve later.

## Algorithm
total_available_seats: Count all available seats
seats:
[
    ["e", "e", "e", ...],
    ["e", "e", "e", ...],
    ["e", "e", "e", ...],
    ..,
    ..,
    ..
]
seats_record = {
    0: [[10, 10], [10, 11]]
}
(key: "row", value: [["left available seats", left_start_idx], "right available seats", right_start_idx])
