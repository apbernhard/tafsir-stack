CREATE USER superset;
CREATE DATABASE superset;
GRANT ALL PRIVILEGES ON DATABASE superset TO superset;
ALTER USER superset with PASSWORD 'superset';