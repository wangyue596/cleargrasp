import cv2
import numpy as np
import OpenEXR
import Imath

def png_to_exr(png_path, exr_path):
    # 读取PNG深度图像
    depth_png = cv2.imread(png_path, cv2.IMREAD_UNCHANGED)
    if depth_png is None:
        raise FileNotFoundError(f"无法读取文件: {png_path}")

    # 检查深度图像是否为16位或32位
    if depth_png.dtype != np.uint16 and depth_png.dtype != np.float32:
        raise ValueError("深度图像必须为16位（uint16）或32位（float32）")

    # 将16位深度图像转换为32位浮点数（如果必要）
    if depth_png.dtype == np.uint16:
        depth_png = depth_png.astype(np.float32)
        depth_png /= 1000.0  # 假设深度以毫米为单位，转换为米

    # 创建EXR文件
    header = OpenEXR.Header(depth_png.shape[1], depth_png.shape[0])
    half_chan = Imath.Channel(Imath.PixelType(Imath.PixelType.FLOAT))
    header['channels'] = {'R': half_chan}

    exr = OpenEXR.OutputFile(exr_path, header)
    exr.writePixels({'R': depth_png.tobytes()})
    exr.close()

# 示例用法
png_path = 'depth.png'
exr_path = 'depth.exr'
png_to_exr(png_path, exr_path)

