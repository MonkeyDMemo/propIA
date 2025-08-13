import azure.functions as func

# Registrar la función
app = func.FunctionApp()

@app.function_name(name="generar_documento")
@app.route(route="generar_documento", auth_level=func.AuthLevel.ANONYMOUS)
def upload_log(req: func.HttpRequest) -> func.HttpResponse:
    import propia.de_1 as function_logic
    return function_logic.main(req)