import cv2
import numpy as np


def count_fingers(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blurred, 125, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if contours:
        hand_contour = max(contours, key=cv2.contourArea)
        hull = cv2.convexHull(hand_contour, returnPoints=False)
        cv2.drawContours(image, hand_contour, -1, (0, 255, 0), 3)
        fingers = 0

        if len(hull) > 3:#ignore irrelevent contours
            defects = cv2.convexityDefects(hand_contour, hull)
            if defects is not None:
                for defect in defects:
                    start, end, far, _ = defect[0]
                    start_point = tuple(hand_contour[start][0])
                    end_point = tuple(hand_contour[end][0])
                    far_point = tuple(hand_contour[far][0])

                    a = np.sum((np.array(far_point) - np.array(start_point))**2)
                    b = np.sum((np.array(far_point) - np.array(end_point))**2)
                    c = np.sum((np.array(start_point) - np.array(end_point))**2)
                    angle = np.arccos((a**2 + b**2 - c**2) / (2 * a * b))

                    if angle <= np.pi / 2:
                        fingers += 1

        return fingers
    else:
        return 0


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        fingers_left = count_fingers(frame[:, :frame.shape[1] // 2])
        fingers_right = count_fingers(frame[:, frame.shape[1] // 2:])

        fingers_sum = fingers_left + fingers_right

        if fingers_sum % 2 == 0:
            result_color = (0, 255, 0)  # Green
        else:
            result_color = (0, 0, 255)  # Red

        result_text = f"Sum: {fingers_sum}"

        cv2.putText(frame, result_text, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, result_color, 2)
        cv2.imshow("Finger Counting", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


main()
