#!/usr/bin/env python3

import argparse
import os
import picamera
import sys
import datetime
from twython import Twython

# fill this out

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def main():
    args = parser.parse_args()
    
    video = open('/pi/home/record.mp4', 'rb')
    response = twitter.upload_video(media=video, media_type='video/mp4')
    twitter.update_status(status='action at ', media_ids=[response['media_id']]) # add datetime.now()
    
    with ImageInference(image_classification.model(model_type)) as inference:
        with picamera.PiCamera(resolution=(1920, 1080)) as camera:
            stream = picamera.PiCameraCircularIO(camera, seconds=args.capture_length)
            camera.start_recording(stream, format='h264')
            while True:
                detection, image, inference_data = detect_object(
                    inference, camera, classes, args.threshold, debug_out,
                    (args.cropbox_left, args.cropbox_right),
                    (args.cropbox_top, args.cropbox_bottom))
                if detection:
                    detect_time = int(time.time())
                    camera.wait_recording(args.capture_delay)
                    video_file = 'capture_%d.mpeg' % detect_time
                    image_file = 'capture_%d.jpg' % detect_time
                    stream.copy_to(os.path.join(args.out_dir, video_file))
                    stream.flush()
                    debug_output(image, inference_data, args.out_dir, image_file)
                    print('Wrote video file to', os.path.join(args.out_dir, video_file))
                    camera.wait_recording(max(args.capture_length - args.capture_delay, 0))


if __name__ == '__main__':
    main()
