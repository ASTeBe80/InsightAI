def list_available_models():
    try:
        model = genai.GenerativeModel()
        models = model.list_models()
        return [m.name for m in models]
    except Exception as e:
        return f"Error listing models: {e}"