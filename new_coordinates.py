'''
Submitted By:
Name: Raunak Kumar
Roll No: 2019BCS-045
'''
import numpy as np
import math


def fetch_input():

    rotation_x = int(input('\nEnter rotation angle about x-axis (in degrees): '))
    rotation_x = math.pi/180*rotation_x                             #converting angle in degress to radians
    rotation_y = int(input('Enter rotation angle about y-axis (in degrees): '))
    rotation_y = math.pi/180*rotation_y                             #converting angle in degress to radians
    rotation_z = int(input('Enter rotation angle about z-axis (in degrees): '))
    rotation_z = math.pi/180*rotation_z                             #converting angle in degress to radians

    translation_x = int(input('Enter translation about x-axis: '))
    translation_y = int(input('Enter translation about y-axis: '))
    translation_z = int(input('Enter translation about z-axis: '))

    initial_frame = ''
    while initial_frame != 'a' and initial_frame != 'b':
        initial_frame = input('Point is known in frame? (A/B): ').lower()
        if initial_frame != 'a' and initial_frame != 'b':
            print('Two frames are \'A\' or \'B\'')

    initial_coordinates = np.array(list(
        map(int, input('\nEnter coordinates of the point in the initial frame: ').split())))

    # return coordinates given by user and transformation matrix for given transformations
    return initial_coordinates, calculate_transformation_matrix(rotation_x, rotation_y, rotation_z, translation_x, translation_y, translation_z, initial_frame)


def calculate_transformation_matrix(rotation_x, rotation_y, rotation_z, translation_x, translation_y, translation_z, initial_frame):
    
    rx = np.array([[1, 0, 0],
                   [0, math.cos(rotation_x), -math.sin(rotation_x)],
                   [0, math.sin(rotation_x), math.cos(rotation_x)]])

    ry = np.array([[math.cos(rotation_y), 0, math.sin(rotation_y)],
                   [0, 1, 0],
                   [-math.sin(rotation_y), 0, math.cos(rotation_y)]])

    rz = np.array([[math.cos(rotation_z), -math.sin(rotation_z), 0],
                   [math.sin(rotation_z), math.cos(rotation_z), 0],
                   [0, 0, 1]])

    
    r = rz @ ry @ rx        # calculating final rotation matrix by multiplying individual rotations around each axes

    if initial_frame == 'a':
        d = np.array([[translation_x], [translation_y], [translation_z]])
        temp = -r.T@d
        temp = np.vstack((temp, [1]))

        transformation_matrix = np.hstack(
            (np.vstack((r.T, np.array([0, 0, 0]))), temp))

        return transformation_matrix

    elif initial_frame == 'b':
        d = np.array([[translation_x], [translation_y], [translation_z], [1]])

        transformation_matrix = np.hstack(
            (np.vstack((r, np.array([0, 0, 0]))), d))

        return transformation_matrix


def transform(initial_coordinates, transformation_matrix):

    initial_coordinates = np.hstack((initial_coordinates, 1))
    final_coordinates = transformation_matrix@initial_coordinates
    return final_coordinates[:3]


def print_transformed_coordinates(final_coordinates):

    print('\nCoordinates of the point in new frame is: ({}, {}, {})'.format(
          final_coordinates[0], final_coordinates[1], final_coordinates[2]))


if __name__ == '__main__':
    initial_coordinates, transformation_matrix = fetch_input()
    final_coordinates = transform(initial_coordinates, transformation_matrix)
    print_transformed_coordinates(final_coordinates)