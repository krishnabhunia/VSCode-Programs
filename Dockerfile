# Use the official Microsoft SQL Server image from the Docker Hub
FROM mcr.microsoft.com/mssql/server:2022-latest

# Set environment variables
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=YourStrong!Passw0rd
ENV MSSQL_PID=Express

# Expose the SQL Server port
EXPOSE 1433

# Run SQL Server process
CMD /opt/mssql/bin/sqlservr