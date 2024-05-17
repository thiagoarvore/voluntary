
<body>
    <header>
        <h1>App fullstack para Ajuda Psicológica Voluntária</h1>
        <p>Este repositório contém um aplicativo projetado para ajudar na organização e coordenação de voluntários durante desastres ou épocas difícies.</p>
        <p>Se você quiser discutir ideias, problemas ou contribuições, sinta-se à vontade para nos contactar.</p>
    </header>
    <section>
        <h2>Tecnologias Utilizadas</h2>
        <ul>
            <li><img src="https://skillicons.dev/icons?i=python" width="20" height="20"/> Python: Ambiente de execução.</li>
            <li><img src="https://skillicons.dev/icons?i=django" width="20" height="20"/> Django: ORM facilitando o gerenciamento do banco de dados.</li>
            <li><img src="https://skillicons.dev/icons?i=html" width="20" height="20"/> HTML: Solução para desenvolvimento de frontend.</li>
            <li><img src="https://skillicons.dev/icons?i=css" width="20" height="20"/> CSS: Arte visual.</li>
            <li><img src="https://skillicons.dev/icons?i=postgres" width="20" height="20"/> POSTGRES: Banco de dados relacional confiável.</li>
        </ul>
    </section>
    <section>
        <h2>Requisitos</h2>
        <p>Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:</p>
        <ul>
            <li>Python (versão recomendada: 3.7 ou superior)</li>
            <li>Django (instalado automaticamente ao seguir as instruções abaixo)</li>
            <li>Outras dependências listadas no arquivo <code>requirements.txt</code></li>
        </ul>
    </section>
    <section>
        <h2>Instalação</h2>
        <p>Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>pip install -r requirements.txt</pre></div>
    </section>
    <section>
        <h2>Rodar o projeto</h2>
        <p>Instale o Postgres</p>
        <p>Após instalar as dependências, aplique as migrations no banco de dados com o comando:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py migrate</pre></div>
        <p>Insira os dados do IBGE para estados e cidades com o comando:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py fetch_data</pre></div>
        <p>Inicie o servidor:</p>
        <div class="highlight highlight-source-shell notranslate position-relative overflow-auto" dir="auto"><pre>python manage.py runserver</pre></div>            
        </div>
    </section>
</body>
