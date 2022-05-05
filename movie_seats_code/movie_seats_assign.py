DIR = [
    (0, 1), 
    (0, 2), 
    (0, 3), 
    (1, 0), 
    (2, 0), 
    (3, 0), 
    (-1, 0), 
    (-2, 0),
    (-3, 0),
    (1, 0),
    (2, 0),
    (3, 0)
    ]
class MovieSeatsSystem:
    def __init__(self, rows, cols):
        self.seats = [["."] * cols for _ in range(rows)]
        self.seats_record = {
            i: 20
            for i in range(rows)
        }
        self.total_available_seats = rows * cols
        self.rows = rows
        self.cols = cols
    
    def get_locations(self, members):
        if members > self.total_available_seats:
            return -1
        locations = []
        stack = [members]
        while stack:
            num = stack.pop()
            num = self.assign_seats(num, locations)
            if num > 0:
                num1 = num // 2
                num2 = num - num1
                stack.append(num1)
                stack.append(num2)
        return locations

    def assign_seats(self, num, locations):
        for i in range(self.rows - 1, -1, -1):
            if self.seats_record[i] >= num:
                for j in range(self.cols):
                    if num == 0:
                        break
                    if self.seats[i][j] == ".":
                        self.seats[i][j] = "R"
                        self.seats_record[i] -= 1
                        self.total_available_seats -= 1
                        num -= 1
                        locations.append((i, j))
        return num

    def create_buffer(self, locations):
        if locations == -1:
            return False
        for x, y in locations:
            for dx, dy in DIR:
                new_x, new_y = x + dx, y + dy
                if not self.is_valid(new_x, new_y):
                    continue
                if self.seats[new_x][new_y] == ".":
                    self.seats[new_x][new_y] = "R"
                    self.total_available_seats -= 1
                    self.seats_record[new_x] -= 1
        return True
    
    def is_valid(self, x, y):
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return True
        return False

    def write_file(self, path, total_locations):
        with open(path, 'a') as f:
            for request_id, locations in total_locations.items():
                if locations == -1:
                    f.write(request_id + " " + "Can not reserve, insufficient seats")
                    f.write("\n")
                else:
                    formated_locations = self.format_locations(locations)
                    formated_locations = ','.join(formated_locations)
                    f.write(request_id + " " + formated_locations)
                    f.write("\n")
    
    def format_locations(self, locations):
        formated_locations = []
        for i, j in locations:
            row = chr(ord("A") + i - 0)
            location = str(row) + str(j)
            formated_locations.append(location)
        return formated_locations

if __name__ == '__main__':
    try:
        rows = 10
        cols = 20
        MV = MovieSeatsSystem(10, 20)
        input_file_name = 'test1.txt'
        input_path = 'input/' + input_file_name
        with open(input_path) as f:
            total_locations = {}
            for line in f:
                request_id, num = line.split(" ")
                locations = MV.get_locations(int(num))
                if locations == -1:
                    total_locations[request_id] = -1
                else:
                    total_locations[request_id] = locations
                    MV.create_buffer(locations)
        output_file_name = 'results_' + input_file_name
        output_path = 'output/' + output_file_name
        MV.write_file(output_path, total_locations)
    except:
        "The system can not work!"
