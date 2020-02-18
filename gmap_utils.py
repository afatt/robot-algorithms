import yaml
import math

def get_corners():
    '''
    '''
    with open('corners.yaml') as stream:
        corners = yaml.load(stream)

    x_corners = []
    y_corners = []
    for corner in corners:
        x_corners.append(corner.get('position')['x'])
        y_corners.append(corner.get('position')['y'])

    return(x_corners, y_corners)

def create_x_axis(x_corners, scan_rad):
    '''
    '''
    x_coord1 = x_corners[0]
    x_coord2 = x_corners[1]

    x_point = 0.0
    x_II_III = []
    while x_point >= x_coord1:
        x_II_III.append(x_point)
        x_point -= scan_rad
    x_II_III.reverse()

    x_point = 0.0
    x_I_IV = []
    while x_point <= x_coord2:
        x_I_IV.append(x_point)
        x_point += scan_rad

    # Remove any redundant x_points between x_I_IV and x_II_III
    # Append x_I_IV to x_II_III
    x_I_IV = [x for x in x_I_IV if x not in x_II_III]
    x_II_III.extend(x_I_IV)

    return(x_II_III)

def create_y_axis(y_corners, scan_rad):
    '''
    '''
    y_coord1 = y_corners[0]
    y_coord4 = y_corners[3]

    y_point = 0.0
    y_III_IV = []
    while y_point >= y_coord1:
        y_III_IV.append(y_point)
        y_point -= scan_rad
    y_III_IV.reverse()

    y_point = 0.0
    y_I_II = []
    while y_point <= y_coord4:
        y_I_II.append(y_point)
        y_point += scan_rad

    # Remove any redundant y_points between y_I_II and y_III_IV
    # Append y_I_II to y_III_IV
    y_I_II = [y for y in y_I_II if y not in y_III_IV]
    y_III_IV.extend(y_I_II)

    return(y_III_IV)

def create_grid(x_axis, y_axis):
    '''
    '''
    values = {'r1': 0.0,'r2': 0.0,'r3': 1.0}
    route_struct = {'name': '',
                    'position': {'x': 0.0, 'y': 0.0},
                    'orientation': values}
    grid = [(x,y) for x in x_axis for y in y_axis]
    print(grid)
    write_string = ''
    i = 1
    for x,y in grid:
        route_struct['name'] = 'coord' + str(i)
        route_struct['position']['x'] = x
        route_struct['position']['y'] = y
        write_string += '- ' + str(route_struct)+ '\r\n'
        i += 1

    f = open('xy_grid.yaml', 'w')
    f.write(write_string)
    f.close()

def main():
    x_corners, y_corners = get_corners()
    x_axis = create_x_axis(x_corners, 2.0)
    y_axis = create_y_axis(y_corners, 2.0)
    create_grid(x_axis, y_axis)


if __name__ == '__main__':
    main()
