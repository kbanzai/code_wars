class Dinglemouse(object):
    def __init__(self, queues, capacity):
        self.queues = [list(queue) for queue in queues]
        self.capacity = capacity
        self.floor = 0
        self.direction = "up"
        self.lift = []
        print(self.queues)
        print(self.capacity)

    def is_empty(self):
        return sum(map(len, self.queues)) == 0

    @property
    def top_floor(self):
        return len(self.queues)-1

    def get_off(self):
        # print("get_off", self.floor, list(filter(lambda p: p == self.floor, self.lift)))
        self.lift = list(filter(lambda p: p != self.floor, self.lift))

    def get_on(self):
        if self.direction == "up":
            get_on_list = list(filter(lambda p: p > self.floor, self.queues[self.floor]))[:self.capacity-len(self.lift)]
        else:
            get_on_list = list(filter(lambda p: p < self.floor, self.queues[self.floor]))[:self.capacity-len(self.lift)]
        # print("get_on", self.floor, get_on_list)
        self.lift += get_on_list
        for p in get_on_list:
            self.queues[self.floor].pop(self.queues[self.floor].index(p))

    def up_pushed_floors(self, floor_range):
        '''
            return the list of floors whose up button is pushed
        '''
        return set(floor for floor, queue in enumerate(self.queues) if queue and max(queue) > floor) & set(floor_range)

    def down_pushed_floors(self, floor_range):
        '''
            return the list of floors whose down button is pushed
        '''
        return set(floor for floor, queue in enumerate(self.queues) if queue and min(queue) < floor) & set(floor_range)

    @property
    def upward_floors(self):
        return range(self.floor+1, self.top_floor+1)

    @property
    def downward_floors(self):
        return range(0, self.floor)

    def move(self):
        '''
            move the lift
            return:
                True (if the lift moves), False (otherwise)
        '''
        current_floor = self.floor
        if self.lift:
            if self.direction == "up":
                next_get_on = min(self.up_pushed_floors(self.upward_floors), default=self.top_floor+1)
                next_get_off = min(self.lift)
                self.floor = min(next_get_on, next_get_off)
            else:
                next_get_on = max(self.down_pushed_floors(self.downward_floors), default=-1)
                next_get_off = max(self.lift)
                self.floor = max(next_get_on, next_get_off)
        elif not self.is_empty():
            if self.direction == "up":
                up = min(self.up_pushed_floors(self.upward_floors), default=self.top_floor+1)
                down = max(self.down_pushed_floors(range(self.floor, self.top_floor+1)), default=-1)
                if up <= self.top_floor:
                    self.floor = up
                elif down >= 0:
                    self.floor = down
                    self.direction = "down"
                else:
                    self.direction = "down"
                    return self.move()
            else:
                up = min(self.up_pushed_floors(range(0, self.floor+1)), default=self.top_floor+1)
                down = max(self.down_pushed_floors(self.downward_floors), default=-1)
                if down >= 0:
                    self.floor = down
                elif up <= self.top_floor:
                    self.floor = up
                    self.direction = "up"
                else:
                    self.direction = "up"
                    return self.move()
        else:
            self.floor = 0
        return self.floor != current_floor

    def theLift(self):
        floors = [self.floor]
        while not self.is_empty() or self.lift:
            self.get_off()
            self.get_on()
            if self.move():
                # print("move to", self.floor, self.queues, self.lift, self.direction)
                floors.append(self.floor)
        return floors

tests = [
    [ ( (),   (),    (5,5,5), (),   (),    (),    () ),     [0, 2, 5, 0]          ],
    [ ( (),   (),    (1,1),   (),   (),    (),    () ),     [0, 2, 1, 0]          ],
    [ ( (),   (3,),  (4,),    (),   (5,),  (),    () ),     [0, 1, 2, 3, 4, 5, 0] ],
    [ ( (),   (0,),  (),      (),   (2,),  (3,),  () ),     [0, 5, 4, 3, 2, 1, 0] ],
]

for queues, answer in tests:
    lift = Dinglemouse(queues, 5)
    result = lift.theLift()
    print(result)
    print(answer)
    print(result == answer)
    if result != answer:
        break