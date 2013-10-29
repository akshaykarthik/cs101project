import create

r = create.Create(3)  # create robot
sensors = r.sensors()  # init sensors, poll

# part 1: move in 1 meter square
for i in xrange(4):
    r.move(100, 100)
    r.turn(90, 90)

# part 2: move until it hits wall
while not (sensors[create.LEFT_BUMP] or sensors[create.RIGHT_BUMP]):
    sensors = r.sensors()
    r.go(1000, 0)
r.stop()

r.close() # close connection