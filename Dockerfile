FROM ubuntu:18.04

LABEL maintainer="Maksim Kalinin <maksim.kalinin.2110@gmail.com>"
LABEL repository="COVID-19-CT"
LABEL version="1.0"
LABEL description="Simple docker image for COVID-19 Computer Tomography."

RUN apt-get update && \
    apt-get install -y bash \
                   build-essential \
                   git \
                   curl \
                   ca-certificates \
                   python3.8 \
                   python3-pip \
                   python3.8-dev


# Create links
RUN ln -sf /usr/bin/python3.8 /usr/bin/python
RUN ln -sf /usr/bin/python3.8 /usr/bin/python3

RUN python3 -m pip install --no-cache-dir --upgrade pip

RUN useradd --no-user-group --create-home --shell /bin/bash covid-19
USER covid-19
WORKDIR /home/covid-19
ENV PATH="/home/covid-19/.local/bin:${PATH}"

RUN python3 -m pip install --no-cache-dir \
    jupyter \
    cython \
    jupyterlab \
    jupyter_contrib_nbextensions

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

USER root
RUN mkdir /home/covid-19/COVID-19-CT
RUN chown -R covid-19 /home/covid-19/COVID-19-CT

USER covid-19
RUN mkdir -p ~/.jupyter && echo c.NotebookApp.ip = \"0.0.0.0\" > ~/.jupyter/jupyter_notebook_config.py
WORKDIR /home/covid-19/COVID-19-CT
CMD ["jupyter-notebook"]