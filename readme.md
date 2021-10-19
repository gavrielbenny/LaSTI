Pastikan anda telah memiliki Python 3, WSL, dan VSCode di dalam perangkat anda

Selanjutnya, lakukan Virtual Environment Setup
- sudo apt install pipenv    #install virtual environment
- pipenv shell      #aktivasi virtual env
- exit              #deaktivasi virtual env

Install FastAPI :
- pip3 install fastapi  #install FastAPI

Install Uvicorn:
- pipenv install uvicorn          #install uvicorn
- uvicorn main:app --reload     #menjalankan uvicorn

Setelah menjalangkan uvicorn, Buka IP:port yang disediakan uvicorn dan tambahkan /docs setelah link tersebut untuk mencoba fungsi GET, POST, PUT(Update), DELETE.

Contoh : http://127.0.0.1:8000/docs

Gavriel Benny
18219078
 