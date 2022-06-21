docker run -d \
  -v /Users/piotr/Projects/key.json:/config \
  -p 127.0.0.1:1433:1433 \
  gcr.io/cloudsql-docker/gce-proxy /cloud_sql_proxy \
  -instances=gcp-dev-dev-4zet:europe-central2:main-instance=tcp:0.0.0.0:1433 -credential_file=/config