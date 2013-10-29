from Map import Map, Location

if __name__ == "__main__":
        map = Map()
        map.load_map("campus.rmap")
        current_location = -1
        locations = map.get_key_locations()

        position = (0, 0)
        map.set_position(position)

        while True:
           #if position == locations[current_location].position:
                # text to speech
                # talk locations[current_location].voice
                # current_location += 1

            end_position = (6,11)
            if map.position == end_position:
                break

            path = map.path_to(end_position)
            print "cur_pos " + str(position) + " || next_pos " +str(path[1]) + " || path" + str(path)
            map.set_position(path[1])
            position = path[1]


