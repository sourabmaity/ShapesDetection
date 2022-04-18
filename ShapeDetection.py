import cv2

img = cv2.imread("shape4.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours[1:]:
    approx = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [contour], 0, (255, 0, 255), 2)
    x, y, w, h = cv2.boundingRect(contour)
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 1)
    elif len(approx) == 4:
        cv2.putText(img, "Square", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 1)
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 1)
    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 1)
    else:
        cv2.putText(img, "Circle", (x + w // 2, y + h // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.6, [255, 255, 0], 1)
    # print(len(approx))
    cv2.imshow("detect", img)
    # cv2.imshow("detect", threshold)
    cv2.waitKey(1000)

cv2.destroyAllWindows()
