import cv2 as cv


def create_tracker(tracker_type):
    if tracker_type == 'BOOSTING':
        return cv.TrackerBoosting.create()
    elif tracker_type == 'MIL':
        return cv.TrackerMIL_create()
    elif tracker_type == 'KCF':
        return cv.TrackerKCF_create()
    elif tracker_type == 'TLD':
        return cv.TrackerTLD_create()
    elif tracker_type == 'MEDIANFLOW':
        return cv.TrackerMedianFlow_create()
    elif tracker_type == 'GOTURN':
        return cv.TrackerGOTURN_create()
    elif tracker_type == 'MOSSE':
        return cv.TrackerMOSSE_create()
    elif tracker_type == "CSRT":
        return cv.TrackerCSRT_create()
    else:
        raise ValueError('Invalid param: tracker_type({})'.format(tracker_type))

