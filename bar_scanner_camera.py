from pyzbar import pyzbar
import cv2

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,image=cap.read()
    # find the barcode in the image and decode each of the barcodes
    # image=cv2.resize(image,(960,540))

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
    cv2.imshow("Image",image)
    if cv2.waitKey(1)==ord('q') :
        break