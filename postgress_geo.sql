psql -v ON_ERROR_STOP=1 --username "greeetha" <<EOF
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
EOF