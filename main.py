import cv2 as cv

if __name__ == '__main__':

    # Read video
    video = cv.VideoCapture('videos/bball1_sd.mp4')

    # Exit if video not opened
    if not video.isOpened():
        print 'Could not open video'
        exit()

    # get fps
    fps = video.get(cv.CAP_PROP_FPS)
    if fps <= 0:
        print 'Unable to read FPS. Defaulting to 25'
        fps = 25

    # Read first frame
    ok, frame = video.read()
    if not ok:
        print 'Cannot read video file'
        exit()

    # Tracking loop
    while(True):
        # Capture frame-by-frame
        ok, frame = video.read()
        if not ok:
            print 'Done reading video file'
            break

        # Display the resulting frame
        cv.imshow('tracking',frame)

        # check if user quit, by pressing 'q' or ESC
        wait_time = int(900 / fps)
        key = cv.waitKey(wait_time) & 0xff
        if key == ord('q') or key == 27:
            break

    # When everything done, release the capture
    video.release()
    cv.destroyAllWindows()
