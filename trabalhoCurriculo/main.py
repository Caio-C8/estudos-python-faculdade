from pathlib import Path
import os
import requests


def criaCurriculo(num_curriculo):
    # Abre o aqrquivo na variável 'arquivo_curriculo' com o with open.
    # No final do bloco do with o arquivo será fechado, mesmo que ocorra algum erro, sem a necessidade do close().
    with open(
        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
    ) as arquivo_curriculo:
        arquivo_curriculo.write(
            """
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Currículo</title>
                <link rel="stylesheet" href="style.css" type="text/css" />
            </head>

            <body>
                <main class="curriculo">
                <section class="cabecalho">
                    <div class="foto"></div>
                    <div class="informacoes">
                    <h3>Data de nascimento:</h3>
                    <div>
                        <h3>Endereço:</h3>
                    </div>
                    <h3>Telefone:</h3>
                    <h3>E-mail:</h3>
                    </div>
                </section>
                <section class="curriculo-body">
                    <div>
                    <h1>Formação Acadêmica:</h1>
                    </div>
                    <div>
                    <h1>Experiência:</h1>
                    </div>
                    <div>
                    <h1>Idiomas:</h1>
                    </div>
                    <div>
                    <h1>Cursos:</h1>
                    </div>
                </section>
                </main>
            </body>
            </html>
            """
        )


def criaStyle():
    with open("C:style.css", "w") as style_arquivo:
        style_arquivo.write(
            """
            @import url("https://fonts.googleapis.com/css2?family=Agdasima:wght@400;700&display=swap");

            * {
            margin: 0;
            font-family: "Agdasima", sans-serif, monospace;
            }

            body {
            display: flex;
            height: auto;
            justify-content: center;
            align-items: center;
            margin: 2rem;
            background-color: #e7e7e7;
            }

            p {
            font-size: 1.5rem;
            color: #333;
            font-weight: bold;
            line-height: 2.2rem;
            margin: 0.5rem 0;
            text-align: justify;
            }

            h1 {
            font-size: 2.3rem;
            color: #008080;
            font-weight: bold;
            }

            h3 {
            display: flex;
            font-size: 1.9rem;
            color: #708090;
            font-weight: bold;
            gap: 0.5rem;
            }

            h3 p {
            margin: 0;
            }

            .curriculo {
            max-height: auto;
            max-width: 60rem;
            border: 0.125rem solid #000;
            border-radius: 1rem;
            padding: 1rem;
            background-color: #fffafa;
            }

            .cabecalho {
            display: flex;
            gap: 2rem;
            }

            .foto {
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0.5rem;
            }

            .img {
            height: 20rem;
            width: 20rem;
            border: 0.125rem solid #000;
            border-radius: 1rem;
            }

            .informacoes {
            display: flex;
            flex-direction: column;
            justify-content: space-evenly;
            }

            .informacoes div p {
            text-indent: 2rem;
            }

            .curriculo-body {
            display: flex;
            flex-direction: column;
            margin: 1.5rem 0 0 0.5rem;
            gap: 1rem;
            }

            .curriculo-body p {
            text-indent: 2rem;
            }

            .curriculo-body div p {
            text-align: justify;
            }

            .curriculo-body div h3 {
            text-indent: 1rem;
            }
            """
        )


