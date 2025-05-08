## CHATBOT APP

### Description

<p>This is an application meant to test the ability to:</p>
<ul>
<li>implement AI integrations</li>
<li>Create friendly user interfaces</li>
<li>handle API integrations</li>
</ul>

### Objectives

<ul>
<li>Enable user to input questions</li>
<li>Provide relevant answers to user questions</li>
<li>Show a history of user's previous queries</li>
</ul>

### Execution

#### Backend Service

<ul>
<li>First make sure you have Python and MySQL installed in your machine</li>
<li>Start the sql service in your machine</li>
<li>Create a database named Journalsappdb</li>
<li>Create a virtual environment for the backend using the following command: python -m venv env</li>
<li>Activate the virtual environment using the following command: source env/bin/activate - Linux env\Scripts\activate - Windows</li>
<li>Add the required dependencies in the virtual environment using the following command: pip install -r requirements.txt</li>
<li>Add tables to the database using python manage.py makemigrations and python manage.py migrate</li>
<li>Execute the backend using the following command: python manage.py runserver</li>
</ul>

#### Frontend Service

<ul>
<li>Navigate to the mobile directory on your command prompt</li>
<li>Run npm install to add the required node modules in your machine</li>
<li>Run npm start and select which platform to execute the application on</li>
</ul>
