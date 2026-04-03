from flask import Flask, request, jsonify, render_template
from modelos.lead import Lead
from dados.banco import lista_leads, hash_leads, arvore_leads
from servicos.verificador_duplicidade import verificar_duplicidade_recursivo
from servicos.agendador import melhor_agendamento

app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return render_template("index.html")


@app.route("/teste")
def teste():
    return "OK"


@app.route("/adicionar_lead", methods=["POST"])
def adicionar_lead():
    dados = request.json

    novo_lead = Lead(
        dados["nome"],
        dados["telefone"],
        dados["email"],
        dados["cpf"]
    )

    if verificar_duplicidade_recursivo(lista_leads, novo_lead):
        return jsonify({"erro": "Lead duplicado"}), 400

    lista_leads.append(novo_lead)
    hash_leads[novo_lead.cpf] = novo_lead
    arvore_leads.inserir(novo_lead)

    return jsonify({"mensagem": "Lead cadastrado com sucesso"})


@app.route("/buscar/<cpf>")
def buscar(cpf):
    lead = hash_leads.get(cpf)

    if not lead:
        return jsonify({"erro": "Não encontrado"}), 404

    return jsonify(vars(lead))


@app.route("/agendar", methods=["POST"])
def agendar():
    intervalos = request.json["intervalos"]

    intervalos.sort(key=lambda x: x[0])

    resultado = melhor_agendamento(intervalos)

    return jsonify({"max_consultas": resultado})


if __name__ == "__main__":
    print("🚀 Servidor iniciando...")
    app.run(debug=True, host="127.0.0.1", port=5000)