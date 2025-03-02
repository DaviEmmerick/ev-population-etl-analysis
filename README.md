# EV Population ETL

Este projeto implementa um pipeline ETL automatizado para processar dados sobre veículos elétricos. Orquestrado com Apache Airflow, o pipeline executa tarefas periodicamente à medida que novos dados são adicionados, transformando e carregando-os em um banco de dados SQL para garantir atualizações eficientes.

# Descrição

O projeto tem como objetivo a automação do processo de Extração, Transformação e Carga (ETL) de dados sobre a população de veículos elétricos. O pipeline coleta dados de um arquivo CSV, processa e limpa as informações necessárias, realiza transformações e, finalmente, carrega os dados em um banco de dados SQL. Além disso, o pipeline é orquestrado e gerido utilizando Apache Airflow, permitindo a execução automática e agendada de tarefas.

# Funcionalidades

- **Extração**: Coleta dados de um arquivo CSV contendo informações sobre veículos elétricos.
- **Transformação**: Limpeza e transformação dos dados para garantir que estejam prontos para análise.
- **Carga**: Carrega os dados transformados em um banco de dados SQL, garantindo que as informações estejam atualizadas e prontas para consultas.
- **Orquestração**: Utiliza Apache Airflow para automatizar e orquestrar o pipeline, permitindo a execução periódica e eficiente das tarefas.

# Como usar

## Pré-requisitos

- Python 3.x
- Ambiente virtual (recomendado)
- Apache Airflow
- Banco de dados SQL (por exemplo, SQLite, PostgreSQL, etc.)

## Instalação

1. Clone o repositório:

git clone https://github.com/DaviEmmerick/ev-population-etl.git 
cd ev-population-etl

2. Crie e ative o ambiente virtual:

python -m venv venv source venv/bin/activate # no Linux/macOS 
venv\Scripts\activate # no Windows

3. Instale as dependências:

pip install -r requirements.txt

4. Configure o Apache Airflow:
Se você ainda não configurou o Apache Airflow, consulte a documentação oficial (https://airflow.apache.org/docs/apache-airflow/stable/installation.html) para realizar a instalação e configuração necessárias.

5. Execute o pipeline:
Para rodar o Airflow e ver o DAG em execução, use:

airflow webserver -p 8080 airflow scheduler

# Fluxo de Trabalho do Pipeline

1. **Extração**: O arquivo CSV contendo dados sobre a população de veículos elétricos é extraído.
2. **Transformação**: Os dados extraídos são limpos e transformados para atender aos requisitos de análise.
3. **Carga**: Os dados transformados são carregados em um banco de dados SQL para posterior análise.
4. **Agendamento e Orquestração**: O pipeline é gerenciado e executado periodicamente pelo Apache Airflow.

# Arquitetura

ev-population-etl/
├── analytics/
│   ├── dags/
│   │   ├── analysis.py
│   │   ├── extract.py
│   │   ├── load.py
│   │   ├── transform.py
│   │   └── etl_pipeline.py
│   ├── data/
│   │   └── Electric_Vehicle_Population_Data.csv
│   └── pyvenv.cfg
├── database.db
├── .gitignore
├── LICENSE
├── README.txt
└── requirements.txt


# Contribuições

Contribuições são bem-vindas! Se você tiver uma sugestão de melhoria ou correção, sinta-se à vontade para abrir um pull request. Certifique-se de que seus testes estão passando antes de submeter o PR.

# Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.




