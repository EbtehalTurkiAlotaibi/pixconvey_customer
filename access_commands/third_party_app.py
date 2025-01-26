
import tkinter as tk
from PIL import Image, ImageTk
import json
import paho.mqtt.client as mqtt
import datetime
# MQTT callback functions
vehicle_id = "000002"
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print("Connection failed")
    display_robot_info()

def on_message(client, userdata, message):
    message = json.loads(message.payload.decode())
    timestamp = message["timestamp"]
    vehiceData = message["vehiceData"]

    electric = vehiceData["electric"]
    drivingMode = vehiceData["drivingMode"]
    speed = vehiceData["speed"]
    doorStatus = vehiceData["doorStatus"]
    location = "h:" + str(vehiceData["heading"]) + ", (" +str(vehiceData["lat"]) + "," + str(vehiceData["lon"]) +")"

    print("Info = ",message)
    update_info_text(timestamp, electric, drivingMode, speed, doorStatus, location )
    client.unsubscribe("/vehicle/info/"+vehicle_id)

def update_info_text(timestamp, electric, drivingMode, speed, doorStatus, location):
    # data preparation
    # Time:
    current_time = datetime.datetime.utcfromtimestamp(timestamp)
    # Charging
    min_value = 39.0
    max_value = 55.4
    # Check if the current value is within the specified range
    if electric < min_value:
        electric = min_value
    elif electric > max_value:
        electric = max_value
    # Driving mode
    mode = "Autonomous"
    if drivingMode == 1:
        mode = "Human Control"
    # Speed
    speed_kmh = round((speed / 100) * 3.6, 3)
    # Door
    status = "Closed"
    if doorStatus == 0:
        status = "Opened"
    percentage = (electric - min_value) / (max_value - min_value) * 100
    info_text.delete(1.0, tk.END)  # Clear the existing text
    info_text.insert(tk.END, f"Time: {current_time} GMT\n")
    info_text.insert(tk.END, f"Charging Level: {percentage:.1f}%\n")
    info_text.insert(tk.END, f"Driving Mode: {mode}\n")
    info_text.insert(tk.END, f"Speed: {speed_kmh} Km/h\n")
    info_text.insert(tk.END, f"Door Status: {status}\n")
    info_text.insert(tk.END, f"Location: {location}")

def create_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("Pixconvey", "Pixconvey")
    client.connect("51.20.236.180", 1883, 60)
    client.loop_start()
    return client

def openCargo():
    message = {
        "timestamp": 1600050933000,
        "taskId": "180",
        "doorControl": 0
    }
    print(message)
    message = json.dumps(message)
    client.publish("/cloud/control/door/"+vehicle_id, message)
    display_robot_info()

def display_robot_info():
    client.subscribe("/vehicle/info/"+vehicle_id)
    # Schedule the next call to display_robot_info in 10 seconds
    root.after(10000, display_robot_info)

# Function to execute MQTT publication for delivery
def deliver():
    dict_place = {
        "Wrap bar": '10000',
        "Tempo!": '10001',
        "JCMB": '10002'
    }
    combo_box1_get = combo_box1.get()
    combo_box2_get = combo_box2.get()

    message = {
        "timestamp": 1697683950,
        "taskId": 123456,
        "businessType": 3,
        "stopPointList": [
            {"nodeID": dict_place[combo_box1_get]},
            {"nodeID": dict_place[combo_box2_get]}
        ]
    }
    message = json.dumps(message)
    print(message)
    client.publish("/cloud/driving/path/"+vehicle_id, message)

# Create a circular button
def create_circular_button(canvas, x, y, text, command):
    button = canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="whitesmoke", width=3, outline='silver')
    text = canvas.create_text(x, y, text=text, font=("Arial", 12, "bold"), fill="navy")
    canvas.tag_bind(button, "<Button-1>", lambda event: command())
    


# Create the main window
root = tk.Tk()
root.title("Pixconvey Controller")
window_width, window_height = 700, 500
root.geometry(f"{window_width}x{window_height}")

# Set the background color of the main window
root.configure(bg="white")

