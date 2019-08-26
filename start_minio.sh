docker pull minio/minio
docker run -p 9000:9000 --name minio \
  -e "MINIO_ACCESS_KEY=MYACCESSKEY" \
  -e "MINIO_SECRET_KEY=MYSECRETKEY" \
  -v /mnt/data:/data \
  minio/minio server /data
