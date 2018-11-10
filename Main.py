import cv2
import time

map_bg = cv2.imread('map.png')
map_bg = cv2.cvtColor(map_bg, cv2.COLOR_BGR2GRAY)
map_editable = cv2.imread('map.png')
map_editable = cv2.cvtColor(map_editable, cv2.COLOR_BGR2GRAY)

startTime = time.time()

def showPreview():
    preview = cv2.resize(map_editable, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Mapping', preview)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    time.sleep(0.1)