# Create a frame for the image and logo
image_frame = tk.Frame(root)
image_frame.pack(side=tk.LEFT, padx=20, pady=20)

# Set the background color of the image frame
image_frame.configure(bg="white")

# Load the image with an absolute path
image_path = "fig.png"  # Replace with the actual path to your image
original_image = Image.open(image_path)
resized_image = original_image.resize((500, 300))

# Create a border by using a Label widget
border = tk.Label(image_frame, relief="sunken")
border.pack()

tk_image = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = tk.Label(border, image=tk_image)
image_label.pack()

# Load the logo image with an absolute path and resize it to 200x80 pixels
logo_path = "log1_.png"  # Replace with the actual path to your logo image
original_logo = Image.open(logo_path)
resized_logo = original_logo.resize((200, 80))
tk_logo = ImageTk.PhotoImage(resized_logo)

# Create a label for the logo and place it in the bottom-left corner
logo_label = tk.Label(image_frame, image=tk_logo, bg="white")
logo_label.pack(side=tk.LEFT, anchor=tk.SW)

# Create a frame for buttons
button_frame = tk.Frame(image_frame)
button_frame.pack(pady=10)

# Create a "Robot Info" button
info_label = tk.Label(button_frame, text="Robot Info", bg='white', font=("Arial", 12, "bold"), foreground="navy", relief="sunken")
info_label.pack(fill='x')

# Create a frame to contain the text widget and give it a sunken relief
info_text_frame = tk.Frame(button_frame, relief="sunken", borderwidth=2, bg="black")
info_text_frame.pack(fill='both', expand=True)

# Create a text widget to display robot information inside the frame
info_text = tk.Text(info_text_frame, height=6, width=40, bg='black', fg='white',highlightthickness=0)  # Set background to whitesmoke and text to black
info_text.insert(tk.END,"Time:\n")
info_text.insert(tk.END, "Charging Level:\n")
info_text.insert(tk.END, "Driving Mode:\n")
info_text.insert(tk.END, "Speed:\n")
info_text.insert(tk.END, "Door Status:\n")
info_text.insert(tk.END, "Location:")
info_text.pack(fill='both', expand=True)

delivery_frame = tk.Frame(root, bg="white")  # Set the background color to white
delivery_frame.pack(side=tk.LEFT, padx=10, pady=10)

# Create a button instead of circular button
# Create a canvas for circular "Deliver" button
canvas = tk.Canvas(delivery_frame, width=80, height=80, bg="white", highlightthickness=0)
canvas.pack(side=tk.TOP, padx=5, pady=5)  # Adjusted the vertical padding


create_circular_button(canvas, 35, 35, "Deliver", deliver)  # Adjusted the y-coordinate (y = 20)


# Create two combo boxes with the same list of options within the frame
combo_options = ["Wrap bar", "Tempo!", "JCMB"]
combo_box1 = tk.StringVar()
combo_box2 = tk.StringVar()

combo_box1.set(combo_options[0])
combo_box2.set(combo_options[0])

combo_menu1 = tk.OptionMenu(delivery_frame, combo_box1, *combo_options)
combo_menu2 = tk.OptionMenu(delivery_frame, combo_box2, *combo_options)

# Set background and foreground attributes for combo boxes
combo_menu1.config(width=20, bg="white", foreground="navy")
combo_menu2.config(width=20, bg="white", foreground="navy")

# Set the highlightbackground to white for both combo boxes
combo_menu1["menu"].config(bg="white", fg="navy")
combo_menu2["menu"].config(bg="white", fg="navy")

combo_menu1.pack(pady=30)
combo_menu2.pack(pady=30)


# Create a canvas for "Open" button
# Create a canvas for circular "Deliver" button
canvas = tk.Canvas(delivery_frame, width=80, height=80,bg="white", highlightthickness=0)
canvas.pack(side=tk.BOTTOM, padx=5, pady=5)  # Adjusted the vertical padding

create_circular_button(canvas, 35, 35, "Open", openCargo)  # Adjusted the y-coordinate (y = 20)


# Create an MQTT client
client = create_mqtt_client()

# Start the main event loop
root.after(10000, display_robot_info)  # Initial call to start updating info
root.mainloop()

