FROM python:2.7
RUN mkdir work_dir
WORKDIR work_dir
ADD ./ ./
ADD scripts /scripts
ADD data /data
ADD gess.conf /gess.conf
#EXPOSE 6900/udp
RUN apt-get update
RUN apt-get install netcat -y
#RUN pip install 
CMD ["python","/scripts/gess-main.py"]
#RUN ./gess.sh start
