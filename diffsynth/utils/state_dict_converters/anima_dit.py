def AnimaDiTStateDictConverter(state_dict):
    new_state_dict = {}

    for key, value in state_dict.items():

        if key.startswith("net."):
            key = key.replace("net.", "", 1)

        elif key.startswith("model.diffusion_model."):
            key = key.replace("model.diffusion_model.", "", 1)

        new_state_dict[key] = value

    return new_state_dict