# Cria o diretório e os arquivos de imagens caso ele não exista.
def criaImg():
    Path("img").mkdir()

    urls = [
        "https://i.pinimg.com/736x/98/70/5a/98705af86e49726241b221877636e756.jpg",
        "https://i.pinimg.com/564x/98/2d/21/982d21c56d4c713f723ed895a7c9a570.jpg",
        "https://i.pinimg.com/564x/64/4f/de/644fde0dcf936aaf29dd1aab6ad00185.jpg",
        "https://i.imgflip.com/7etzd2.jpg",
        "https://i.pinimg.com/736x/8c/b2/bf/8cb2bf0306bf1650ddf37ebe4d993aaa.jpg",
        "https://i.pinimg.com/564x/58/48/bb/5848bb576d69654df4199d76fc7e3827.jpg",
        "https://i.pinimg.com/736x/52/94/51/52945151cd70d90df6fbef8d56ba7865.jpg",
        "https://i.pinimg.com/736x/e6/2a/a1/e62aa16bec853fdd71fd54e0ab315d13.jpg",
        "https://i.pinimg.com/564x/ae/59/cf/ae59cfb3afd5c3426bd270588334096c.jpg",
        "https://i.pinimg.com/736x/5a/6e/78/5a6e782d4e9d78ade6450cd88e222d6e.jpg",
    ]

    nomes = [
        "cabelo_regua.jpg",
        "cachorro_terno.jpg",
        "cr7_bigode.jpg",
        "fofo.jpg",
        "inteligente.jpg",
        "joinha.jpg",
        "leon_trono.jpg",
        "selfie.jpg",  #
        "sem_imagem.jpg",
        "sorriso_sutil.jpg",
    ]

    for url, nome_imagem in zip(urls, nomes):
        # Vai criar o diretório até o arquivo .jpg na ordem.
        imagem = os.path.join("img", nome_imagem)
        # Faz a requisição para baixar a imagem da URL e armazena o conteúdo binário da imagem.
        img = requests.get(url)

        # Verifica se a imagem foi baixada corretamente (código 200 significa sucesso).
        if img.status_code == 200:
            # Abre (ou cria) o arquivo no modo 'wb' ("write binary") para escrever os dados binários da imagem.
            with open(imagem, "wb") as arquivo_imagem:
                # Vai escrever no arquivo o conteúdo da variável img, que é o conteúdo binário da imagem.
                arquivo_imagem.write(img.content)
        else:
            print(f"Falha ao baixar {nome_imagem}")


# Vai solicitar os dados e dar a opção de reescrevê-los caso ocorra algum erro de digitação.
def solicitarDado(campo):
    while True:
        dado = input(f"\nDigite {campo}").strip()

        while True:
            confirmacao = (
                input(f'Você inseriu "{dado}". Deseja reescrever este campo (S/N): ')
                .strip()
                .lower()
            )

            if confirmacao == "s":
                print(f"Reescreva o campo novamente.")
                break
            elif confirmacao == "n":
                return dado
            else:
                print("\nOpção inválida.\n")


def gravaInfo(num_curriculo):
    print("\nComeçe pelas informações básicas.")
    nome = solicitarDado("seu nome: ")
    dataNascimento = solicitarDado("sua data de nascimento no formato DD/MM/AAAA: ")
    tel = solicitarDado("seu telefone no formato (XX) XXXXX-XXXX: ")
    email = solicitarDado("seu e-mail: ")

    print("\nAgora Preencha as informações referentes ao endereço.")
    rua = solicitarDado("a rua: ")
    numero = solicitarDado("o número: ")
    cidade = solicitarDado("a cidade: ")
    estado = solicitarDado("o estado: ")

    with open(
        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
    ) as arquivo_curriculo:
        linhas_curriculo = arquivo_curriculo.readlines()

    # No for, será verificado se existe o conteúdo "<div class=\"informacoes\">" em cada linha de linhas_curriculo.
    # O i representa o índice da linha, e linha é o conteúdo da linha e o enumerate vai permitir obter o índice e o conteúdo de cada linha em linhas_curriculo.
    # O linha_nome será incrementado para que o conteúdo seja gravado uma linha após o conteúdo.
    for i, linha in enumerate(linhas_curriculo):
        if '<div class="informacoes">' in linha:
            linha_nome = i + 1
            break
    # O insert vai inserir uma linha ao invés de sobrescrever uma linha.
    linhas_curriculo.insert(linha_nome, f"                <h1>{nome}</h1>\n")

    for i, linha in enumerate(linhas_curriculo):
        if "Data de nascimento:" in linha:
            linha_data = i + 1
            break
    linhas_curriculo.insert(
        linha_data, f"                    <p>{dataNascimento}</p>\n"
    )

    for i, linha in enumerate(linhas_curriculo):
        if "<h3>Endereço:</h3>" in linha:
            linha_endereco = i + 1
            break
    linhas_curriculo.insert(
        linha_endereco, f"                    <p>{rua}, {numero}</p>\n"
    )
    linhas_curriculo.insert(
        linha_endereco + 1, f"                    <p>{estado}, {cidade}</p>\n"
    )

    for i, linha in enumerate(linhas_curriculo):
        if "Telefone:" in linha:
            linha_tel = i + 1
            break
    linhas_curriculo.insert(linha_tel, f"                    <p>{tel}</p>\n")

    for i, linha in enumerate(linhas_curriculo):
        if "E-mail:" in linha:
            linha_email = i + 1
            break
    linhas_curriculo.insert(linha_email, f"                    <p>{email}</p>\n")

    with open(
        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
    ) as arquivo_curriculo:
        arquivo_curriculo.writelines(linhas_curriculo)

    print("\nINFORMAÇÕES BÁSICAS SALVAS COM SUCESSO!")


