from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
import re

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    def get_response(self):
        path = self.url().path
        is_match = bool(re.search(r"^/(proyecto/(\d+))?$", path))
        if is_match and path in projects:
            return projects[path]
        else:
            return """
                <h1>ERROR</h1>
            """
projects = {
    "/": """
        <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Ana Lee </title>
                <link href="css/style.css" rel="stylesheet">
            </head>
            <body>
            <h1>Ana Lee </h1> 
                <h2>Desarrolladora Web (Música/Diseño/Empresaria)</h2>
                <small>Este texto fue generado por Copilot:</small>
                <h3>
                ¡Hola! Soy Ana Lee, una desarrolladora web que se especializa en la
                creación de sitios web y aplicaciones web. Me encanta trabajar con
                tecnologías web modernas y crear experiencias de usuario atractivas y
                fáciles de usar. También soy una artista y empresaria apasionada, y me
                encanta combinar mi creatividad y mi pasión por la tecnología para crear
                soluciones web únicas y efectivas. .
                </h3>
                </br>
                <h2>Proyectos</h2>
                <h3><a href="/proyecto/1"> Web Estática  - App de recomendación de libros </a></h3>
                <h3><a href="/proyecto/2"> Web App - MeFalta, que película o serie me falta ver </a></h3>
                <h3><a href="/proyecto/3"> Web App - Foto22,  web para gestión de fotos </a></h3>
                </br>
                <h2>Experiencia</h2>
                <h3>Desarrolladora Web Freelance</h3>
                <h3>Backend: FastAPI, nodejs, Go</h3>
                <h3>Frontend: JavaScript, htmx, React</h3>
            </body>
            </html>
    """,
    "/proyecto/1": """
        <!doctype html>
            <html lang="es">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <title>Ana Lee</title>
                <link href="css/style.css" rel="stylesheet" />
            </head>
            <body>
                <h1>Ana Lee</h1>
                <h2>Recomendación de libros</h2>

                <p>
                El proyecto consiste en el diseño de un sitio que muestra la informacion
                de distintos libros. La información se obtiene de una base de datos la
                cual se actualiza cada vez que se agrega un nuevo libro. Lorem ipsum dolor
                sit amet, consectetur adipiscing elit. Nulla aliquam faucibus sapien, nec
                eleifend libero pulvinar a. Donec suscipit tortor quis velit placerat, et
                finibus nibh fermentum. Cras eget nunc pretium, aliquet neque sed, porta
                ex. Sed eros nisl, ultricies sit amet nisl ut, euismod euismod ex. Cras
                ipsum enim, porttitor at pharetra non, venenatis iaculis nulla. Praesent
                vel mi non lectus ultricies accumsan eget non lectus. Pellentesque ornare
                lorem et ipsum vestibulum, et eleifend ante sollicitudin. Interdum et
                malesuada fames ac ante ipsum primis in faucibus. Vivamus congue, urna vel
                fermentum lobortis, turpis eros maximus enim, a consectetur quam augue in
                dolor.
                </p>
                <p>
                In non bibendum metus. Phasellus ac laoreet dui, nec viverra enim. Donec
                pharetra ultrices erat nec molestie. Sed interdum dignissim velit in
                consequat. Sed lectus purus, facilisis eu pharetra sit amet, vehicula in
                purus. Cras dictum arcu ante, sed sollicitudin enim interdum ut. Donec
                consectetur, velit a luctus rutrum, orci nunc interdum diam, nec cursus
                risus neque vitae arcu. Mauris est neque, vulputate id est sed, euismod
                sodales felis. Aenean ac ipsum quis lacus fermentum pharetra.
                </p>
                <h2>Tecnologías</h2>
                <ul>
                <li>HTML5</li>
                <li>CSS</li>
                <li>Redis</li>
                </ul>
            </body>
            </html>
    """,
    "/proyecto/2": """
        <h1>Proyecto 2</h1>
    """,
    "/proyecto/3": """
        <h1>Proyecto 3</h1>
    """
}


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
