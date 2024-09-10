from utils import read_video, save_video

def main():
    video_path = r'input_videos\08fd33_4.mp4'
    save_path = 'output_videos'
    
    # Read video
    video_frames = read_video(video_path)

    # Save video
    save_video(video_frames, save_path + "/output_video.mp4")

    print('video salvo')

if __name__ == '__main__':
    main()