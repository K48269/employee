FROM python3.9
COPY . .
RUN pip3 install -r requirements.txt
RUN python3.5 -m easy_install pip
EXPOSE 5001
ENTRYPOINT [ "python3","app.py" ]