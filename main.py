from flask import Flask, render_template, request, send_from_directory, redirect
import os


app = Flask(__name__)  

ASSETS_DIR = 'assets'
IMAGES_DIR = 'images'
VIDEOS_DIR = 'videos'
TV_DIR = 'tv'


def get_asset_images_url(images_dir):
    # 获取图片文件夹下的所有图片 /IMAGES_DIR/images_dir
    images = [os.path.join(IMAGES_DIR, images_dir, img) 
                for img in os.listdir(os.path.join(ASSETS_DIR, IMAGES_DIR, images_dir))
                if img.endswith(('.jpg', '.jpeg', '.png', '.gif', '.JPG', '.JPEG', '.PNG', '.GIF'))]
    return images


def get_asset_videos_url(videos_dir):
    # 获取图片文件夹下的所有图片 /VIDEOS_DIR/videos_dir 返回视频列表为[VIDEOS_DIR/videos/video1,  ...]
    videos = [os.path.join(VIDEOS_DIR, videos_dir, video) 
                for video in os.listdir(os.path.join(ASSETS_DIR, VIDEOS_DIR, videos_dir))
                if video.endswith(('mp4', 'mov', 'flv', 'wmv', 'rmvb', 'mkv', 
                                    'MP4', 'MOV', 'FLV', 'WMV', 'RMVB', 'MKV'))]
    return videos


def get_asset_tv_url(tv_dir):
    # 获取tv文件夹下的所有视频 /TV_DIR/tv_dir 返回视频列表为[tv1, ...]   
    tvs = [tv for tv in os.listdir(os.path.join(ASSETS_DIR, TV_DIR, tv_dir))
                if tv.endswith(('mp4', 'mov', 'flv', 'wmv', 'rmvb', 'mkv', 
                                    'MP4', 'MOV', 'FLV', 'WMV', 'RMVB', 'MKV'))]
    return tvs


@app.route('/')
def home():
    return redirect('/tv')

@app.route('/image')
def image():
    images_dir = os.path.join(ASSETS_DIR, IMAGES_DIR)
    # 获取所有子目录
    subdirectories = [d for d in os.listdir(images_dir) if os.path.isdir(os.path.join(images_dir, d))]
    # 获取每个子目录下的图片
    images_dict = {}
    for d in subdirectories:
        images_dict[d] = get_asset_images_url(os.path.join(d))
    # 按照子目录名称排序并剔除空目录
    sorted_images_dict = {k: images_dict[k] for k in sorted(images_dict.keys()) if images_dict[k]}
    return render_template('image.html', images_dir=sorted_images_dict)

@app.route('/assets/<path:filename>')
def assets(filename):
    return send_from_directory(ASSETS_DIR, filename)

@app.route('/detail_image')
def detail_image():
    image_key = request.args.get('image_key')
    images_dir = os.path.join(image_key)
    images = get_asset_images_url(images_dir)
    return render_template('detail_image.html', images=images)

@app.route('/video')
def video():
    videos_dir = os.path.join(ASSETS_DIR, VIDEOS_DIR)
    # 获取所有子目录
    subdirectories = [d for d in os.listdir(videos_dir) if os.path.isdir(os.path.join(videos_dir, d))]
    # 获取每个子目录下的视频
    videos_dict = {}
    for d in subdirectories:
        videos_dict[d] = get_asset_videos_url(os.path.join(d))
    # 按照子目录名称排序并剔除空目录
    sorted_videos_dict = {k: videos_dict[k] for k in sorted(videos_dict.keys()) if videos_dict[k]}
    return render_template('video.html', videos_dir=sorted_videos_dict)


@app.route('/detail_video')
def detail_video():
    video_key = request.args.get('video_key')
    video_dir = os.path.join(video_key)
    videos = get_asset_videos_url(video_dir)
    return render_template('detail_video.html', videos=videos)

@app.route('/tv')
def tv():
    tv_dir = os.path.join(ASSETS_DIR, TV_DIR)
    # 获取所有子目录
    subdirectories = [d for d in os.listdir(tv_dir) if os.path.isdir(os.path.join(tv_dir, d))]  
    # 获取每个子目录下的视频
    tv_dict = {}
    for d in subdirectories:
        tv_dict[d] = get_asset_tv_url(os.path.join(d))
    # 按照子目录名称排序并剔除空目录
    sorted_tv_dict = {k: tv_dict[k] for k in sorted(tv_dict.keys()) if tv_dict[k]}
    return render_template('tv.html', tv_dir=sorted_tv_dict)

@app.route('/tv/<tv_name>/<id>')
def detail_tv(tv_name, id):
    tv_src = os.path.join(TV_DIR, tv_name, id)
    tvs = get_asset_tv_url(tv_name)
    return render_template('detail_tv.html', tv_name=tv_name, tv_src=tv_src, tvs=tvs)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')