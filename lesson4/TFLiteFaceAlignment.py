import numpy as np
import cv2
from numpy.ma.core import left_shift
import tensorflow as tf
from functools import partial
from TFLiteFaceDetector import UltraLightFaceDetecion
import sys

#left_eye = 35,36,33,37,39,42,40,41
#righ_eye = 89,90,87,91,93,96,94,95
#lips = 52,55,56,53,59,58,61,68,67,71 63,64


class CoordinateAlignmentModel():
    def __init__(self, filepath, marker_nums=106, input_size=(192, 192)):
        self._marker_nums = marker_nums
        self._input_shape = input_size
        self._trans_distance = self._input_shape[-1] / 2.0

        self.eye_bound = ([35, 41, 40, 42, 39, 37, 33, 36],
                          [89, 95, 94, 96, 93, 91, 87, 90])

        # tflite model init
        self._interpreter = tf.lite.Interpreter(model_path=filepath)
        self._interpreter.allocate_tensors()

        # model details
        input_details = self._interpreter.get_input_details()
        output_details = self._interpreter.get_output_details()

        # inference helper
        self._set_input_tensor = partial(self._interpreter.set_tensor,
                                         input_details[0]["index"])
        self._get_output_tensor = partial(self._interpreter.get_tensor,
                                          output_details[0]["index"])

        self.pre_landmarks = None

    def _calibrate(self, pred, thd, skip=6):
        if self.pre_landmarks is not None:
            for i in range(pred.shape[0]):
                if abs(self.pre_landmarks[i, 0] - pred[i, 0]) > skip:
                    self.pre_landmarks[i, 0] = pred[i, 0]
                elif abs(self.pre_landmarks[i, 0] - pred[i, 0]) > thd:
                    self.pre_landmarks[i, 0] += pred[i, 0]
                    self.pre_landmarks[i, 0] /= 2

                if abs(self.pre_landmarks[i, 1] - pred[i, 1]) > skip:
                    self.pre_landmarks[i, 1] = pred[i, 1]
                elif abs(self.pre_landmarks[i, 1] - pred[i, 1]) > thd:
                    self.pre_landmarks[i, 1] += pred[i, 1]  
                    self.pre_landmarks[i, 1] /= 2
        else:
            self.pre_landmarks = pred

    def _preprocessing(self, img, bbox, factor=3.0):

        maximum_edge = max(bbox[2:4] - bbox[:2]) * factor
        scale = self._trans_distance * 4.0 / maximum_edge
        center = (bbox[2:4] + bbox[:2]) / 2.0
        cx, cy = self._trans_distance - scale * center

        M = np.array([[scale, 0, cx], [0, scale, cy]])

        cropped = cv2.warpAffine(img, M, self._input_shape, borderValue=0.0)
        inp = cropped[..., ::-1].astype(np.float32)

        return inp[None, ...], M

    def _inference(self, input_tensor):
        self._set_input_tensor(input_tensor)
        self._interpreter.invoke()

        return self._get_output_tensor()[0]

    def _postprocessing(self, out, M):
        iM = cv2.invertAffineTransform(M)
        col = np.ones((self._marker_nums, 1))

        out = out.reshape((self._marker_nums, 2))

        out += 1
        out *= self._trans_distance

        out = np.concatenate((out, col), axis=1)

        return out @ iM.T  # dot product

    def get_landmarks(self, image, detected_faces=None):

        for box in detected_faces:
            inp, M = self._preprocessing(image, box)
            out = self._inference(inp)
            pred = self._postprocessing(out, M)

            # self._calibrate(pred, 1, skip=6)
            # yield self.pre_landmarks

            yield pred


