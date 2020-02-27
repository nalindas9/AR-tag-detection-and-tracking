# AR-tag-detection-and-tracking
ENPM673 Project: Detecting an AR tag in a video file and implementing augmented reality applications in the video

Follow the steps below to execute the program:

1. Clone the file. 
2. Once extracted, navigate to the src Folder. Here you will find three python scripts - cube.py, lena.py, and mylib.py.
3. To run the Lena image Superimpose Code, run the python script - lena.py by using the command "python lena.py" in the Terminal. Python version: 3.7.4
4. To run the Cube Superimpose code, run the python script - cube.py by using the command "python cube.py"

You will be prompted to enter some arguments when you the scripts:
1. Enter the Video you want the image or cube to be superimposed on.
2. Enter the path of the folder where you have all the videos and the image. Remember to put all of the videos and the image in the same folder. For eg. /home/user/Downloads means that all videos and image are in the Downloads folder.
3. Specify the name of the image you want to be superimposed for eg. Lena.png
4. Let it run until the video renders completely. 
5. The video will be saved as "Cube.avi" and "Lena.avi" in the path you specified earlier.


The Link for the Videos are:

https://drive.google.com/drive/folders/1qQ-2OK3BI_u52wEMzeqOyZm5m6r8ZpaV?usp=sharing

The videos include - Superimposing of template image on all the test videos and of a 3D cube on all the test videos.

Have designed a self-implemented version of cv2.warpPerspective
One of the issues faced was, the computation time of this function was alot. After iterating over just a small range of pixel range, I could optimize the code.
The code which took a run time of 1 hour to render, now takes just 10 minutes maximum. Go through the function 'warpTag()' and 'warpLena()' in the file mylib.py

Check the Images along with this folder, for seeing the outputs in the folder 'output-pictures'


