<think>

# **Flask-daisyui-template v1** : Modèle d'Application Flask

Un combot gagant <br>
## Flask
Flask est un micro-framework Python léger pour construire des applications web. Il permet de créer facilement des API et des sites web dynamiques.

![Flask Logo](https://upload.wikimedia.org/wikipedia/commons/3/3c/Flask_logo.svg|width=200)
[Site officiel de Flask](https://flask.palletsprojects.com/)
# +

## DaisyUI
DaisyUI est une bibliothèque de composants UI pour Tailwind CSS. Elle offre des composants prêts à l'emploi pour créer des interfaces élégantes et modernes.


![DaisyUI Logo](https://img.daisyui.com/images/daisyui-logo/daisyui-logotype.svg|width=200)

[Site officiel de DaisyUI](https://daisyui.com/)

**Un modèle complet d'application Flask avec des extensions utiles pré-configurées.**

Utilisez ce modèle pour démarrer votre projet plus rapidement. Il inclut les extensions suivantes déjà configurées :

* **Flask-Login** - Gère les sessions utilisateurs pour Flask.
* **Flask-Uploads** - Gère le téléchargement et le service de fichiers.
* **Flask-Cache** - Ajoute un système de cache à l'application.
* **Flask-Admin** - Interface d'administration pour Flask.
* **Flask-Flatpages** - Gère des pages statiques basées sur des fichiers texte.
* **Flask-Gravatar** - Intégration simplifiée de Gravatar.
* **Flask-Mail** - Envoi de emails avec support pour les tests unitaires.
* **Flask-Restless** - Génère des API RESTful pour les modèles SQLAlchemy.
* **Flask-SQLAlchemy** - Intègre SQLAlchemy pour la gestion de bases de données.
* **Flask-PyMongo** - Support pour MongoDB via PyMongo.
* **Flask-Themes** - Permet de gérer plusieurs thèmes d'apparence.
* **Flask-WTF** - Intégration de WTForms avec CSRF, upload de fichiers et reCAPTCHA.

Mais integre egalement daisyui a tailwinds en *offline*. Vous trouverez un fichier de macro de composentes de daisy ui 5 dans **app/templates/components.html.**
---

## Prérequis
Python 3.8.5+ et pew.

---

## Installation

1. Clonez le dépôt :
   ```bash
   $ git clone https://github.com/Mr-KAM/flask-daisyui-template.git
   $ cd flask-daisyui-template
   ```

2. Installez les dépendances dans un virtualenv:
   ```bash
   $ pew new venv
   $ pew workon venv
   $ pip install -r requirements.txt
   ```

3. Lancez l'application :
   ```bash
   $ python run.py
   ```

4. Accédez à l'application via :
   ```
   http://localhost:5000
   ```

---

## Configuration
Toute la configuration se trouve dans : `configuration.py`.
