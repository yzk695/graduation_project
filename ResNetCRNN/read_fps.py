import cv2

def sample_clips(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
    except:
        print('Can not open %s.' % video_path)
        pass
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if ret is False:
            break
        frame_count = frame_count + 1
    return frame_count

import os
import pickle
import pdb
import pandas as pd
if __name__ == '__main__':
    root_path = "UCF8/"
    filenames = os.listdir(root_path)
    frame_dict = {}
    action_name = []
    for avi in filenames:
        frames = sample_clips(root_path + avi)
        # pdb.set_trace()
        name = avi.split(".")[0]

        loc1 = name.find('v_')
        loc2 = name.find('_g')
        label = name[(loc1 + 2): loc2]
        pdb.set_trace()

        if label not in action_name:
            action_name.append(label)
        frame_dict[name] = frames
    # df = pd.DataFrame([frame_dict])
    # with open("UCF8_frame_count.pkl", "wb") as f:
    #     pickle.dump(df, f)
    with open("UCF8actions.pkl", "wb") as f1:
        pickle.dump(action_name, f1) 