import cv2
import cv2.aruco as aruco
import Calculation_Module

url = ' http://192.168.43.97:8080/'
tl1 = [0]
tl2 = [0]
tr1 = [0]
tr2 = [0]
br1 = [0]
br2 = [0]
bl1 = [0]
bl2 = [0]
imgOut = 0
x_sum = 0
y_sum = 0
x = 0
y = 0


def findArucoMarker(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
    return bboxs, ids


def augmentAruco(bbox, id, img, drawid=True):
    global tl1, tl2, tr1, tr2, br1, br2, bl1, bl2, imgOut, x_sum, y_sum, x, y
    tl1 = bbox[0][0][0]
    tl2 = bbox[0][0][1]
    tr1 = bbox[0][1][0]
    tr2 = bbox[0][1][1]
    br1 = bbox[0][2][0]
    br2 = bbox[0][2][1]
    bl1 = bbox[0][3][0]
    bl2 = bbox[0][3][1]

    idMark_X = tl1
    idMark_Y = tl2
    idMark = (int(idMark_X), int(idMark_Y - 30))

    x_sum = tl1 + tr1 + br1 + bl1
    y_sum = tl2 + tr2 + br2 + bl2

    x = tl1 + tr1
    y = tl2 + tr2

    imgOut = img
    if drawid:
        cv2.putText(imgOut, str(id), idMark, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
        cv2.putText(imgOut, f'ROBOT{id}', Calculation_Module.centerPoint, cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1)
    else:
        cv2.putText(imgOut, "Unidentified ID",
                    (int(Calculation_Module.x_centerPixel), int(Calculation_Module.y_centerPixel)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)
    return imgOut


def drawMark(mark=True):
    if mark:
        Calculation_Module.SingleWayPoint.calculateValue(calculate=True)
        cv2.putText(imgOut, str(Calculation_Module.distance_Des_Center), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 0, 0), 1)
        cv2.circle(imgOut, Calculation_Module.centerPoint, 1, (0, 255, 255), 4)
        cv2.circle(imgOut, Calculation_Module.midPoint, 1, (0, 255, 255), 4)
        cv2.circle(imgOut, Calculation_Module.destinationPoint, 10, (0, 255, 255), 4)
        cv2.line(imgOut, Calculation_Module.destinationPoint, (int(Calculation_Module.x_destination), 0), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.destinationPoint, (0, int(Calculation_Module.y_destination)), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.destinationPoint, (int(Calculation_Module.x_destination), 480), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.destinationPoint, (640, int(Calculation_Module.y_destination)), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.midPoint, Calculation_Module.centerPoint, (255, 0, 0), 2)
        cv2.line(imgOut, Calculation_Module.centerPoint, (int(Calculation_Module.x_centerPixel), 0), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.centerPoint, (0, int(Calculation_Module.y_centerPixel)), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.centerPoint, (int(Calculation_Module.x_centerPixel), 480), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.centerPoint, (640, int(Calculation_Module.y_centerPixel)), (255, 0, 0), 1)
        cv2.line(imgOut, Calculation_Module.destinationPoint, Calculation_Module.centerPoint, (255, 0, 0), )
    else:
        pass
