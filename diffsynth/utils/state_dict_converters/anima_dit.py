def AnimaDiTStateDictConverter(state_dict):
    new_state_dict = {}
    for key in state_dict:
        value = state_dict[key]

        if key.startswith("net."):
            key = key[len("net."):]
        elif key.startswith("model.diffusion_model."):
            key = key[len("model.diffusion_model."):]

        new_state_dict[key] = value

    return new_state_dict
