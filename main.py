import cv2 as cv
import argparse
from tracker.tracker import ActionTracker

if __name__ == '__main__':

    # parse arguments
    ap = argparse.ArgumentParser()
    ap.add_argument('-v', '--video', help='path to the video file')
    args = vars(ap.parse_args())

    # read video
    video = None
    if args.get("video", False):
        video = cv.VideoCapture(args["video"])
    else:
        print 'Please specify video file'
        exit()

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

    # init tracker
    tracker = ActionTracker()
    # ball_rect = (456, 148, 12, 12) # SD
    ball_rect = (908, 295, 29, 25) # HD
    # ballrect =
    tracker.init(frame, ball_rect=ball_rect)

    # Tracking loop
    count = 1
    while(True):
        # Capture frame-by-frame
        ok, frame = video.read()
        if not ok:
            print 'Done reading video file'
            break

        # update tracker
        ok = tracker.update(frame)
        count += 1
        if not ok:
            print 'on frame {}, failed to track'.format(count)
            break

        # draw bounding box
        rect = tracker.ball_rect
        cv.rectangle(frame, (int(rect[0]), int(rect[1])), (int(rect[0] + rect[2]), int(rect[1] + rect[3])), (255, 0, 0), 2, 1)


        # Display the resulting frame
        cv.imshow('tracking',frame)

        # wait between frames to show at 'normal' speed
        wait_time = int(900 / fps)

        # check if user quit, by pressing 'q' or ESC
        key = cv.waitKey(wait_time) & 0xff
        if key == ord('q') or key == 27:
            break

        # write frame out to file
        # cv.imwrite('videos/frame.png', frame)
        # exit()


    # When everything done, release the capture
    video.release()
    cv.destroyAllWindows()
