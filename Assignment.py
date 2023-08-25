
class FlightTable:
    def __init__(self, data):
        self.data = data

    def sort_data(self, sort_by):
        if sort_by == 1:
            self.data.sort(key=lambda x: x[0])
        elif sort_by == 2:
            self.data.sort(key=lambda x: x[2])
        elif sort_by == 3:
            priority_order = {'High': 1, 'MID': 2, 'Low': 3}
            self.data.sort(key=lambda x: priority_order[x[3]])

    def print_data(self):
        print('P_ID\tProcess\tStart Time (ms)\tPriority')
        for row in self.data:
            print('\t'.join(map(str, row)))

data = [
    ('P1', 'VSCode', 100, 'MID'),
    ('P23', 'Eclipse', 234, 'MID'),
    ('P93', 'Chrome', 189, 'High'),
    ('P42', 'JDK', 9, 'High'),
    ('P9', 'CMD', 7, 'High'),
    ('P87', 'NotePad', 23, 'Low')
]

flight_table = FlightTable(data)
sort_by = int(input('Enter sorting parameter [1. P_ID, 2. Start Time, 3. Priority]: '))
flight_table.sort_data(sort_by)
flight_table.print_data()