def gravaFormacao(num_curriculo):
    print("\nAgora você deve preencher informações sobre sua formação acadêmica.\n")
    # Cria uma lista vazia.
    formacoes = []

    while True:
        formacao = (
            input("Você deseja preencher a parte de formações acadêmicas (S/N): ")
            .strip()
            .lower()
        )
        if formacao == "s":
            while True:
                graduacao = solicitarDado("sua graduação: ")
                graduacao_tipo = solicitarDado("o tipo da sua graduação: ")
                local_graduacao = solicitarDado("o local da sua graduação: ")
                data_conclusao = solicitarDado(
                    "a data de conclusão da graduação no formato MM/AAAA: "
                )

                # Cria um dicionário que vai armazenar pares de chave-valor.
                # Por exemplo, o valor graduacao vai ser armazenado na chave 'graduacao'.
                # No final esse dicionário vai ser adicionado na lista, assim cada dicionário vai ser armazenado em uma posição da lista.
                formacao_academica = {
                    "graduacao": graduacao,
                    "tipo": graduacao_tipo,
                    "local": local_graduacao,
                    "conclusao": data_conclusao,
                }
                formacoes.append(formacao_academica)

                while True:
                    adicionar_graduacao = (
                        input("\nDeseja adicionar outras graduações (S/N): ")
                        .strip()
                        .lower()
                    )
                    if adicionar_graduacao == "n":
                        break
                    elif adicionar_graduacao == "s":
                        break
                    else:
                        print("\nOpção inválida.")

                if adicionar_graduacao == "n":
                    with open(
                        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
                    ) as arquivo_curriculo:
                        linhas_curriculo = arquivo_curriculo.readlines()

                    for i, linha in enumerate(linhas_curriculo):
                        if "<h1>Formação Acadêmica:</h1>" in linha:
                            linha_formacao = i + 1
                            break

                    # Cria um laço de repetição que vai gravar as informações requisitadas do dicionário.
                    # A formacaoAcademica seria a posição onde o dicionário está na lista.
                    # No fim o linha_formacao vai aumentar para, caso tenha mais dicionários, gravar em outras linhas o restante do conteúdo.
                    for formacao_academica in formacoes:
                        linhas_curriculo.insert(
                            linha_formacao,
                            f"                <p>Graduação: {formacao_academica['graduacao']} | Tipo de graduação: {formacao_academica['tipo']} | Local da graduação: {formacao_academica['local']} | Data de conclusão: {formacao_academica['conclusao']}</p>\n",
                        )
                        linha_formacao += 1

                    with open(
                        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
                    ) as arquivo_curriculo:
                        arquivo_curriculo.writelines(linhas_curriculo)

                    print(
                        '\nINFORMAÇÕES SOBRE "Formações Acadêmicas" SALVAS COM SUCESSO!'
                    )

                    break
        elif formacao == "n":
            with open(
                f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
            ) as arquivo_curriculo:
                linhas_curriculo = arquivo_curriculo.readlines()

            for i, linha in enumerate(linhas_curriculo):
                if "<h1>Formação Acadêmica:</h1>" in linha:
                    linha_formacao = i + 1
                    break
            linhas_curriculo.insert(
                linha_formacao, "                <p>Sem formações acadêmicas.</p>\n"
            )

            with open(
                f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
            ) as arquivo_curriculo:
                arquivo_curriculo.writelines(linhas_curriculo)

            break
        else:
            print("\nOpção inválida.\n")
            adicionar_graduacao = ""

        if adicionar_graduacao == "n":
            break


