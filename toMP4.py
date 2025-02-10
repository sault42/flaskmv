import os
import subprocess

def convert_to_mp4(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            # 检查文件扩展名
            if filename.endswith(('.avi', '.mov', '.mkv', '.flv', '.wmv', '.rmvb', '.MP4', '.MOV', '.MKV', '.FLV', '.WMV', '.RMVB')):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(root, os.path.splitext(filename)[0] + '.mp4')
                
                # 如果目标文件已存在，跳过转换
                if os.path.exists(output_path):
                    print(f"跳过: {output_path} 已存在")
                    # os.remove(input_path)
                    continue
                
                # 使用 ffmpeg 转换视频
                result = subprocess.run(['ffmpeg', '-i', input_path, output_path], capture_output=False, text=False)
                
                # 检查转换是否成功
                if result.returncode == 0:
                    print(f"转换成功: {input_path} -> {output_path}")
                    # 删除原文件
                    os.remove(input_path)
                    print(f"已删除原文件: {input_path}")
                else:
                    print(f"转换失败: {input_path}")
                    print(f"错误信息: {result.stderr}")

if __name__ == "__main__":
    directory = './assets/videos'
    convert_to_mp4(directory)