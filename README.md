# Endpoint in Flask, which can display the graph of the quadratic equation function

## Overview

Preparing an Endpoint in Flask that can display a graph of a quadratic function.
The endpoint takes the following parameters:
- a, b, c: equation parameters y = ax^2+ bx + c
- xmin, xmax, ymin, ymax: limit values of the graph area to be displayed

## Instructions

- Build an image
```
docker build -t my-flask-app .
```

- Run the container
```
docker run -p 5000:5000 my-flask-app
```

- Display the enpoint with sample parameters

http://localhost:5000/plot?a=3&b=0&c=0&xmin=-5&xmax=5&ymin=0&ymax=10