from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: tarefa

tasks = []


if __name__ == '__main__':
    app.run(debug = True)