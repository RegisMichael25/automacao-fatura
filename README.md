Processador de Dados Financeiros

Este projeto consiste em um script Python para processar, estruturar e exportar dados de transações financeiras a partir de um texto não estruturado para planilhas nos formatos ODS e XLSX.

🎯 Objetivo do Projeto

O objetivo principal é automatizar a extração de informações de gastos (data, descrição e valor) de um texto simples, convertê-las em um formato tabular organizado e exportá-las para arquivos de planilha, facilitando a análise e o controle financeiro.

✨ Funcionalidades

    Extração de Dados: Utiliza expressões regulares (RegEx) para identificar e extrair data, descrição e valor de cada transação no texto de entrada.

    Processamento e Estruturação: Converte os dados extraídos em um formato estruturado, utilizando a biblioteca Pandas para criar um DataFrame. As datas são padronizadas e os valores são convertidos para o tipo numérico (float).

    Exportação Flexível: Exporta os dados processados para dois formatos de planilha populares:

        .xlsx (formato padrão do Microsoft Excel)

        .ods (formato OpenDocument, compatível com LibreOffice Calc e outras suítes de escritório)

🔧 Tecnologias e Bibliotecas Utilizadas

    Python: A linguagem de programação principal.

    Pandas: Biblioteca utilizada para manipulação e análise de dados, essencial para a criação do DataFrame e exportação para planilhas.

    re: Módulo de expressões regulares do Python, usado para o parsing do texto de entrada.

    datetime: Módulo para manipulação de datas, usado para obter o ano atual.

    openpyxl: Engine para a escrita de arquivos .xlsx.

    odfpy: Engine para a escrita de arquivos .ods.

⚙️ Pré-requisitos

Antes de executar o script, você precisa ter o Python instalado em seu sistema. Além disso, as bibliotecas necessárias devem ser instaladas. Você pode instalá-las usando pip:
Bash

pip install pandas openpyxl odfpy

▶️ Como Usar

    Clone o repositório ou salve o script em um arquivo, por exemplo, processador.py.

    Abra o script em um editor de código e, se desejar, substitua o conteúdo da variável dados_texto pelos seus próprios dados, mantendo o mesmo padrão.

    Altere o caminho de exportação na variável caminho_completo para o diretório e nome de arquivo desejado:
    Python

caminho_completo = '/seu/caminho/para/dados_financeiros'

Execute o script a partir do seu terminal:
Bash

    python processador.py

    Verifique a saída: Após a execução, dois arquivos serão gerados no caminho especificado: dados_financeiros.ods e dados_financeiros.xlsx, contendo as transações organizadas.

📄 Estrutura do Código

O script é dividido nas seguintes partes:

    Importação das Bibliotecas: Importa pandas, re e datetime.

    Dados de Entrada: A variável dados_texto contém a string multilinhas com os dados brutos das transações.

    Função processar_dados_financeiros:

        Define um padrão de expressão regular para encontrar as transações.

        Itera sobre as correspondências encontradas.

        Formata a data para o padrão DD/MM/AAAA.

        Converte o valor de string para float.

        Retorna uma lista de dicionários, onde cada dicionário representa uma transação.

    Execução Principal:

        Chama a função processar_dados_financeiros para obter a lista de dados.

        Cria um DataFrame do Pandas a partir da lista.

        Converte a coluna de data do DataFrame para o tipo datetime.

    Exportação dos Dados:

        Utiliza pd.ExcelWriter para salvar o DataFrame em arquivos .ods e .xlsx, selecionando as colunas relevantes.

🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões para melhorar este script, sinta-se à vontade para abrir uma issue ou enviar um pull request.
