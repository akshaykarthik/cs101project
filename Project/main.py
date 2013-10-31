from Map import Map, Location
import sys
import create

if __name__ == "__main__":
        #r = create.Create(3)


        cmap = Map()
        cmap.load_map("campus.rmap")
        current_location = -1
        locations = cmap.get_key_locations()

        position = (2, 3)
        cmap.set_position(position)


        while True:
           #if position == locations[current_location].position:
                # text to speech
                # talk locations[current_location].voice
                # current_location += 1


            end_position = (1,1)


            for val in range(len(cmap.map)):
                for val2 in range(len(cmap.map[val])):
                    if (val, val2) == position:
                        sys.stdout.write("X")
                    elif (val, val2) == end_position:
                        sys.stdout.write("@")
                    else:
                        sys.stdout.write("0" if cmap.map[val][val2] == 1 else "~")

                print
            if cmap.position == end_position:
                break

            path = cmap.path_to(end_position)
            if path != 'not found':
                print "cur {:<8} | next {:<8} | path {}".format(position, path[1], path)
                cmap.set_position(path[1])
                position = path[1]
            else:
                break


