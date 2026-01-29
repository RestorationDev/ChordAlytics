import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


def draw_rectangle(frame, bbox):
    x, y, w, h = [int(i) for i in bbox]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


def select_quadrilateral_roi(frame):
    print("Please select four points around the object to track.")
    points = []

    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))
            cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)
            if len(points) == 4:
                cv2.destroyAllWindows()

    cv2.imshow("Select ROI", frame)
    cv2.setMouseCallback("Select ROI", click_event)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(points) == 4:
        return np.array(points, dtype=np.float32)
    print("Error: You must select exactly four points.")
    return None


def compute_homography(src_points, dst_points):
    H, _ = cv2.findHomography(src_points, dst_points)
    return H


def apply_homography(H, point):
    point_homogeneous = np.array([point[0], point[1], 1])
    transformed = np.dot(H, point_homogeneous)
    transformed /= transformed[2]
    return transformed[0], transformed[1]


ret, frame = cap.read()
if not ret:
    print("Error: Failed to capture initial frame.")
    exit()

src_points = select_quadrilateral_roi(frame)
if src_points is None:
    cap.release()
    cv2.destroyAllWindows()
    exit()

width, height = 100, 100
dst_points = np.array([
    [0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]
], dtype=np.float32)
H = compute_homography(src_points, dst_points)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
    cv2.imshow("Webcam Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
