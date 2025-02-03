FROM mcr.microsoft.com/azure-functions/python:4-python3.10

WORKDIR /home/site/wwwroot
COPY . /home/site/wwwroot

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 7071
CMD ["func", "start", "--python"]
