FROM hkarhani/ibfsta:latest
MAINTAINER Hassan El Karhani <hkarhani@gmail.com>

WORKDIR /notebooks
COPY *.py /notebooks/
COPY *.ipynb /notebooks/

EXPOSE 8888

CMD /bin/sh -c "/usr/bin/jupyter notebook --allow-root"
