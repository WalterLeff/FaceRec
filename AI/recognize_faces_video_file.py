# USAGE
# python recognize_faces_video_file.py --encodings encodings.pickle --input videos/lunch_scene.mp4
# python recognize_faces_video_file.py --encodings encodings.pickle --input videos/lunch_scene.mp4 --output output/lunch_scene_output.avi --display 0
#python recognize_faces_video_file.py --encodings encodings.pickle --input videos/WIN_20191227_14_35_51_Pro.mp4 --output WIN_20191227_14_35_51_Pro_output.avi --display 0
# import the necessary packages
import face_recognition
from datetime import datetime
import argparse
import imutils
import pickle
import time
import cv2


def recognize_faces_video_file():

    now = datetime. now()
    current_time = now. strftime("%H:%M:%S")

    # load the known faces and embeddings
    print(current_time + "[INFO] loading encodings...")
    data = pickle.loads(open("AI/encodings.pickle", "rb").read())


    # initialize the pointer to the video file and the video writer
    print(current_time + "[INFO] processing video...")

    inputFile = 'AI/videos/Test2.mp4'
    stream = cv2.VideoCapture(inputFile)
    writer = None
    print(current_time + "[INFO] stream opened ... ")
    # loop over frames from the video file stream
    while True:
        # grab the next frame
        (grabbed, frame) = stream.read()

        # if the frame was not grabbed, then we have reached the
        # end of the stream
        if not grabbed:
            break

        # convert the input frame from BGR to RGB then resize it to have
        # a width of 750px (to speedup processing)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=750)
        r = frame.shape[1] / float(rgb.shape[1])

        # detect the (x, y)-coordinates of the bounding boxes
        # corresponding to each face in the input frame, then compute
        # the facial embeddings for each face
        boxes = face_recognition.face_locations(rgb, model='cnn')
        encodings = face_recognition.face_encodings(rgb, boxes)
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"], encoding)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)

            # update the list of names
            names.append(name)

        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # rescale the face coordinates
            top = int(top * r)
            right = int(right * r)
            bottom = int(bottom * r)
            left = int(left * r)

            # draw the predicted face name on the image
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(
                frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2
            )
            print(name)

        output = 'AI/output/test.avi'
        # if the video writer is None *AND* we are supposed to write
        # the output video to disk initialize the writer
        if writer is None and output is not None:
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(
                output, fourcc, 24, (frame.shape[1], frame.shape[0]), True
            )

        # if the writer is not None, write the frame with recognized
        # faces t odisk
        if writer is not None:
            writer.write(frame)

        # # check to see if we are supposed to display the output frame to
        # # the screen
        # if args["display"] > 0:
        #     cv2.imshow("Frame", frame)
        #     key = cv2.waitKey(1) & 0xFF

        #     # if the `q` key was pressed, break from the loop
        #     if key == ord("q"):
        #         break

    # close the video file pointers
    stream.release()

    # check to see if the video writer point needs to be released
    if writer is not None:
        writer.release()
    print(current_time + "[INFO] ready...")
#recognize_faces_video_file()