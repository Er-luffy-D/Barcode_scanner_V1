# Barcode scanner using commmand line argument
(I have also provided a sample image for test)
## Installation:

  ### 1. Clone the repository
  ```
  git clone https://github.com/Er-luffy-D/Barcode_scanner_V1
  ```
  ### 2. Install the dependencies
  ```
  cd Barcode_scanner_V1
  pip install -r requirements.txt
  ```
  ### 3. To run the code use (here you have to pass `--image` and `(image name with its extension)` & Image must be in same directory
  ```
  python barcode_scanner.py --image img.png
  ```
## Added realtime barcode scanner modified version of previous barcode scanner
  in this you can decode a barcode in realtime.
  ### To use this:
  ```
  python bar_scanner_camera.py
  ```
  this will automatically opens your camera and the decoding of barcode starts
