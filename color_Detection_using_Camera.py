import cv2

# Detect color name based on RGB values
def get_color_name(R, G, B):
    if R > 200 and G < 50 and B < 50:
        return "Red"
    elif G > 200 and R < 50 and B < 50:
        return "Green"
    elif R > 200 and G > 200 and B < 50:
        return "Yellow"
    elif R < 50 and G > 200 and B > 200:
        return "Cyan"
    elif R > 200 and G < 50 and B > 200:
        return "Magenta"
    elif R > 200 and G > 200 and B > 200:
        return "White"
    elif R < 50 and G < 50 and B < 50:
        return "Black"
    elif B > 200 and G < 50 and R < 50:
        return "Blue"
    else:
        return "Unknown"

# Mouse click event to grab color
def show_color(event, x, y, flags, param):
    global clicked, r, g, b, xpos, ypos
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked = True
        xpos, ypos = x, y
        b, g, r = frame[y, x]  # Note: cv2 uses (y,x)
        b, g, r = int(b), int(g), int(r)

# Initialize
cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Detection")
cv2.setMouseCallback("Color Detection", show_color)

clicked = False
r = g = b = xpos = ypos = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if clicked:
        # Draw color box
        cv2.rectangle(frame, (20, 20), (300, 60), (b, g, r), -1)

        # Get color name
        color_name = get_color_name(r, g, b)
        text = f"{color_name}  R={r} G={g} B={b}"

        # Put text over the box
        text_color = (255, 255, 255) if r + g + b < 400 else (0, 0, 0)
        cv2.putText(frame, text, (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2)

    cv2.imshow("Color Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
