# Use a Python 3.12 base image
FROM python:3.12-slim
LABEL "author.name"="Terry Brooks"
LABEL "author.email"="Terry.Arthur@BrooksJr.com"

# Install necessary dependencies and Doppler CLI
RUN apt-get update && apt-get install -y \
    apt-transport-https=2.6.1 \
    ca-certificates=20230311 \
    apache2-utils=2.4.61-1~deb12u1 \
    curl  \
    gnupg=2.2.40-1.1 \
    cron=3.0pl1-162 \
    libmagic1=1:5.44-3 \
    libssl-dev \
    libenchant-2-dev=2.3.3-2 \
    make=4.3-4.1 \
    git && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | gpg --dearmor -o /usr/share/keyrings/doppler-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/doppler-archive-keyring.gpg] https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && \
    apt-get -y install doppler=3.69.0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose ports
EXPOSE 7772

# Set environment variables
ARG TOKEN=${NHHC_DT}
ARG DOPPLER_PROJECT='nhhc'
ARG DOPPLER_CONFIG='prod'
ENV DOPPLER_TOKEN=${TOKEN}
ENV DOPPLER_PROJECT=${DOPPLER_PROJECT}
ENV DOPPLER_CONFIG=${DOPPLER_CONFIG}
ENV CONTAINER_PATH_EX='/src/app/'
# Create necessary groups and users
RUN groupadd --system celery && \
    useradd -g celery celery && \
    groupadd --system nhhc && \
    useradd --home-dir /src/app --no-create-home -g nhhc nhhc_app

# Copy and install requirements
COPY --chown=nhhc_app:nhhc ./requirements.txt ./requirements.txt
# Copy the application code
COPY --chown=nhhc_app:nhhc nhhc/ /src/app/
RUN touch /src/.attestation_sweeper.log && chmod 777 /src/.attestation_sweeper.log
ADD --chown=nhhc_app:nhhc ./scripts/attestation_sweeper.sh /src/attestation_sweeper.sh
RUN chmod 0777 /src/attestation_sweeper.sh
# Install application dependencies
RUN pip install -r ./requirements.txt

# Set up Doppler directory permissions
RUN mkdir -p /src/app/.doppler && \
    chown nhhc_app:nhhc /src/app/.doppler && \
    chmod 775 /src/app/.doppler

COPY --chown=nhhc_app:nhhc ./postgres_ssl.crt  /src/postgres_ssl.crt

# Set the shell to bash
SHELL ["/bin/bash", "-c"]
RUN cat <<EOF | tee /etc/crontab > /dev/null
0 23 * * sat bash /src/attestation_sweeper.sh
EOF
USER nhhc_app

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "" ]
# Command to run the Gunicorn server
ENTRYPOINT ["doppler", "run", "--"]
WORKDIR /src/app/

# CMD ["python3 -m gunicorn", "--workers=3", "--threads=2", "nhhc.wsgi:application", "-b", ":7772"]
CMD ["/bin/bash"]
