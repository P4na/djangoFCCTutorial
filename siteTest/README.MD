se utilizzi un sistema windows e hai problemi con lutilizzo del virtual env con errore 

".\venv\Scripts\activate.ps1 : Impossibile caricare il file C:\Develop\git\djangoFCCTutorial\siteTest\venv\Scripts\activate.ps1. L'esecuzione di script è disabilitata nel        
sistema in uso. Per ulteriori informazioni, vedere about_Execution_Policies all'indirizzo https://go.microsoft.com/fwlink/?LinkID=135170.
In riga:1 car:1
+ .\venv\Scripts\activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : Errore di protezione: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess"

devi usare nel terminale 

Set-ExecutionPolicy Unrestricted -Scope Process

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 