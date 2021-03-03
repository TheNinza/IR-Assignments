"""
Assignment 2 - Introduction to Robotics (BCCS-9402)

By: Nikhil Gupta (2019BCS-036)

"""

import numpy as np
import math

def get_input():
    
    rotationX = int(input('\nEnter angle of rotation arround x-axis (in degrees): '))
    rotationX = math.pi/180*rotationX
    rotationY = int(input('Enter angle of rotation arround y-axis (in degrees): '))
    rotationY = math.pi/180*rotationY
    rotationZ = int(input('Enter angle of rotation arround z-axis (in degrees): '))
    rotationZ = math.pi/180*rotationZ

    translationX = int(input('Enter translation in x-axis: '))
    translationY = int(input('Enter translation in y-axis: '))
    translationZ = int(input('Enter translation in z-axis: '))

    initialFrame = ''
    while initialFrame != 'a' and initialFrame != 'b':
        initialFrame = input('Enter the frame in which the point is? (a/b): ').lower()
        if initialFrame != 'a' and initialFrame != 'b':
            print('Two frames are \'A\' or \'B\'')

    initialCoordinates = np.array(list(
        map(int, input('\nEnter coordinates of the point in the frame (x y z): ').split())))

    # returning initial coordinates and the transformation matrix
    return initialCoordinates, getTransformationMatrix(rotationX, rotationY, rotationZ, translationX, translationY, translationZ, initialFrame)


def getTransformationMatrix(rotationX, rotationY, rotationZ, translationX, translationY, translationZ, initialFrame):

    # rotation matrix for rotation about x-axis
    rMatX = np.array([[1, 0, 0],[0, math.cos(rotationX), -math.sin(rotationX)], [0, math.sin(rotationX), math.cos(rotationX)]])

    # rotation matrix for rotation about y-axis
    rMatY = np.array([[math.cos(rotationY), 0, math.sin(rotationY)],[0, 1, 0], [-math.sin(rotationY), 0, math.cos(rotationY)]])

    # rotation matrix for rotation about z-axis
    rMatZ = np.array([[math.cos(rotationZ), -math.sin(rotationZ), 0], [math.sin(rotationZ), math.cos(rotationZ), 0],[0, 0, 1]])

    # final rotation matrix is the matrix multiplication of all three rotation matrices
    rMat = rMatZ @ rMatY @ rMatX

    # inverse transformation matrix if point is known is frame 'A' we need 
    if initialFrame == 'a':
        # displacement matrix
        d = np.array([[translationX], [translationY], [translationZ]])
        temp = -rMat.T@d
        temp = np.vstack((temp, [1]))

        transformationMatrix = np.hstack(
            (np.vstack((rMat.T, np.array([0, 0, 0]))), temp))

        return transformationMatrix

    elif initialFrame == 'b':
        # displacement matrix
        d = np.array([[translationX], [translationY], [translationZ], [1]])

        transformationMatrix = np.hstack(
            (np.vstack((rMat, np.array([0, 0, 0]))), d))

        return transformationMatrix


def transform(initialCoordinates, transformationMatrix):

    initialCoordinates = np.hstack((initialCoordinates, 1))
    finalCoordinates = transformationMatrix@initialCoordinates

    return finalCoordinates[:3]


def printAnswer(finalCoordinates):


    print('\nPosition of the point in other frame is: ({}, {}, {})'.format(finalCoordinates[0], finalCoordinates[1], finalCoordinates[2]))


if __name__ == '__main__':
    initialCoordinates, transformationMatrix = get_input()
    finalCoordinates = transform(initialCoordinates, transformationMatrix)
    printAnswer(finalCoordinates)