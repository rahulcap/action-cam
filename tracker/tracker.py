import cv2 as cv


class ActionTracker(object):
    # vars
    _tracker = None
    _ball_rect = None
    _frame = None

    ##
    # constructor
    #
    def __init__(self, tracker_type='KCF'):
        if tracker_type == 'BOOSTING':
            self._tracker = cv.TrackerBoosting_create()
        elif tracker_type == 'MIL':
            self._tracker = cv.TrackerMIL_create()
        elif tracker_type == 'KCF':
            self._tracker = cv.TrackerKCF_create()
        elif tracker_type == 'TLD':
            self._tracker = cv.TrackerTLD_create()
        elif tracker_type == 'MEDIANFLOW':
            self._tracker = cv.TrackerMedianFlow_create()
        elif tracker_type == 'GOTURN':
            self._tracker = cv.TrackerGOTURN_create()
        elif tracker_type == 'MOSSE':
            self._tracker = cv.TrackerMOSSE_create()
        elif tracker_type == 'CSRT':
            self._tracker = cv.TrackerCSRT_create()
        else:
            raise ValueError('Invalid tracker_type: {}'.format(tracker_type))

    ##
    # properties
    #
    @property
    def ball_rect(self):
        return self._ball_rect

    ##
    # init tracker
    #
    def init(self, frame, ball_rect = None):
        self._frame = frame
        if ball_rect is not None:
            self._ball_rect = ball_rect
        # TODO scan image for best rect
        if self._ball_rect is not None:
            ok = self._tracker.init(frame, self._ball_rect)
            if not ok:
                raise Exception('Unable to init tracker')

    ##
    # update tracker
    #
    def update(self, frame):
        self._frame = frame
        ok, rect = self._tracker.update(frame)
        if ok:
            self._ball_rect = rect
        else:
            # TODO log failures to track
            print 'failed to track ball'

        return ok

