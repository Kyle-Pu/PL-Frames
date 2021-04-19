import cv2
import os

imageDirectory = "Frames" # Directory to store image output

# Create our directory if nonexistent
isDir = os.path.isdir(imageDirectory)
if not isDir:
	os.mkdir(imageDirectory)

# Create sub-directories in output folder if nonexistent
angles = [-9, -4, -2, 0, 2, 4, 9]
for angle in angles:
	directoryPath = f"{imageDirectory}/%s" % angle
	if not os.path.isdir(directoryPath):
		os.mkdir(directoryPath)

# We want frames from all videos
for vidFilePath in os.listdir("./Videos"):
	videoCapture = cv2.VideoCapture(f"./Videos/{vidFilePath}") # Start video capture

    	# Keep extracting frames until end of video
	frameNum = 1 # For labeling frames
	while True:
		hasFramesLeft, image = videoCapture.read()   # Grab next video frame

		if not hasFramesLeft:
			break

		cv2.imwrite(f"./{imageDirectory}/{vidFilePath[0:vidFilePath.find('.')]}/{frameNum}.jpg", image) # Save frame as JPEG file, find folder via video name
		frameNum += 1
