import tkinter as tk
import cv2
from deepface import DeepFace
import requests
import webbrowser

def detect_emotion():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite("captured.jpg", frame)
    cap.release()

    try:
        result = DeepFace.analyze("captured.jpg", actions=['emotion'])
        emotion = result[0]['dominant_emotion']
        show_recommendation(emotion)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def show_recommendation(emotion):
    recommendations = {
        "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "angry": "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP",
        "neutral": "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U",
        "surprise": "https://open.spotify.com/playlist/37i9dQZF1DX2aneNMeYHQ8",
        "fear": "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
        "disgust": "https://open.spotify.com/playlist/37i9dQZF1DWYNSm3Z3MxiM"
    }
    link = recommendations.get(emotion, "https://open.spotify.com/")
    result_label.config(text=f"Detected Emotion: {emotion.title()}")
    webbrowser.open(link)

root = tk.Tk()
root.title("Emotion-Based Music Recommender")
root.geometry("400x300")

tk.Label(root, text="Click below to detect emotion\nand get a music recommendation", font="Arial 14").pack(pady=20)
tk.Button(root, text="Detect Emotion", font="Arial 14", command=detect_emotion).pack(pady=10)
result_label = tk.Label(root, font="Arial 14")
result_label.pack(pady=20)

root.mainloop()
