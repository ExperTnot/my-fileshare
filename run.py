import subprocess
import time

def check_stream(url):
    """Check if the stream is online."""
    result = subprocess.run(['streamlink', url, 'best', '--quiet'], capture_output=True, text=True)
    if 'No playable streams found on this URL' in result.stderr:
        return False
    return True

def record_stream(url, output_path):
    """Record the stream."""
    command = [
        'streamlink',
        url,
        'best',
        '-o', output_path
    ]
    return subprocess.Popen(command)

def main():
    stream_url = 'kick.com/kittyflutevt'
    output_template = '/mnt/hd1/VODs/processed/kittyflutevt-kick/{time:%Y-%m-%d}-{title}.ts'
    
    while True:
        if check_stream(stream_url):
            process = record_stream(stream_url, output_template)
            process.wait()  # Wait for the recording process to complete
        time.sleep(15)  # Wait for 15 seconds before checking again

if __name__ == '__main__':
    main()
