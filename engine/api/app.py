"""
Connexion script. Part of the StoryTechnologies Builder project.

July 08, 2016
Brett Alistair Kromkamp (brett.kromkamp@gmail.com)
"""

import connexion


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == '__main__':
    # Run standalone gevent server (http://www.gevent.org/index.html).
    app.run(port=8080, server='gevent')
