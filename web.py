from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse


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
        path_elements = ": ".join(self.url().path.split("/")[1:])
        parsed_query = parse_qsl(self.url().query)
        query_elements = [_ for _ in parsed_query]
        query_text = ""
        if query_elements:
            query_text = ", ".join([f"{x}: {y}" for (x, y) in query_elements])
        return f"""
            <h1>{path_elements}, {query_text}</h1>
        """


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
