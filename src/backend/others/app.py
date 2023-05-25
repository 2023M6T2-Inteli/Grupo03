from sanic import Sanic, response

app = Sanic(__name__)


@app.route("/")
async def home(request):
    return response.text("Hello Sanic")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)