def gravaExperiencia(num_curriculo):
    print("\nAgora você deve preencher informações sobre sua experiência.\n")
    experiencias = []

    while True:
        experiencia = (
            input("Você deseja preencher a parte de experiências (S/N): ")
            .strip()
            .lower()
        )
        if experiencia == "s":
            while True:
                cargo = solicitarDado("o cargo: ")
                periodo_cargo = solicitarDado(
                    "o período de permanência no cargo no formato MM/AAAA - MM/AAAA: "
                )
                empresa = solicitarDado("em qual empresa você exerceu seu cargo: ")
                descricao = solicitarDado("uma breve descrição das tarefas exercidas: ")

                cargos_experiencias = {
                    "cargo": cargo,
                    "periodo": periodo_cargo,
                    "empresa": empresa,
                    "descricao": descricao,
                }
                experiencias.append(cargos_experiencias)

                while True:
                    adicionar_experiencia = (
                        input("\nDeseja adicionar outras experiências (S/N): ")
                        .strip()
                        .lower()
                    )
                    if adicionar_experiencia == "n":
                        break
                    elif adicionar_experiencia == "s":
                        break
                    else:
                        print("\nOpção inválida.")

                if adicionar_experiencia == "n":
                    with open(
                        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
                    ) as arquivo_curriculo:
                        linhas_curriculo = arquivo_curriculo.readlines()

                    for i, linha in enumerate(linhas_curriculo):
                        if "<h1>Experiência:</h1>" in linha:
                            linha_experiencia = i + 1
                            break

                    for experiencia in experiencias:
                        linhas_curriculo.insert(
                            linha_experiencia,
                            f"                <h3>{experiencia['empresa']}</h3>\n",
                        )
                        linhas_curriculo.insert(
                            linha_experiencia + 1,
                            f"                <p>Cargo: {experiencia['cargo']} | Período do cargo: {experiencia['periodo']}</p>\n",
                        )
                        linhas_curriculo.insert(
                            linha_experiencia + 2,
                            f"                <p>{experiencia['descricao']}</p>\n",
                        )
                        linha_experiencia += 3

                    with open(
                        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
                    ) as arquivo_curriculo:
                        arquivo_curriculo.writelines(linhas_curriculo)

                    print('\nINFORMAÇÕES SOBRE "Experiências" SALVAS COM SUCESSO!')

                    break
        elif experiencia == "n":
            with open(
                f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
            ) as arquivo_curriculo:
                linhas_curriculo = arquivo_curriculo.readlines()

            for i, linha in enumerate(linhas_curriculo):
                if "<h1>Experiência:</h1>" in linha:
                    linha_experiencia = i + 1
                    break
            linhas_curriculo.insert(
                linha_experiencia,
                "                <p>Sem experiências profissionais.</p>\n",
            )

            with open(
                f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
            ) as arquivo_curriculo:
                arquivo_curriculo.writelines(linhas_curriculo)

            break
        else:
            print("\nOpção inválida.\n")
            adicionar_experiencia = ""

        if adicionar_experiencia == "n":
            break


