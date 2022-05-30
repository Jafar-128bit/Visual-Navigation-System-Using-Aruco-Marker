import cv2
import os
import sys
import Network_module
import Aruco_Detection_Module
import Calculation_Module
import Move_Robot

distance_Des_Center = 0
robot1Address = 'http://192.168.1.254:5000/'
robot1AddressPing = 'www.google.com'
camAddress = 'www.google.com'
img = 0


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def networkPing(address, ping=False):
    if ping:
        if address == robot1AddressPing:
            Network_module.pingTest(url=robot1AddressPing)
            Avg_msR = str(Network_module.Avg_ms)
            Max_msR = str(Network_module.Max_ms)
            Min_msR = str(Network_module.Min_ms)
            cv2.rectangle(img, (460, 420), (625, 460), (255, 255, 255), thickness=-1, lineType=1)
            cv2.putText(img, Avg_msR, (470, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, Max_msR, (520, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, Min_msR, (560, 450), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, "AvgR", (470, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "MaxR", (520, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "MinR", (570, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "Network Strength in ms Robot", (450, 410), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 255),
                        1)
        if address == camAddress:
            Network_module.pingTest(url=camAddress)
            Avg_msC = str(Network_module.Avg_ms)
            Max_msC = str(Network_module.Max_ms)
            Min_msC = str(Network_module.Min_ms)
            cv2.rectangle(img, (460, 320), (625, 360), (255, 255, 255), thickness=-1, lineType=1)
            cv2.putText(img, Avg_msC, (470, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, Max_msC, (520, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, Min_msC, (560, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0), 1)
            cv2.putText(img, "AvgC", (470, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "MaxC", (520, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "MinC", (570, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            cv2.putText(img, "Network Strength in ms Camera", (440, 310), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 0, 255),
                        1)
    else:
        print("[ERROR] no ping from server")


def conditionCheck(Check=True):
    if Check:
        Calculation_Module.SingleWayPoint.calculateValue(calculate=True)
        Calculation_Module.SingleWayPoint.QuadrantsAssignPt1(pointX1=Calculation_Module.x_centerPixel,
                                                             pointY1=Calculation_Module.y_centerPixel)
        Calculation_Module.SingleWayPoint.QuadrantsAssignPt2(pointX2=Calculation_Module.x_sum_half,
                                                             pointY2=Calculation_Module.y_sum_half)
        if Calculation_Module.distance_Des_Center > 20:
            if Calculation_Module.QuadValueP1 == 1:
                if Calculation_Module.QuadValueP2 == 1:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 2:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 3:
                    Move_Robot.motion.forwardMotion(url=robot1Address)
                else:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
            elif Calculation_Module.QuadValueP1 == 2:
                if Calculation_Module.QuadValueP2 == 1:
                    Move_Robot.motion.RightMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 2:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 3:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
                else:
                    Move_Robot.motion.forwardMotion(url=robot1Address)
            elif Calculation_Module.QuadValueP1 == 3:
                if Calculation_Module.QuadValueP2 == 1:
                    Move_Robot.motion.forwardMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 2:
                    Move_Robot.motion.RightMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 3:
                    Move_Robot.motion.RightMotion(url=robot1Address)
                else:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
            elif Calculation_Module.QuadValueP1 == 4:
                if Calculation_Module.QuadValueP2 == 1:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 2:
                    Move_Robot.motion.forwardMotion(url=robot1Address)
                elif Calculation_Module.QuadValueP2 == 3:
                    Move_Robot.motion.RightMotion(url=robot1Address)
                else:
                    Move_Robot.motion.LeftMotion(url=robot1Address)
            else:
                print('[ERROR] No data to send')
        else:
            Move_Robot.motion.Stop(url=robot1Address)
    else:
        print('[ERROR] enable the check value')


def nothing():
    pass


def main():
    global img
    cap = cv2.VideoCapture(0)

    while True:
        sccuess, img = cap.read()
        arucoFound = Aruco_Detection_Module.findArucoMarker(img)
        if len(arucoFound[0]) != 0:
            for bboxs, id in zip(arucoFound[0], arucoFound[1]):
                if id == 6:
                    Aruco_Detection_Module.drawMark(mark=True)
                    cv2.putText(img, "Robot Identify", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
                    img = Aruco_Detection_Module.augmentAruco(bboxs, id, img, drawid=True)
                    Aruco_Detection_Module.drawMark(mark=True)
                    networkPing(address=robot1AddressPing, ping=False)
                    networkPing(address=camAddress, ping=False)
                    conditionCheck(Check=True)
                else:
                    img = Aruco_Detection_Module.augmentAruco(bboxs, id, img, drawid=False)
                    Aruco_Detection_Module.drawMark(mark=False)
                    conditionCheck(Check=False)
                    Aruco_Detection_Module.drawMark(mark=False)
        else:
            Move_Robot.motion.Stop(url=robot1Address)
            cv2.putText(img, "No Marker present, Searching for Markers", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 1)
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            Network_module.moveRobot(order=5, address=robot1Address)
            Network_module.moveRobot(order=5, address=robot1Address)
            Network_module.moveRobot(order=5, address=robot1Address)
            restart_program()


if __name__ == "__main__":
    main()
