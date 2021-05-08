def play_video(video_name = "output.mp4"):
    import numpy as np
    import cv2
    from time import time
    
    # Control play video speed.
    # 30fps / 1s = 0.033 s = 33.33 ms
    delay = 35

    cap = cv2.VideoCapture(video_name)

    start = time()

    while(cap.isOpened()):
        ret, frame = cap.read()
        
        # Judging the current number of frames
        if cap.get(cv2.CAP_PROP_POS_FRAMES) != cap.get(cv2.CAP_PROP_FRAME_COUNT):
            cv2.imshow('Video', frame)

            if cv2.waitKey(delay) & 0xFF == ord('q'):
                end = time() - start
                print("[INFO] Play %.2f s of video." % end)
                break
        else:
            end = time() - start
            print("[INFO] Play %.2f s video." % end)
            break
        
    cap.release()
    cv2.destroyAllWindows()