# Sites do Grupos de Pesquisa da UFPI

Sistema da Universidade Federal do Piauí para criação de páginas de Grupos de Pesquisa da UFPI. Além de disponibilizar as informações dos grupos internacionalmente, os usuário têm acesso a formúlario de contato e newsletter para manter contato com seus seguidores.

## Backup de dados (desenvolvimento)

Para facilitar o cadastro de dados durante o desenvolvimento deve-se salvar e atualizar o arquivo data.json com as informações mais atuais.

### Copiar dados do banco

```
$ python manage.py dumpdata --exclude auth.permission > data.json 
```

### Carregar dados no banco

```
$ python manage.py loaddata data.json
```

## Internacionalização

O idioma **Português** deve obrigatoriamente ser cadastrado com esse nome e a sigla **pt** no banco de dados, já que toda a internacionalização para o idioma, que é padrão no sistema, foi desenvolvida com esses parâmetros.

### Criar/Atualizar idioma

Para criar ou atualizar um arquivo de tradução deve-se estar na pasta **core** e usar o comando **makemessages** passando a sigla do idioma como parâmetro.

```
$ cd core

$ django-admin.py makemessages -l pt
```

### Compilar arquivo de idioma

Também deve-se estar na pasta **core** e usar o comando a seguir:

```
$ django-admin compilemessages
```