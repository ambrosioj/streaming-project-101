FROM bitnami/spark:3.5.1 as jupyter-local

# Switch to root for setup
USER root

# Set up a writable home directory for Jupyter
ENV HOME=/home/jupyter
RUN mkdir -p $HOME && \
    chmod -R 777 $HOME

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Set working directory and permissions
WORKDIR /app
RUN chmod -R 777 /app

# Switch back to the non-root user
USER 1001

# Expose the necessary port
EXPOSE 8888