def gravaIdioma(num_curriculo):
    print(
        "\nAgora você deve preencher informações sobre idiomas que você tenha proeficiência.\n"
    )
    idiomas = []

    while True:
        idioma_pergunta = (
            input("Você deseja preencher a parte de idiomas (S/N): ").strip().lower()
        )
        if idioma_pergunta == "s":
            while True:
                lingua = solicitarDado("o idioma: ")
                nivel = solicitarDado("seu nível de proeficiência no idioma: ")

                idiomas_falados = {"lingua": lingua, "nivel": nivel}
                idiomas.append(idiomas_falados)

                while True:
                    adicionar_idioma = (
                        input("\nDeseja adicionar outros idiomas (S/N): ")
                        .strip()
                        .lower()
                    )
                    if adicionar_idioma == "n":
                        break
                    elif adicionar_idioma == "s":
                        break
                    else:
                        print("\nOpção inválida.")

                if adicionar_idioma == "n":
                    with open(
                        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
                    ) as arquivo_curriculo:
                        linhas_curriculo = arquivo_curriculo.readlines()

                    for i, linha in enumerate(linhas_curriculo):
                        if "<h1>Idiomas:</h1>" in linha:
                            linha_idioma = i + 1
                            break

                    for idioma in idiomas:
                        linhas_curriculo.insert(
                            linha_idioma,
                            f"                <p>{idioma['lingua']} | {idioma['nivel']}</p>\n",
                        )
                        linha_idioma += 1

                    with open(
                        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
                    ) as arquivo_curriculo:
                        arquivo_curriculo.writelines(linhas_curriculo)

                    print('\nINFORMAÇÕES SOBRE "Idiomas" SALVAS COM SUCESSO!')

                    break
        elif idioma_pergunta == "n":
            with open(
                f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
            ) as arquivo_curriculo:
                linhas_curriculo = arquivo_curriculo.readlines()

            for i, linha in enumerate(linhas_curriculo):
                if "<h1>Idiomas:</h1>" in linha:
                    linha_idioma = i + 1
                    break
            linhas_curriculo.insert(
                linha_idioma,
                "                <p>Sem proeficiência em outros idiomas.</p>\n",
            )

            with open(
                f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
            ) as arquivo_curriculo:
                arquivo_curriculo.writelines(linhas_curriculo)

            break
        else:
            print("\nOpção inválida.\n")
            adicionar_idioma = ""

        if adicionar_idioma == "n":
            break


def gravaCurso(num_curriculo):
    print(
        "\nAgora você deve preencher informações sobre cursos que você fez ou está fazendo.\n"
    )
    cursos = []

    while True:
        curso_pergunta = (
            input("Você deseja preencher a parte de cursos (S/N): ").strip().lower()
        )
        if curso_pergunta == "s":
            while True:
                nome_curso = solicitarDado("o nome do curso: ")
                instituicao = solicitarDado("o nome da instituição: ")

                cursos_feitos = {"nome": nome_curso, "lugar": instituicao}
                cursos.append(cursos_feitos)

                while True:
                    adicionar_curso = (
                        input("\nDeseja adicionar outros cursos (S/N): ")
                        .strip()
                        .lower()
                    )
                    if adicionar_curso == "n":
                        break
                    elif adicionar_curso == "s":
                        break
                    else:
                        print("\nOpção inválida.")

                if adicionar_curso == "n":
                    with open(
                        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
                    ) as arquivo_curriculo:
                        linhas_curriculo = arquivo_curriculo.readlines()

                    for i, linha in enumerate(linhas_curriculo):
                        if "<h1>Cursos:</h1>" in linha:
                            linha_curso = i + 1
                            break

                    for curso in cursos:
                        linhas_curriculo.insert(
                            linha_curso,
                            f"                <p>{curso['nome']} | {curso['lugar']}</p>\n",
                        )
                        linha_curso += 1

                    with open(
                        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
                    ) as arquivo_curriculo:
                        arquivo_curriculo.writelines(linhas_curriculo)

                    print('\nINFORMAÇÕES SOBRE "Cursos" SALVAS COM SUCESSO!')

                    break
        elif curso_pergunta == "n":
            with open(
                f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
            ) as arquivo_curriculo:
                linhas_curriculo = arquivo_curriculo.readlines()

            for i, linha in enumerate(linhas_curriculo):
                if "<h1>Cursos:</h1>" in linha:
                    linha_curso = i + 1
                    break
            linhas_curriculo.insert(
                linha_curso, "                <p>Sem cursos realizados.</p>\n"
            )

            with open(
                f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
            ) as arquivo_curriculo:
                arquivo_curriculo.writelines(linhas_curriculo)

            break
        else:
            print("\nOpção inválida.\n")
            adicionar_curso = ""

        if adicionar_curso == "n":
            break


