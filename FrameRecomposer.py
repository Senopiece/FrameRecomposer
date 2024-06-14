import cv2
import os
import argparse
from tqdm import tqdm
from natsort import natsorted


def extract_frames(video_path, frames_dir):
    video_cap = cv2.VideoCapture(video_path)
    total_frames = int(video_cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if not total_frames:
        print(f"No video found on the provided path")
        return

    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    
    print(f"Extracting frames from {video_path}...")
    success, frame = video_cap.read()
    count = 0
    with tqdm(total=total_frames, unit="frame") as pbar:
        while success:
            frame_path = os.path.join(frames_dir, f"{count}.jpg")
            cv2.imwrite(frame_path, frame)
            success, frame = video_cap.read()
            count += 1
            pbar.update(1)
    
    print(f"Extracted {count} frames from {video_path}")

def create_video(frames_dir, output_path, fps=30):
    frames = [os.path.join(frames_dir, frame) for frame in os.listdir(frames_dir) if frame.endswith(".jpg")]
    frames = natsorted(frames)
    if not frames:
        print(f"No frames found in {frames_dir}. Skipping video creation.")
        return

    frame_height, frame_width, _ = cv2.imread(frames[0]).shape
    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
    
    print(f"Creating video {output_path} from frames...")
    with tqdm(total=len(frames), unit="frame") as pbar:
        for frame in frames:
            # print(frame)
            img = cv2.imread(frame)
            video_writer.write(img)
            pbar.update(1)
    
    video_writer.release()
    print(f"Video {output_path} created successfully.")

def main():
    parser = argparse.ArgumentParser(description="FrameRecomposer - A tool for extracting and recomposing video frames using OpenCV.")
    subparsers = parser.add_subparsers(dest='command', help='Sub-command help')
    
    # Subparser for extracting frames
    parser_extract = subparsers.add_parser('extract', help='Extract frames from a video')
    parser_extract.add_argument('--video', type=str, required=True, help='Path to the input video file.')
    parser_extract.add_argument('--frames_dir', type=str, required=True, help='Directory to save extracted frames.')
    
    # Subparser for creating video
    parser_create = subparsers.add_parser('create', help='Create a video from frames')
    parser_create.add_argument('--frames_dir', type=str, required=True, help='Directory containing frames.')
    parser_create.add_argument('--output', type=str, required=True, help='Path to save the output video file.')
    parser_create.add_argument('--fps', type=int, default=30, help='Frames per second for the output video.')
    
    args = parser.parse_args()
    
    if args.command == 'extract':
        extract_frames(args.video, args.frames_dir)
    elif args.command == 'create':
        create_video(args.frames_dir, args.output, args.fps)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
