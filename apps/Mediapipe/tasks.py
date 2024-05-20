import cv2
from . import handTrackingModule as htm

def Track_numbers():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4, 480)

    l = ['' , ]
    n = ''

    detector = htm.handDetector(detectionCon=0.75)
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmlist = detector.findPosition(img,draw=False)
        if len(lmlist) != 0:
            k= lmlist[8][2] > lmlist[6][2]
            if not k and not lmlist[20][2] < lmlist[18][2]:
                n=1
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
                
            if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]    and not lmlist[4][1] > lmlist[8][1]: 
                n=2
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if lmlist[4][1]  >lmlist[12][1] and lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2]   and lmlist[16][2] > lmlist[14][2]: 
                n=3
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            
            if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[20][2] < lmlist[18][2]: 
                n=4
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if  lmlist[4][1] > lmlist[12][1] and    lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[20][2] < lmlist[18][2]: 
                n=5
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] < lmlist[12][1] and lmlist[20][2] > lmlist[18][2]: 
                n=6
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            
            if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
                n=7
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if lmlist[8][2] < lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
                n=8
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if lmlist[8][2] > lmlist[6][2] and lmlist[12][2] < lmlist[10][2] and lmlist[16][2] < lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] < lmlist[18][2]: 
                n=9
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
            if lmlist[8][2] > lmlist[6][2] and lmlist[12][2] > lmlist[10][2] and lmlist[16][2] > lmlist[14][2] and lmlist[4][1] > lmlist[20][1] and lmlist[20][2] > lmlist[18][2]: 
                n=10
                cv2.rectangle(img,(20,255),(170,425),(0,255,0),cv2.FILLED)
                cv2.putText(img,str(n),(45,375),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)
                
            if n != l[-1]:
                l.append(n)

        
        
        cv2.imshow("image",img)
        key  = cv2.waitKey(1)
        if key == 27:
            cap.release()
            cv2.destroyAllWindows()
            return(l)