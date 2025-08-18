# syntax=docker/dockerfile:1.7

# Fix DS001 - specify a tag
FROM registry1.dso.mil/ironbank/redhat/ubi/ubi9:9.6 AS builder
ARG BINARY_NAME=cli_app
ENV BINARY_NAME=${BINARY_NAME}

RUN dnf -y update --security && \
    dnf -y install gcc-c++ make cmake ninja-build ca-certificates && \
    dnf clean all && \
    rm -rf /var/cache/dnf /tmp/* /var/tmp/* && \
    # Remove unnecessary setuid/setgid binaries - per IB internal docs
    find /usr/bin /usr/sbin -perm /6000 -type f -exec chmod a-s {} \; || true

WORKDIR /src
COPY CMakeLists.txt /src/
COPY cpp/ /src/cpp/
COPY thirdparty/ /src/thirdparty/
COPY service/ /src/service/

RUN cmake -S /src -B /build -G Ninja \
    -DCMAKE_BUILD_TYPE=Release && \
    cmake --build /build -j && \
    cmake --install /build --prefix /opt/app && \
    # Strip debug symbols from binaries
    strip /opt/app/bin/* && \
    # Set proper permissions
    chmod 755 /opt/app/bin/* && \
    # Clean build artifacts
    rm -rf /build /src

# Python Builder
FROM registry1.dso.mil/ironbank/redhat/ubi/ubi9:9.6 AS python-builder

RUN dnf -y install python3.11 python3.11-pip && \
    dnf clean all

WORKDIR /app
COPY service/requirements.txt .
RUN python3.11 -m pip install --no-cache-dir --target=/app/deps -r requirements.txt

COPY service/ /app/service/

# Runtime - Use python slim for easier debugging first
# Used second stage, can't build python from scratch/distroless
FROM python:3.11-slim AS runtime

# Create expected directory structure
RUN mkdir -p /app/build/bin && \
    useradd -u 65532 -m nonroot

WORKDIR /app

# Copy Python deps and service
COPY --chown=65532:65532 --from=python-builder /app/deps /app/site-packages
COPY --chown=65532:65532 service/ /app/service/

# Copy C++ binary to expected location
COPY --chown=65532:65532 --from=builder /opt/app/bin/cli_app /app/build/bin/cli_app

# Set environment variables
ENV PYTHONPATH=/app/site-packages:/app:$PYTHONPATH
ENV CLI_APP_PATH=/app/build/bin/cli_app

USER 65532
EXPOSE 8080

# Run the service
CMD ["python3", "/app/service/main.py"]