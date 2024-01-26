import rosbag
import numpy as np
from cv_bridge import CvBridge 
import cv2

# Bag paths
bag_file_path = "database/experiment/bags/bead1.bag"
video_file_path = "database/experiment/videos/bead1.avi"

bridge = CvBridge()

show = False

list_images = []
with rosbag.Bag(bag_file_path, 'r') as bag:
    # Iterate through the messages in the bag
    for topic, msg, t in bag.read_messages():
        # Process the messages as needed
        if topic == "/xiris/image_raw":

            # Extract image
            image = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            height, width = image.shape
            size = (width, height)
            list_images.append(image)

            # Show Image    
            if show:
                cv2.imshow("Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

