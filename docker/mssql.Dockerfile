# Use the official SQL Server 2022 image as the base image
FROM mcr.microsoft.com/mssql/server:2022-latest

# Set environment variables
ENV ACCEPT_EULA=Y
ENV MSSQL_SA_PASSWORD=YourStrong@Passw0rd
# Change to Developer/Standard/Enterprise if needed
ENV MSSQL_PID=Developer

# Expose the SQL Server port
EXPOSE 1433

# Start SQL Server when the container starts
CMD ["/opt/mssql/bin/sqlservr"]
