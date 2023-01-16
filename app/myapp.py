from flask import Response, Flask, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
import io


app = Flask(__name__)


@app.route('/plot')
def plot():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    c = float(request.args.get('c'))
    xmin = float(request.args.get('xmin'))
    xmax = float(request.args.get('xmax'))
    ymin = float(request.args.get('ymin'))
    ymax = float(request.args.get('ymax'))

    x = np.linspace(xmin, xmax, 100)
    y = a*x**2 + b*x + c

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    plt.title(f"y = {a}x^2 + {b}x + {c}")
    plt.xlabel('x')
    plt.ylabel('y')

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')