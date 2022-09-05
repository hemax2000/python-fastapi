# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.183.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
FROM mcr.microsoft.com/vscode/devcontainers/python:dev-3.10


COPY app1/requirements.txt app1/requirements.txt
COPY app1/requirements-dev.txt app1/requirements-dev.txt

COPY app2/requirements.txt app2/requirements.txt
COPY app2/requirements-dev.txt app2/requirements-dev.txt

COPY commons/requirements.txt commons/requirements.txt
COPY commons/requirements-dev.txt commons/requirements-dev.txt

RUN pip install --no-cache-dir \
    -r commons/requirements-dev.txt \
    -r app1/requirements-dev.txt \
    -r app2/requirements-dev.txt \
    && rm -rf /tmp/pip-tmp

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1