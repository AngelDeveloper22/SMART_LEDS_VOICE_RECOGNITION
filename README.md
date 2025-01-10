# SMART LEDS Voice Recognition

This project implements a voice recognition system designed to control LEDs based on the word **"HOLA"** spoken by a specific user. The system utilizes machine learning techniques to recognize the command and only respond to the designated voice. This project was developed as part of an advanced control class during a bachelor's degree in Electrical Mechanical Engineering.

---

## Folder Structure

```
SMART_LEDS_VOICE_RECOGNITION/
├── data/
│   ├── angel_voice/                        # Audio files of the designated user's voice
│   ├── other_voices/                       # Audio files of other users' voices
├── notebooks/
│   ├── audio_preprocessing_and_exploration.ipynb  # Explore and preprocess audio data
│   ├── voice_model_training.ipynb                # Train and evaluate the voice recognition model
├── src/
│   ├── communication_serial_smart.py             # Handle serial communication with LEDs
│   ├── firmware_leds.ino                         # Arduino firmware to control LED hardware
├── models/
│   ├── saved_model.pb                            # Trained TensorFlow model
│   ├── keras_metadata.pb                         # Metadata for the trained model
├── README.md                                     # Project documentation (this file)
```

---

## Features

1. **Voice Recognition**:
   - Trains a machine learning model to detect the word **"HOLA"**.
   - The model responds exclusively to a specific user’s voice.

2. **LED Control**:
   - Integrates with an Arduino to toggle LED states based on recognized commands.

3. **Preprocessing**:
   - Audio files are processed to extract features for training the model.

---

## Requirements

### Software

- Python 3.8 or later
- Jupyter Notebook
- TensorFlow 2.x
- Arduino IDE (for firmware deployment)

### Python Packages

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd SMART_LEDS_VOICE_RECOGNITION
   ```

2. **Set Up the Environment**:
   - Install the required Python packages.
   - Upload the `firmware_leds.ino` to your Arduino.

3. **Run Jupyter Notebooks**:
   - Navigate to the `notebooks/` directory.
   - Start with `audio_preprocessing_and_exploration.ipynb` to preprocess and analyze audio data.
   - Use `voice_model_training.ipynb` to train and evaluate the voice recognition model.

4. **Test the System**:
   - Run `communication_serial_smart.py` to enable communication between the model and the Arduino.

---

## Dataset

- Audio recordings of the word **"HOLA"** spoken by multiple users, including the designated user.
- Located in the `data/` folder:
  - `angel_voice/`: Audio recordings of the designated user's voice.
  - `other_voices/`: Audio recordings of other users' voices.
- Ensure audio files are preprocessed using the provided notebook before training the model.

---

## Outputs

- **Trained Model**:
  - Saved in the `models/` folder as `saved_model.pb`.

- **Performance Metrics**:
  - Accuracy and loss values logged during training.

---

## Contribution

- Feel free to fork this repository and suggest improvements.
- Report any issues or bugs through the GitHub issue tracker.

---

## License

This project is open-source and licensed under the MIT License.

---

## Acknowledgments

- Developed as part of an advanced control class.
- Special thanks to the TensorFlow and Arduino communities for their resources and tools.

---

