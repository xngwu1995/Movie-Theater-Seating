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
total_available_seats: Count all available seats \
seats: \
[
    [".", ".", ".", ...],
    [".", ".", ".", ...],
    [".", ".", ".", ...],
    ..,
    ..,
    ..
] \
seats_record = {
    0: 20
} \
(key: "row", value: "available seats in this row") \

## Docker Image
docker pull xngwu1995/movie-seating:latest \n
docker container run -t -d --name movie-seating xngwu1995/movie-seating \
docker exec -it movie-seating bash \
cd app/movie_seats_code/ \
python3 movie_seats_assign.py
