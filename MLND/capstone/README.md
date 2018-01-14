# 机器学习（进阶）纳米学位毕业项目——猫狗大战

**注意：本项目与以下版本库不兼容，需要使用作业环境中的版本**

- matplotlib(2.1.1)


- keras(2.1.0)

## 主要文件

- report.pdf - 项目报告
- dogs_vs_cats.ipynb - 主要代码文件
- dogs_vs_cats.html - 主要代码文件 HTML 格式
- abnormal.ipynb - 检测异常值的代码
- abnormal.html - 检测异常值代码的 HTML 格式
- image.py - 自定义类
- feature_*.h5 - 预训练特征向量
- vgg16.h5 - 对训练数据集进行分类的结果
- pred*.csv - 模型预测结果

## 文件下载

- [feature_resnet50.h5](https://www.dropbox.com/s/hm9v5poyir55wzm/feature_resnet50.h5?dl=0)  
- [feature_inceptionv3.h5](https://www.dropbox.com/s/pqz5sitxgzbh1ql/feature_inceptionv3.h5?dl=0)


- [feature_xception.h5](https://www.dropbox.com/s/c1s5psjoha5m8at/feature_xception.h5?dl=0)

## 作业环境

- ubuntu(16.04)
- CUDA(8)
- cuDNN(6)
- tensorflow-gpu(1.4.1)
- h5py(2.7.1)
- matplotlib(2.0.2)
- keras(2.0.8)
- numpy(1.13.3)
- pandas(0.21.1)
- pillow(4.3.0)
- sklearn(0.19.1)
- seaboard(0.8.1)

## 运行时间

在 AWS p2.xlarge 主机上约 30 分钟

## 参考资料

1. [深度学习，维基百科](https://zh.wikipedia.org/zh-hans/%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0)
2. [人工神经网络，维基百科](https://zh.wikipedia.org/zh-hans/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)
3. [卷积神经网络，维基百科](https://zh.wikipedia.org/zh-hans/卷积神经网络)
4. [TensorFlow 中文社区](http://www.tensorfly.cn/)
5. [Keras Documentation](https://keras.io/)
6. [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
7. [Rethinking the Inception Architecture for Computer Vision](https://arxiv.org/abs/1512.00567)
8. [Xception: Deep Learning with Depthwise Separable Convolutions](https://arxiv.org/abs/1610.02357)
9. [猫狗大战，杨培文](https://github.com/ypwhs/dogs_vs_cats)
