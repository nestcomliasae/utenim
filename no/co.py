container = client.V1Container(
    name="my-container",
    image="my-image",
    command=["my-command"],
    args=["arg1", "arg2"],
    env=[client.V1EnvVar(name="MY_ENV_VAR", value="my-value")],
    ports=[client.V1ContainerPort(container_port=8080)]
)
