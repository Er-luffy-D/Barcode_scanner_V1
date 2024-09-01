from pyzbar import pyzbar
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args=vars(ap.parse_args())

# load the input image

image=cv2.imread(args["image"])

# find the barcode in the image and decode each of the barcodes

barcodes= pyzbar.decode(image)

#loop over the detected barcodes 
for barcode in barcodes:

    # extract the bounding box location
    (x,y,w,h)=barcode.rect
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)

    # The barcode data is a bytes object so if we want to draw it on our output image we need to convert it into a string 
    # so converting it into string

    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    text=f"{barcodeData} ,({barcodeType})"
    cv2.putText(image,text,(x,y-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)

    print(f"[info] found {barcodeType} barcode :{barcodeData}")
    image=cv2.resize(image,(960,540))
    cv2.imshow("Image",image)
    cv2.waitKey(0)