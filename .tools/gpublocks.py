#!/usr/bin/env python3
"""GPU acceleration, emitted as commented YAML that stays valid when uncommented.

Convention (important):
  '#'  single hash = a real config line -> REMOVE the hash to enable
  '##' double hash = human comment (never remove)

Two parts are emitted so uncommenting never produces a duplicate mapping key:
  env_lines(gclass) -> GPU env vars, appended as items under the service's
                       existing `environment:` block (caller already emitted one)
  service_keys(gclass) -> service-level keys (devices:/runtime:/deploy.reservations)
  swarm_placement_gpu() -> swarm placement hint
  swarm_note() -> swarm deploy note

Each variant is independently uncommentable. test_gpu-style checks confirm
validity + activation.
"""
IND = "      "  # env indent in compose


def env_lines(gclass, indent=IND):
    if not gclass:
        return ""
    if gclass == "transcode":
        return (f"{indent}# - NVIDIA_DRIVER_CAPABILITIES=all\n"
                f"{indent}# - LIBVA_DRIVER_NAME=iHD            # Intel iGPU VAAPI/QSV\n"
                f"{indent}# - VAAPI_DRIVER=iHD")
    if gclass == "compute":
        return (f"{indent}# - NVIDIA_DRIVER_CAPABILITIES=all\n"
                f"{indent}# - NVIDIA_VISIBLE_DEVICES=all\n"
                f"{indent}# - ONEAPI_DEVICE_SELECTOR=*        # Intel iGPU/Arc OpenVINO\n"
                f"{indent}# - ZES_ENABLE_SYSMAN=1")
    if gclass == "passthrough":
        return (f"{indent}# - LIBVA_DRIVER_NAME=iHD\n"
                f"{indent}# - INTEL_GPU=1")
    return ""


def service_keys(gclass, indent="    "):
    if not gclass:
        return ""
    if gclass == "transcode":
        return (f"{indent}# devices:\n"
                f"{indent}#   - /dev/dri:/dev/dri\n"
                f"{indent}# group_add:\n"
                f"{indent}#   - render\n"
                f"{indent}#   - video\n"
                f"{indent}# runtime: nvidia")
    if gclass == "compute":
        return (f"{indent}# deploy:\n"
                f"{indent}#   resources:\n"
                f"{indent}#     reservations:\n"
                f"{indent}#       devices:\n"
                f"{indent}#         - driver: nvidia\n"
                f"{indent}#           count: 1\n"
                f"{indent}#           capabilities: [gpu]\n"
                f"{indent}# devices:\n"
                f"{indent}#   - /dev/dri:/dev/dri")
    if gclass == "passthrough":
        return (f"{indent}# devices:\n"
                f"{indent}#   - /dev/kvm:/dev/kvm\n"
                f"{indent}#   - /dev/dri:/dev/dri")
    return ""


def swarm_placement_gpu(indent="          "):
    return (f"{indent}# - node.role == manager\n"
            f"{indent}# GPU: add node-generic-resources to daemon.json and:\n"
            f"{indent}#   - node.labels.gpu == true")


def swarm_note(indent="      "):
    return (f"{indent}# GPU: swarm ignores `devices:`/`runtime:`. Declare in\n"
            f"{indent}#   /etc/docker/daemon.json: \"node-generic-resources\": [\"gpu=1\"]\n"
            f"{indent}#   then use deploy.resources.reservations.generic_resources.")
