FROM registry.cn-hangzhou.aliyuncs.com/wangye-front/front:1.0
WORKDIR /root
COPY ./* ./
CMD ["ls"]
