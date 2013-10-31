import create, time

r = create.Create(3)  # create robot

assignment = 0

while True:
    sensors = r.sensors()
    assignment = 1 if sensors[create.LEFT_BUMP] else 2 if sensors[create.RIGHT_BUMP] else 0
    if assignment != 0:
        break

if assignment == 1:  # assignment 1
    while True:
        sensors = r.sensors()
        if sensors[create.PLAY_BUTTON]:
            break

        lb, rb = sensors[create.LEFT_BUMP], sensors[create.RIGHT_BUMP]

        if lb and rb:
            r.turn(180, 90)
        elif lb:
            r.turn(90, 90)
        elif rb:
            r.turn(-90, 90)
        else:
            r.go(50, 0)
elif assignment == 2:  # assignment 2s
    while True:
        sensors = r.sensors()
        lb, rb = sensors[create.LEFT_BUMP], sensors[create.RIGHT_BUMP]
        contact, distance = sensors[create.WALL_IR_SENSOR], sensors[create.WALL_SIGNAL]

        threshold = 50
        difference = 10
        r.go(5, -5 if (distance - threshold) < difference else
            5 if (distance - threshold) > difference else 0)

        time.sleep(0.1)
        if lb and rb:
            break

r.stop()

r.close() # close connection