# Use the latest Ubuntu base image
FROM ubuntu:20.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages and update the repository
RUN apt-get update && apt-get upgrade && apt-get install -y wget curl gnupg2 apt-transport-https software-properties-common

# Import the public repository GPG keys
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add the Microsoft SQL Server repository (using the Ubuntu 20.04 repository)
RUN add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"

# Install SQL Server
RUN apt-get update && apt-get upgrade && apt-get install -y mssql-server

# Set environment variables for SA password and edition
ENV SA_PASSWORD=YourStrong!Passw0rd
ENV ACCEPT_EULA=Y

# Expose the SQL Server port
EXPOSE 1433

# Start SQL Server
CMD ["/opt/mssql/bin/sqlservr"]