def warp_effect(frame,landmark,num1,num2):
 
            x = min(landmark[:,0])
            x_max = max(landmark[:,0])
            y = min(landmark[:,1])
            y_max = max(landmark[:,1])
            w = x_max-x
            h = y_max-y
            median_x = (x+x_max)//2
            median_y = (y+y_max)//2
            
            mask = np.zeros(frame.shape,np.uint8) 
            cv2.drawContours(mask,[landmark],-1,(255,255,255),-1)
            img_resize = cv2.resize(frame,(0,0),fx=num2,fy=num2)
            img_resize=img_resize / 255
            mask_resize = cv2.resize(mask,(0,0),fx=num2,fy=num2)
            mask_resize=mask_resize / 255
            image = frame[int(median_y - (num1*h)):int(median_y+(num1*h)),int(median_x-(num1*w)):int(median_x+(num1*w))]
            image=image / 255
            try:
                forground = cv2.multiply(mask_resize,img_resize)
                background = cv2.multiply(image,1-mask_resize[y*num2:(y+h)*num2,x*num2:(x+w)*num2])
                resualt = cv2.add(background,forground[y*num2:(y+h)*num2,x*num2:(x+w)*num2])
                resualt = resualt*255
                frame[int(median_y - (num1*h)):int(median_y+(num1*h)),int(median_x-(num1*w)):int(median_x+(num1*w))]= resualt
            except:
                 pass

            # ---------> ((y_min+y_max)/2) -/+ h     |2x
            # ---------> ((x_min+x_max)/2) -/+ w     |2x

            # ---------> ((y_min+y_max)/2) -/+ 2*h   |4x
            # ---------> ((x_min+x_max)/2) -/+ 2*w   |4x

            # ---------> ((y_min+y_max)/2) -/+ 1.5*h |3x 
            # ---------> ((x_min+x_max)/2) -/+ 1.5*w |3x

            return frame
    

if __name__ == '__main__':
    fd = UltraLightFaceDetecion("weights/RFB-320.tflite",conf_threshold=0.88)
    fa = CoordinateAlignmentModel("weights/coor_2d106.tflite")


    cap = cv2.VideoCapture(0)
    format = cv2.VideoWriter_fourcc(*"XVID")
    save = cv2.VideoWriter("video.mp4",format,20.0,(640, 480))
    while True:
        ret , frame = cap.read()
        boxes, scores = fd.inference(frame)

        for pred in fa.get_landmarks(frame, boxes):
            pred_int = np.round(pred).astype(np.int)

            eye_left = [35,36,33,37,39,42,40,41]
            landmark_left_eye = []
            for i in eye_left:
                landmark_left_eye.append(tuple(pred_int[i]))
            
            eye_right = [89,90,87,91,93,96,94,95]
            landmark_right_eye = []
            for i in eye_right:
                landmark_right_eye.append(tuple(pred_int[i]))


            lips = [52,55,56,53,59,58,61,68,67,71,63,64]
            landmark_lips = []
            for i in lips:
                landmark_lips.append(tuple(pred_int[i]))
            
            landmark_left_eye = np.array(landmark_left_eye)
            landmark_right_eye = np.array(landmark_right_eye)
            landmark_lips = np.array(landmark_lips)

            # for i,p in enumerate(np.round(pred).astype(np.int)):
            #     cv2.circle(img, tuple(p), 1, (125, 255, 125), 1, cv2.LINE_AA)
            #     cv2.putText(img,str(i),tuple(p),cv2.FONT_HERSHEY_COMPLEX,0.25,(0,0,255),1)
            #     print(i,p)
            
            _,y1 = pred_int[60]
            _,y2 = pred_int[62]

            warp_effect(frame,landmark_left_eye,1,2)
            warp_effect(frame,landmark_right_eye,1,2)
            if 5 <= y1-y2 <=15:
                warp_effect(frame,landmark_lips,1,2)
            if 16<= y1-y2 <=27:
                warp_effect(frame,landmark_lips,1.5,3)
            if 28<= y1-y2:
                warp_effect(frame,landmark_lips,2,4)
        save.write(frame)
        cv2.imshow("Face warp effect",frame)
        if cv2.waitKey(1) & 0xFF==ord("0"):
            break

cap.release()
save.release()
cv2.destroyAllWindows()
