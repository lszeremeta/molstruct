# Molstruct Dockerfile

FROM gcr.io/distroless/python3
LABEL maintainer="Łukasz Szeremeta <l.szeremeta.dev+molstruct@gmail.com>"

WORKDIR /app

# add project files (see .dockerignore)
COPY molstruct molstruct

ENTRYPOINT [ "python", "-m", "molstruct" ]