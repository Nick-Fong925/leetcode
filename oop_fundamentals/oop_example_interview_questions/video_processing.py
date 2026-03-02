"""
VIDEO PROCESSING INTERVIEW QUESTION - APPROACH GUIDE
=====================================================

PROBLEM STATEMENT (What we know):
We are GIVEN a list of videos upfront
We DON'T know the lengths initially - must call video.get_length() for each
We have a TIME BUDGET (e.g., 10 minutes total processing time)
GOAL: Maximize the NUMBER (count) of videos we process
Assumption: processing_time = video_length


Even with the above, you should still ask:

1. "Can I call get_length() on ALL videos before deciding which to process?" Yes which allows for sorting

2. "Does processing take exactly the same time as the video length?" -> Processing same as length

3. "Once I start processing, must I finish that video?" -> Assume that you cant cancel mid video

4. "Do all videos have equal priority?" -> no priority


"To maximize the COUNT of videos processed with limited time, I should use a 
GREEDY ALGORITHM: process the SHORTEST videos first.

Why? If I have 10 minutes:
- Process [5min, 5min] → 2 videos 
- Process [1min, 1min, 1min, 7min] → 4 videos 

By processing shorter videos first, I fit more videos into my time budget."

This is similar to the Activity Selection Problem.

Pseudo-code:

1. Get the list of all videos
2. For each video, call get_length() and store (video, length) pairs
3. Sort videos by length (ascending - shortest first)
4. Initialize: time_remaining = time_budget, processed_videos = []
5. For each video in sorted order:
   - If video.length <= time_remaining:
       - Process the video
       - Subtract video.length from time_remaining
       - Add to processed_videos
   - Else: skip (not enough time)
6. Return processed_videos or count

Time Complexity: O(n log n) - dominated by sorting
Space Complexity: O(n) - storing video-length pairs
"""

class Video:
    """Represents a video with an ID and length."""
    
    def __init__(self, video_id, length):
        self.video_id = video_id
        self._length = length
    
    def get_length(self):
        """Call this function to get the video length."""
        return self._length
    
    def process(self):
        """Simulates processing the video."""
        print(f"Processing video {self.video_id} (length: {self._length} min)")
    
    def __repr__(self):
        return f"Video({self.video_id})"


class VideoProcessor:

    
    def __init__(self, time_budget):

        self.time_budget = time_budget
    
    def process_videos(self, videos):
        video_lengths = []
        for video in videos:
            length = video.get_length()  
            video_lengths.append((video, length))
        
    
        video_lengths.sort(key=lambda x: x[1]) 
        
        processed_videos = []
        time_remaining = self.time_budget
        
        for video, length in video_lengths:
            if length <= time_remaining:
    
                video.process()
                processed_videos.append(video)
                time_remaining -= length
        
        return processed_videos


if __name__ == "__main__":

    videos = [
        Video("V1", 5),   # 5 minutes
        Video("V2", 2),   # 2 minutes
        Video("V3", 8),   # 8 minutes
        Video("V4", 1),   # 1 minute
        Video("V5", 3),   # 3 minutes
        Video("V6", 4),   # 4 minutes
    ]
    
    processor = VideoProcessor(time_budget=10)
    
    print("Videos available:", videos)
    print(f"Time budget: {processor.time_budget} minutes\n")
    
    # Process videos
    processed = processor.process_videos(videos)
    
    print(f"\n✓ Processed {len(processed)} videos: {processed}")
    print(f"Total time used: {sum(v.get_length() for v in processed)} minutes")