def escolheImagem(num_curriculo):
    print("\nAgora escolha uma imagem que terá em seu currículo.\n")
    print("1 - Fazendo um joia.")
    print("2 - Usando um terno.")
    print("3 - Sentado.")
    print("4 - Com bigode.")
    print("5 - Com o cabelo bacana.")
    print("6 - Selfie básica.")
    print("7 - Mostrando os músculos.")
    print("8 - Sorrindo sutilmente.")
    print("9 - Com aparência de inteligente.")
    print("10 - Sem foto.")

    with open(
        f"C:curriculo{num_curriculo}.html", "r", encoding="utf-8"
    ) as arquivo_curriculo:
        linhas_curriculo = arquivo_curriculo.readlines()

    for i, linha in enumerate(linhas_curriculo):
        if '<div class="foto">' in linha:
            linha_img = i + 1
            break

    while True:
        escolha = solicitarDado("o número da imagem que terá em seu currículo: ")

        if escolha == "1":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/joinha.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "2":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/cachorro_terno.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "3":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/leon_trono.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "4":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/cr7_bigode.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "5":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/cabelo_regua.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "6":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/selfie.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "7":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/fofo.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "8":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/sorriso_sutil.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "9":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/inteligente.jpg" alt="Foto do currículo">\n',
            )
            break
        elif escolha == "10":
            linhas_curriculo.insert(
                linha_img,
                f'                <img class="img" src="img/sem_imagem.jpg" alt="Foto do currículo">\n',
            )
            break
        else:
            print("\nOpção inválida.")

    with open(
        f"C:curriculo{num_curriculo}.html", "w", encoding="utf-8"
    ) as arquivo_curriculo:
        arquivo_curriculo.writelines(linhas_curriculo)

    print("\nIMAGEM SALVA COM SUCESSO!\n")


# Vai permitir que mais de um currículo seja criado.
def controleCurriculo(criar_curriculo, num_curriculo):
    if criar_curriculo == "s":
        if num_curriculo >= 1:
            num_curriculo += 1
            return num_curriculo
    else:
        num_curriculo = 1
        return num_curriculo


def principal(criar_curriculo, num_curriculo):
    # Cria um loop infinito que vai se repetir até que um comando interrompa o loop, no caso aqui é o break.
    while True:
        num_curriculo = controleCurriculo(criar_curriculo, num_curriculo)
        # Com o uso da biblioteca pathlib e com o objeto Path, vai ser criado uma variavél que vai receber o caminho do arquivo style.css.
        arquivo_style = Path("style.css")
        diretorio_img = Path("img")

        # Aqui vai ser comparado se o arquivo existe. Caso não exista, ele será criado.
        while True:
            if not arquivo_style.is_file():
                criaStyle()
                break
            else:
                break

        while True:
            if not diretorio_img.is_dir():
                criaImg()
                break
            else:
                break

        criaCurriculo(num_curriculo)
        gravaInfo(num_curriculo)
        gravaFormacao(num_curriculo)
        gravaExperiencia(num_curriculo)
        gravaIdioma(num_curriculo)
        gravaCurso(num_curriculo)
        escolheImagem(num_curriculo)

        while True:
            criar_curriculo = (
                input("Você quer criar outro currículo (S/N): ").strip().lower()
            )
            if criar_curriculo == "s":
                break
            elif criar_curriculo == "n":
                break
            else:
                print("Opção inválida")

        if criar_curriculo == "n":
            break

    return num_curriculo


# ----------Programa Principal----------#
print("Bem-vindo(a) ao gerador de currículos.")
print(f"\n{principal('', 0)} currículo(s) criado(s) com sucesso!")
