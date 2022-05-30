import Aruco_Detection_Module
import math

x_sum_half = 0
y_sum_half = 0
x_centerPixel = 0
y_centerPixel = 0
x_destination = 0
y_destination = 0
centerPoint = 0
midPoint = 0
destinationPoint = 0
distance_Des_Center = 0
QuadValueP1 = 0
QuadValueP2 = 0


class SingleWayPoint:
    @staticmethod
    def calculateValue(calculate=False):
        global x_centerPixel, y_centerPixel, centerPoint, x_sum_half, y_sum_half, midPoint, x_destination, y_destination, destinationPoint, distance_Des_Center
        if calculate:
            x_sum = Aruco_Detection_Module.x_sum
            y_sum = Aruco_Detection_Module.y_sum
            x = Aruco_Detection_Module.x
            y = Aruco_Detection_Module.y
            x_centerPixel = x_sum * 0.25
            y_centerPixel = y_sum * 0.25
            centerPoint = (int(x_centerPixel), int(y_centerPixel))
            x_sum_half = x * 0.5
            y_sum_half = y * 0.5
            midPoint = (int(x_sum_half), int(y_sum_half))
            x_destination = 320
            y_destination = 240
            destinationPoint = int(x_destination), int(y_destination)
            y_diff = (y_destination - y_sum_half) * (y_destination - y_sum_half)
            x_diff = (x_destination - x_sum_half) * (x_destination - x_sum_half)
            distance_Des_Center = int(math.sqrt(abs(y_diff + x_diff)))
        else:
            print('First Assign values then Calculate')

    @staticmethod
    def QuadrantsAssignPt1(pointX1=0, pointY1=0):
        global QuadValueP1
        if int(pointX1) > x_destination:
            if int(pointY1) < y_destination:
                QuadValueP1 = 1
            elif int(pointY1) > y_destination:
                QuadValueP1 = 4
            else:
                print('[ERROR] No Data to show')
        elif int(pointX1) < x_destination:
            if int(pointY1) < y_destination:
                QuadValueP1 = 2
            elif int(pointY1) > y_destination:
                QuadValueP1 = 3
            else:
                print('[ERROR] No Data to show')
        else:
            print('[ERROR] No Data to show')

    @staticmethod
    def QuadrantsAssignPt2(pointX2=0, pointY2=0):
        global QuadValueP2
        if int(pointX2) > x_centerPixel:
            if int(pointY2) < y_centerPixel:
                QuadValueP2 = 1
            elif int(pointY2) > y_centerPixel:
                QuadValueP2 = 4
            else:
                print('[ERROR] No Data to show')
        elif int(pointX2) < x_centerPixel:
            if int(pointY2) < y_centerPixel:
                QuadValueP2 = 2
            elif int(pointY2) > y_centerPixel:
                QuadValueP2 = 3
            else:
                print('[ERROR] No Data to show')
        else:
            print('[ERROR] No Data to show')
