# proyecto-sysacad

## Instalación
1. Clona el repositorio.
2. Crea un entorno virtual en la carpeta del proyecto:
    ```
    python -m venv env_name
o bien podes hacerla en una carpeta diferente *(sugerido)*
    
    python -m venv C:\Users\userX\environments\gral_env



3. Activa el entorno. Dependiendo la terminal que uses, el comando varia: 
**Git Bash (Windows):**

    source env_name/Scripts/activate

**CMD (Windows):**

    env_name\Scripts\activate    

---
\
Una vez activado, deberías ver algo como (env_name) al inicio de la línea en tu terminal. Si no lo ves, pone 
    
    which python


4. Instala las dependencias en el entorno virtual seleccionado
    
    pip install -r requirements.txt