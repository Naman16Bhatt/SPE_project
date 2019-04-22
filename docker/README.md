# EECS 4415 Big Data Systems - Docker Image

This repository contains Dockerfiles for building the Docker image for the course.

### Published at

- [eecsyorku/eecs4415][1]

### Based on

- [gettyimages/spark:2.3.1-hadoop-3.0][2] ([Github repo][3]).

Added as local subtree in [upstream](upstream/) directory, via:
```
git subtree add --squash --prefix=upstream git@github.com:gettyimages/docker-spark.git 2.3.1-hadoop-3.0
```

To update:
```
git subtree pull --squash --prefix=upstream git@github.com:gettyimages/docker-spark.git 2.3.1-hadoop-3.0
```

### Contains

- [Python 3.5.3][4]
- Java JDK 8.171.11
- [Hadoop 3.0.0][5]
- [Spark 2.3.1][6]

[1]: https://hub.docker.com/r/eecsyorku/eecs4415
[2]: https://hub.docker.com/r/gettyimages/spark
[3]: https://github.com/gettyimages/docker-spark
[4]: https://docs.python.org/3.5/
[5]: https://hadoop.apache.org/docs/r3.0.0/
[6]: http://spark.apache.org/docs/2.3.1/
