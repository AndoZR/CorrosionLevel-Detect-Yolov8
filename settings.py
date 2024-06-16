from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM, RTSP, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'pict2.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'pict1.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEOS_DICT = {
    'vid1': VIDEO_DIR / 'vid1.mp4',
    'vid2': VIDEO_DIR / 'vid2.mp4',
    'vid3': VIDEO_DIR / 'vid3.mp4',
    'vid4': VIDEO_DIR / 'vid4.mp4',
    'vid5': VIDEO_DIR / 'vid5.mp4',
    'vid6': VIDEO_DIR / 'vid6.mp4',
    'vid7': VIDEO_DIR / 'vid7.mp4',
}

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
# DETECTION_MODEL = MODEL_DIR / 'best.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

# SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'best.pt'

# Webcam
WEBCAM_PATH = 0
