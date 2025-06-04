from text2three.registry import get_model

if __name__ == "__main__":
    model = get_model("point_e")
    model.generate("a floating sci-fi orb")